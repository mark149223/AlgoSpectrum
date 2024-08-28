import math

import numpy as np
from Algo.algo_common import *
import time
from scipy.optimize import curve_fit


def find_right_border(spectr_sample, LEFT_BORDER, integral_from_leftborder_to_end):
    '''Находит правую границу (целую), левая граница целая
    Считается что в границе значение не учитывается и оно аппаратно находится левее границы'''
    integral_for_border_definition = 0
    integral_on_section = 0
    right_border = 0
    for i, row in spectr_sample.iterrows():  # находим правую границу
        if i == len(spectr_sample) - 1:  # на этом заканчивается, т.к последний участок [i-1, i] учтен
            break
        x_first = spectr_sample['energy'].iloc[i]  # аргумент начала прямой
        y_first = spectr_sample['N'].iloc[i]  # аргумент начала прямой
        if x_first > LEFT_BORDER:
            integral_on_section = y_first
            integral_for_border_definition += integral_on_section
            if math.isclose(integral_for_border_definition,
                            integral_from_leftborder_to_end / 2):  # это сравнение двух float чисел с точностью 1e-9
                right_border = x_first
                break
            if integral_for_border_definition > (integral_from_leftborder_to_end / 2):
                right_border = x_first
                break

    if right_border:
        return right_border
    else:
        raise Exception



def calculate_s_relation(spectr, left_border, right_border):
    # Считает (left, max], (right,
    max_channel_number = spectr.shape[0] - 1
    full_integral = calculate_spectr_integral(spectr,
                                              left_border+1,
                                              max_channel_number)

    tail_integral = calculate_spectr_integral(spectr,
                                              right_border+1,
                                              max_channel_number)
    S_relation = full_integral / tail_integral
    return S_relation

def calculate_s_relation_error(spectr_sample,spectr, left_border, right_border):
    sample_spectr_s_relation = calculate_s_relation(spectr_sample, left_border, right_border)
    spectr_s_relation = calculate_s_relation(spectr, left_border, right_border)
    percent_relative_error = (spectr_s_relation-sample_spectr_s_relation)*100/sample_spectr_s_relation
    return percent_relative_error


def calculate_n_at_borders_error(spectr_sample,spectr, left_border, right_border):
    sample_spectr_n_at_borders = calculate_spectr_integral(spectr_sample,
                                              left_border+1,
                                              right_border)
    spectr_n_at_borders = calculate_spectr_integral(spectr,
                                              left_border+1,
                                              right_border)
    percent_relative_error = (spectr_n_at_borders-sample_spectr_n_at_borders)*100/sample_spectr_n_at_borders
    return percent_relative_error

def calculate_n_at_borders(spectr, left_border, right_border):
    integral = calculate_spectr_integral(spectr,
                                              left_border+1,
                                              right_border)
    return integral

def do_mape_algo(spectr_sample, spectr_for_gain,
                        left_border,right_border,
                        gain_factor_min,gain_factor_max,
                        gain_factor_step, left_mape, right_mape):
    gain_koff = find_gain_koff_MAPE(spectr_sample, spectr_for_gain,
                        left_border,right_border,
                        gain_factor_min,gain_factor_max,
                        gain_factor_step, left_mape, right_mape)
    processed_spectr = full_expand_spectrum(spectr_for_gain, gain_koff)
    return processed_spectr

def do_NAR_algo(spectr_sample, spectr_for_gain,
                        left_border,right_border,
                        gain_factor_min,gain_factor_max,
                        gain_factor_step):
    '''В качестве начального параметра использует
    gain_factor_min
    '''


    RELATIVE_MIN = 1.99
    RELATIVE_MAX = 2.01
    STEP = 0.01
    gain_koff = gain_factor_min
    MAX_EXECUTE = 10
    relative_s = calculate_s_relation(spectr_for_gain, left_border, right_border)
    processed_spectr = None
    start = time.time()
    if RELATIVE_MIN<=relative_s<=RELATIVE_MAX:
        return spectr_for_gain
    else:
        while not (RELATIVE_MIN<=relative_s<=RELATIVE_MAX):
            if relative_s<RELATIVE_MIN: # сжатие
                gain_koff-= STEP
                processed_spectr = full_expand_spectrum(spectr_for_gain, gain_koff)
                relative_s =  calculate_s_relation(processed_spectr, left_border, right_border)
            else:   # relative_s>RELATIVE_MAX   # растяжение
                gain_koff += STEP
                processed_spectr = full_expand_spectrum(spectr_for_gain, gain_koff)
                relative_s =  calculate_s_relation(processed_spectr, left_border, right_border)

            if (time.time()-start)>MAX_EXECUTE:
                raise Exception('Срыв алгоритма стабилизации. Прошло более 30 с')


    return processed_spectr





def generate_expusr_function(a):
    # Функция-оболочка, принимающая x и возвращающая результат f(x) = ax + b
    def expusr(x, k, u):
        return a * np.exp(-k * ((x - u) ** 2))
    # Возвращаем функцию linear_function
    return expusr

def exclude_gamma_part(spectr_sample, spectr_processed,
                       left_interval, right_interval,
                       init_a, init_k, init_u, left_border,
                       right_border, left_mape, right_mape):
    spectr_gamma = spectr_processed.copy()
    spectr_approx_gamma = spectr_processed.copy()
    spectr_without_gamma = spectr_processed.copy()
    initial_guess = [init_k, init_u]
    '''Скорректировать их по высоте'''
    mean_linear_difference = correct_contration_difference(spectr_sample, spectr_gamma, left_mape, right_mape)
    spectr_gamma.loc[:, 'N'] = spectr_gamma['N']-spectr_sample['N']    # оставить только гамма
    '''Вернуть начальную высоту'''
    spectr_gamma.loc[:, 'N'] = spectr_gamma['N']/mean_linear_difference

    x_data = spectr_gamma['energy'][left_interval:right_interval+1]
    y_data = spectr_gamma['N'][left_interval:right_interval+1]

    x_data.astype('float64')
    y_data.astype('float64')

    expusr_generate = generate_expusr_function(init_a)


    try:
        popt, pcov = curve_fit(expusr_generate, x_data, y_data, p0=initial_guess)
    except Exception:
        print('не обнаружено')
        raise Exception('Не обнаружена гамма-составляющая')

    # Генерация значений для графика
    x_fit = spectr_gamma['energy']
    y_fit = expusr_generate(x_fit, *popt)
    spectr_approx_gamma.loc[:, 'N'] = y_fit

    spectr_without_gamma.loc[:, 'N'] = spectr_without_gamma['N'] - spectr_approx_gamma['N']

    processed_a = init_a
    processed_k = popt[0]
    processed_u = popt[1]

    return processed_a, processed_k, processed_u, \
        spectr_gamma,spectr_approx_gamma, spectr_without_gamma

def create_borders(spectr_sample,left_border):
    '''Создает начальные границы
    Принимает калибровочный спектр и левую границу
    Cчитает интеграл от левой границы не включая'''

    if left_border < 0 or left_border >= (len(spectr_sample) - 1):
        raise SettingLeftBorderError('the left border is out of the spectrum')
    max_channel_number = spectr_sample.shape[0]-1   # номер последнего канала
    integral_from_leftborder_to_end = calculate_spectr_integral(spectr_sample, left_border+1,
                                                 max_channel_number)  # суммарный интеграл начиная с LEFT_BORDER
    if math.isclose(integral_from_leftborder_to_end, 0):  # Проверка того, что площадь после левой границы не ноль
        raise SettingLeftBorderError(
            'The area of the figure to the right of the left border is equal to zero. Please check the value of the left border')

    right_border = find_right_border(spectr_sample, left_border, integral_from_leftborder_to_end)
    return right_border


def full_expand_spectrum(spectr_for_gain, gain_koff):
    zeros_df = pd.DataFrame({'energy': [0], 'N': [0]})
    spectr_for_gain_processed = spectr_for_gain.copy()
    spectr_for_gain_processed['energy'] = spectr_for_gain_processed['energy'] + 1
    spectr_for_gain_processed = pd.concat([zeros_df, spectr_for_gain_processed], ignore_index=True)

    spectr_for_gain_processed['N'] = spectr_for_gain_processed['N'].astype(float)
    spectr_for_gain_processed['energy'] = spectr_for_gain_processed['energy'].astype(int)  # преобразуем энергию в int

    expand_spectr = spectr_for_gain_processed.copy()
    discretized_expand_spectr = spectr_for_gain_processed.copy()

    first_expand_spectr(spectr_for_gain_processed,expand_spectr, gain_koff)
    correct_discretization(discretized_expand_spectr, expand_spectr, gain_koff)

    expand_spectrum = discretized_expand_spectr.drop(discretized_expand_spectr.index[0]).reset_index(drop=True)
    expand_spectrum['energy'] = expand_spectrum['energy'] - 1
    return expand_spectrum

def find_gain_koff_MAPE(spectr_sample, spectr_for_gain,
                        LEFT_BORDER,RIGHT_BORDER,
                        GAIN_FACTOR_MIN,GAIN_FACTOR_MAX,
                        GAIN_FACTOR_STEP, left_mape, right_mape):
    MAPE_list = []
    gain_koff_array =  np.arange(GAIN_FACTOR_MIN, GAIN_FACTOR_MAX + GAIN_FACTOR_STEP, GAIN_FACTOR_STEP)
    '''Преобразование датафрейма'''
    zeros_df = pd.DataFrame({'energy': [0], 'N': [0]})
    spectr_for_gain_processed = spectr_for_gain.copy()
    spectr_sample_added = spectr_sample.copy()


    spectr_for_gain_processed.loc[:, 'energy'] = spectr_for_gain_processed['energy'] + 1
    spectr_sample_added.loc[:, 'energy'] = spectr_sample_added['energy'] + 1

    spectr_for_gain_processed = pd.concat([zeros_df, spectr_for_gain_processed], ignore_index=True)
    spectr_sample_added = pd.concat([zeros_df,spectr_sample_added], ignore_index=True)

    spectr_for_gain_processed['N'] = spectr_for_gain_processed['N'].astype(float)
    spectr_for_gain_processed['energy'] = spectr_for_gain_processed['energy'].astype(int)   # преобразуем энергию в int

    expand_spectr = spectr_for_gain_processed.copy()
    discretized_expand_spectr = spectr_for_gain_processed.copy()

    left_border = LEFT_BORDER+1 # из-за смещения
    right_border = RIGHT_BORDER + 1 # из-за смещения

    for gain_koff in gain_koff_array:
        first_expand_spectr(spectr_for_gain_processed,expand_spectr, gain_koff)
        correct_discretization(discretized_expand_spectr, expand_spectr, gain_koff)
        correct_contration_difference(spectr_sample_added, discretized_expand_spectr, left_mape, right_mape)
        mape = findMAPE(spectr_sample_added,discretized_expand_spectr,
                        left_mape, right_mape)
        MAPE_list.append(mape)
    MAPE_list = np.array(MAPE_list)
    ix_min_mape = find_ix_min_mape(MAPE_list)
    return gain_koff_array[ix_min_mape]


def find_ix_min_mape(MAPE_list):
    min_index = np.argmin(MAPE_list)
    return min_index

def correct_contration_difference(spectr_sample,middle_discretized_spectr,left_mape, right_mape):
    '''Умножить на линейную разницу спектр middle_discretized_spectr'''

    left_slice = left_mape
    right_slice = right_mape
    N_sample = spectr_sample['N'][left_slice:(right_slice+1)]

    N_spectr = middle_discretized_spectr['N'][left_slice:(right_slice+1)]
    mean_linear_difference = np.mean(N_sample/N_spectr)
    middle_discretized_spectr.loc[:, 'N'] = middle_discretized_spectr['N']*mean_linear_difference
    return mean_linear_difference

def findMAPE(spectr_sample,middle_discretized_spectr,left_mape, right_mape):
    # left_interval_border = left_border + int((right_border-left_border)/2)
    # right_interval_border = right_border

    left_interval_border = left_mape

    right_interval_border = right_mape

    def mape(sample, spectr):
        '''Значения sample никогда не ноль'''
        return  np.sum(np.abs((spectr - sample) / sample))

    sample_slice = spectr_sample[(spectr_sample['energy'] >= left_interval_border) &
                                 (spectr_sample['energy'] <= right_interval_border)]
    spectr_slice = middle_discretized_spectr[(middle_discretized_spectr['energy'] >= left_interval_border) &
                                             (middle_discretized_spectr['energy'] <= right_interval_border)]

    mape_value = mape(sample_slice['N'], spectr_slice['N'])
    return mape_value


def first_expand_spectr(spectr_for_gain_processed,expand_spectr, gain_koff):
    '''spectr_for_gain_processed - спектр с 0 в начале '''
    # Умножаем каждый столбец x на коэффициент koff
    expand_spectr['energy'] = spectr_for_gain_processed['energy'] * gain_koff
    # Преобразуем числа в столбце x в int, если после операций они стали целыми
    expand_spectr['energy'] = expand_spectr['energy'].apply(lambda x: int(x) if math.isclose(x, int(x)) else x) # преобразуем целочисленную энергию в int

def correct_discretization(discretized_expand_spectr, expand_spectr, gain_koff):
    '''Выполняет поправку дискретизации
    @retval discretized_expand_spectr
    Работает только на расширение, считаем, что интервал всегда больше отрезка,
    отрезок = 1

    Можно оптимизировать уменьшить число обращений к датафреймам'''

    discretized_N_mass = [0 for i in range(expand_spectr.shape[0]*int(math.ceil(gain_koff)))]
    g = 0 # число исследуемых обычных интервалов
    if gain_koff!= 1:
        for channel in range(expand_spectr.shape[0] - 1):
            en_1 = expand_spectr['energy'].iloc[channel]  # аргумент начала прямой
            en_2 = expand_spectr['energy'].iloc[channel + 1]  # аргумент конца прямой
            N = expand_spectr['N'].iloc[channel + 1]  # значение на конце интервала

            en_1_ceil = int(math.ceil(en_1))
            en_2_ceil = int(math.ceil(en_2))
            en_2_floor = int(math.floor(en_2))



            if en_1_ceil==en_2_ceil:
                discretized_N_mass[en_1_ceil]+= N
            else:
                add_N = (en_1_ceil-en_1)*N/gain_koff
                discretized_N_mass[en_1_ceil] += add_N
                i=1
                while en_1_ceil+i <= en_2:  # Если en_2 на границе
                    add_N = N/gain_koff
                    discretized_N_mass[en_1_ceil+i] = add_N
                    i+=1
                add_N = (en_2-en_2_floor)*N/gain_koff
                discretized_N_mass[en_2_ceil] += add_N

        discretized_N_mass = discretized_N_mass[:expand_spectr.shape[0]]
        # print(discretized_N_mass)
        discretized_expand_spectr.loc[:, 'N'] = pd.Series(discretized_N_mass)

    else:
        discretized_expand_spectr = expand_spectr.copy()