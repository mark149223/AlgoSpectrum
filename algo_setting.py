from common import *
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from Algo.aglo_func import *

def init_setting_vars_(self):
    self.min_gain = tk.StringVar(value='1')
    self.max_gain = tk.StringVar(value='2')
    self.step_gain = tk.StringVar(value='0.01')

    self.primary_equation_a = tk.StringVar(value='28000')
    self.primary_equation_k = tk.StringVar(value='0.00022')
    self.primary_equation_u = tk.StringVar(value='0')

    self.approx_equation_a = tk.StringVar(value='-')
    self.approx_equation_k = tk.StringVar(value='-')
    self.approx_equation_u = tk.StringVar(value='-')

    self.left_border = tk.IntVar(value=0)
    self.right_border = tk.IntVar(value=0)

    self.left_analysis_border = tk.IntVar(value=0)
    self.right_analysis_border = tk.IntVar(value=256)

    self.left_approx_chunnel = tk.IntVar(value=0)
    self.right_approx_chunnel = tk.IntVar(value=0)

    self.left_mape = tk.IntVar(value=0)
    self.right_mape = tk.IntVar(value=0)

    self.stabilization_algo_type = tk.StringVar(value=AlgoType.Standart_1_2.value)
    self.stabilization_algo_type_list = [i.value for i in AlgoType]



    # self.view_N_in_border = tk.StringVar(value='-')
    # self.view_error_N_in_border = tk.StringVar(value='-')
    # self.view_relative_s =tk.StringVar(value='-')
    # self.view_error_relative_s =tk.StringVar(value='-')
    # self.view_life_time  = tk.StringVar(value='-')
    # self.view_real_time = tk.StringVar(value='-')
    #
    # self.view_N_in_border.set(self.sample_spectr_N_in_border.get())
    # self.view_error_N_in_border.set(self.sample_spectr_error_N_in_border.get())
    # self.view_relative_s.set(self.sample_spectr_relative_s.get())
    # self.view_error_relative_s.set(self.sample_spectr_error_relative_s.get())
    # self.view_life_time.set(self.sample_spectr_life_time.get())
    # self.view_real_time.set(self.sample_spectr_real_time.get())


    # self.metric_mass = []    self.sample_spectr_flag = 0
    # self.spectr_flag = 0
    # self.processed_spectr_flag = 0
    # self.cleaned_spectr_flag = 0
    # self.borders = 0



def create_setting_widgets_(self):
    FONT = 16
    SHIFT = 30
    tk.Label(self.setting_frame, text='Параметры MAPE-усиления:', anchor='w', bg='#C0C0C0', padx=0, pady=0,
             font=(self.font_type, -FONT)).place(x=self.width / 2 - 100, y=2*SHIFT)
    tk.Label(self.setting_frame, text='Минимум:', anchor='w', bg='#C0C0C0', padx=0, pady=0,
             font=(self.font_type, -FONT)).place(x=100, y=3*SHIFT)
    tk.Label(self.setting_frame, text='Максимум:', anchor='w', bg='#C0C0C0', padx=0, pady=0,
             font=(self.font_type, -FONT)).place(x=300 , y=3*SHIFT)
    tk.Label(self.setting_frame, text='Шаг:', anchor='w', bg='#C0C0C0', padx=0, pady=0,
             font=(self.font_type, -FONT)).place(x=530, y=3*SHIFT)

    min_gain_entry = tk.Entry(self.setting_frame, width=4, bg='#C0C0C0',
                                   font=(self.font_type, -FONT),
                                   textvariable=self.min_gain ,
                                   justify='center',
                                   ).place( x=100+84, y=3* SHIFT+5, height=18)
    max_gain_entry = tk.Entry(self.setting_frame, width=4, bg='#C0C0C0',
                                   font=(self.font_type, -FONT),
                                   textvariable=self.max_gain ,
                                   justify='center',
                                   ).place( x=300+88, y=3* SHIFT+5, height=18)
    step_gain_entry = tk.Entry(self.setting_frame, width=4, bg='#C0C0C0',
                                   font=(self.font_type, -FONT),
                                   textvariable=self.step_gain ,
                                   justify='center',
                                   ).place( x=530+42, y=3* SHIFT+5, height=18)


    tk.Label(self.setting_frame, text='Начальные параметры функции аппроксимации:',
             anchor='w', bg='#C0C0C0', padx=0, pady=0,
             font=(self.font_type, -FONT)).place(x=self.width / 2 - 190, y=4 * SHIFT)
    tk.Label(self.setting_frame, text='a:', anchor='w', bg='#C0C0C0', padx=0, pady=0,
             font=(self.font_type, -FONT)).place(x=100, y=5 * SHIFT)
    tk.Label(self.setting_frame, text='k:', anchor='w', bg='#C0C0C0', padx=0, pady=0,
             font=(self.font_type, -FONT)).place(x=282, y=5 * SHIFT)
    tk.Label(self.setting_frame, text='u:', anchor='w', bg='#C0C0C0', padx=0, pady=0,
             font=(self.font_type, -FONT)).place(x=530, y=5 * SHIFT)

    equation_a_entry=tk.Entry(self.setting_frame, width=10, bg='#C0C0C0',
                              font=(self.font_type, -FONT),
                              textvariable=self.primary_equation_a,
                              justify='center',
                              ).place( x=100+20, y=5* SHIFT+5, height=18)
    equation_k_entry=tk.Entry(self.setting_frame, width=10, bg='#C0C0C0',
                              font=(self.font_type, -FONT),
                              textvariable=self.primary_equation_k,
                              justify='center',
                              ).place( x=282+20, y=5* SHIFT+5, height=18)
    equation_u_entry=tk.Entry(self.setting_frame, width=10, bg='#C0C0C0',
                              font=(self.font_type, -FONT),
                              textvariable=self.primary_equation_u,
                              justify='center',
                              ).place( x=530+20, y=5* SHIFT+5, height=18)

    tk.Frame(self.setting_frame, bg='black', height=1, width=self.width).place(x=0, y=6 * SHIFT + 15)

    SHIFT2 = 50
    START_SHIFT = 7 * SHIFT


    tk.Label(self.setting_frame, text='Установка границ', anchor='w', bg='#C0C0C0', padx=0, pady=0,
             font=(self.font_type, -FONT)).place(x=20, y=START_SHIFT)
    tk.Label(self.setting_frame, text='Алгоритм стабилизации', anchor='w', bg='#C0C0C0', padx=0, pady=0,
             font=(self.font_type, -FONT)).place(x=20, y=START_SHIFT+SHIFT2)
    tk.Label(self.setting_frame, text='Устранение наплыва', anchor='w', bg='#C0C0C0', padx=0, pady=0,
             font=(self.font_type, -FONT)).place(x=20, y=START_SHIFT+2*SHIFT2)
    tk.Label(self.setting_frame, text='Расчёт метрик', anchor='w', bg='#C0C0C0', padx=0, pady=0,
             font=(self.font_type, -FONT)).place(x=20, y=START_SHIFT+3*SHIFT2)


    calculate_border_button = tk.Button(self.setting_frame,
                                        text="Применить",
                                        command=self.calculate_border,
                                        font=(self.font_type, 12),

                                        width=12,
                                        height=1,
                                        justify='center'
                                        )
    calculate_border_button.place(x=20 + 200, y=START_SHIFT-4)

    calculate_processed_spectr_button = tk.Button(self.setting_frame,
                                        text="Применить",
                                        command=self.calculate_processed_spectr,
                                        font=(self.font_type, 12),
                                        width=12,
                                        height=1,
                                        justify='center'
                                        )
    calculate_processed_spectr_button.place(x=20 + 200, y=START_SHIFT+SHIFT2-4)

    calculate_cleaned_spectr_button = tk.Button(self.setting_frame,
                                                  text="Применить",
                                                  command=self.calculate_cleaned_spectr,
                                                  font=(self.font_type, 12),
                                                  width=12,
                                                  height=1,
                                                  justify='center'
                                                  )
    calculate_cleaned_spectr_button.place(x=20 + 200, y=START_SHIFT + 2*SHIFT2 - 4)

    calculate_metrics_button = tk.Button(self.setting_frame,
                                                  text="Применить",
                                                  command=self.calculate_metrics,
                                                  font=(self.font_type, 12),
                                                  width=12,
                                                  height=1,
                                                  justify='center'
                                                  )
    calculate_metrics_button.place(x=20 + 200, y=START_SHIFT + 3*SHIFT2 - 4)

    tk.Label(self.setting_frame, text='Левая граница:', anchor='w', bg='#C0C0C0', padx=0, pady=0,
             font=(self.font_type, -FONT)).place(x=20 + 400, y=START_SHIFT)

    left_border_entry=tk.Entry(self.setting_frame, width=6, bg='#C0C0C0',
                                   font=(self.font_type, -FONT),
                                   textvariable=self.left_border ,
                                   justify='center',
                                   ).place(x=20 + 520, y=START_SHIFT+5, height=18)

    tk.Label(self.setting_frame, text='Тип алгоритма:', anchor='w', bg='#C0C0C0', padx=0, pady=0,
             font=(self.font_type, -FONT)).place(x=20 + 400, y=START_SHIFT+SHIFT2)

    tk.Label(self.setting_frame, text='Окно аппроксимации:', anchor='w', bg='#C0C0C0', padx=0, pady=0,
             font=(self.font_type, -FONT)).place(x=20 + 400, y=START_SHIFT + 2*SHIFT2)

    tk.Label(self.setting_frame, text='MAPE аппроксимация:', anchor='w', bg='#C0C0C0', padx=0, pady=0,
             font=(self.font_type, -FONT)).place(x=20 + 400, y=START_SHIFT + 3*SHIFT2)

    left_approx_channel_entry=tk.Entry(self.setting_frame, width=4, bg='#C0C0C0',
                                   font=(self.font_type, -FONT),
                                   textvariable=self.left_approx_chunnel ,
                                   justify='center',
                                   ).place(x=20 + 570, y=START_SHIFT+ 2*SHIFT2+5, height=18)

    right_approx_channel_entry=tk.Entry(self.setting_frame, width=4, bg='#C0C0C0',
                                   font=(self.font_type, -FONT),
                                   textvariable=self.right_approx_chunnel ,
                                   justify='center',
                                   ).place(x=20 + 620, y=START_SHIFT+ 2*SHIFT2+5, height=18)

    left_mape_entry=tk.Entry(self.setting_frame, width=4, bg='#C0C0C0',
                                   font=(self.font_type, -FONT),
                                   textvariable=self.left_mape ,
                                   justify='center',
                                   ).place(x=20 + 570, y=START_SHIFT+ 3*SHIFT2+5, height=18)

    right_mape_entry=tk.Entry(self.setting_frame, width=4, bg='#C0C0C0',
                                   font=(self.font_type, -FONT),
                                   textvariable=self.right_mape ,
                                   justify='center',
                                   ).place(x=20 + 620, y=START_SHIFT+ 3*SHIFT2+5, height=18)

    self.combobox_stabilization_algo_type = ttk.Combobox(self.setting_frame,
                                                values=self.stabilization_algo_type_list,
                                                background='#C0C0C0',
                                                foreground='#C0C0C0',
                                                style='TCombobox',
                                                font=(self.font_type, 12),
                                                width=14,
                                                justify='center')
    self.combobox_stabilization_algo_type['state'] = 'readonly'
    self.combobox_stabilization_algo_type.bind("<<ComboboxSelected>>", self.stabilization_algo_type_changed)
    self.combobox_stabilization_algo_type.place(x=20 + 520, y=START_SHIFT+SHIFT2)
    self.combobox_stabilization_algo_type.set(self.stabilization_algo_type.get())


def set_analysis_window_(self):
    pass
def show_analysis_window_(self):
    pass



def calculate_border_(self):
    # print(self.left_border.get())
    # print(self.sample_spectr)
    if not self.sample_spectr_flag.get():
        messagebox.showerror('Внимание: ', f"Калибровочный cпектр не загружен")
        return
    try:
        right_border = create_borders(self.sample_spectr,self.left_border.get())
    except Exception as ex:
        print(ex)
        messagebox.showerror('Внимание: ', f"Ошибка алгоритма")

    else:
        self.right_border.set(right_border)
        self.borders.set(True)
        self.animate()
        messagebox.showinfo('Внимание: ', f"Выполнено")
def calculate_processed_spectr_(self):
    if not self.spectr_flag.get():
        messagebox.showerror('Внимание: ', f"Cпектр не загружен")
        return
    if not self.borders.get():
        messagebox.showerror('Внимание: ', f"Не установлены границы")
        return
    try:
        if self.stabilization_algo_type.get() == AlgoType.Standart_1_2.value:
            self.processed_spectr = do_NAR_algo(self.sample_spectr, self.spectr,
                        self.left_border.get(),self.right_border.get(),
                        float(self.min_gain.get()),float(self.max_gain.get()),
                        float(self.step_gain.get()))
        else:   #self.stabilization_algo_type.get() == AlgoType.MAPE.value
            self.processed_spectr = do_mape_algo(self.sample_spectr, self.spectr,
                        self.left_border.get(),self.right_border.get(),
                        float(self.min_gain.get()),float(self.max_gain.get()),
                        float(self.step_gain.get()),self.left_mape.get(), self.right_mape.get())
    except Exception as ex:
        print(ex)
        messagebox.showerror('Внимание: ', f"{ex}")
    else:
        self.processed_spectr_flag.set(True)
        self.animate()
        messagebox.showinfo('Внимание: ', f"Выполнено")
def calculate_cleaned_spectr_(self):
    if not self.processed_spectr_flag.get():
        messagebox.showerror('Внимание: ', f"Преобразованный спектр отсутствует")
        return
    try:
        processed_a, processed_k, processed_u, \
            self.gamma_spectr, self.gamma_approx_spectr, self.cleaned_spectr = exclude_gamma_part(self.sample_spectr,
                                                                                         self.processed_spectr,
                                                                                         self.left_approx_chunnel.get(),
                                                                                         self.right_approx_chunnel.get(),
                                                                                         float(self.primary_equation_a.get()),
                                                                                         float(self.primary_equation_k.get()),
                                                                                         float(self.primary_equation_u.get()),
                                                                                         self.left_border.get(),
                                                                                         self.right_border.get(),
                                                                                         self.left_mape.get(),
                                                                                         self.right_mape.get())
    except Exception as ex:
        print(ex)
        messagebox.showerror('Внимание: ', f"Ошибка алгоритма")
    else:
        self.approx_equation_a.set(str(round(processed_a,1)))
        self.approx_equation_k.set(str(round(processed_k,5)))
        self.approx_equation_u.set(str(round(processed_u,1)))
        self.cleaned_spectr_flag.set(True)
        self.animate()
        messagebox.showinfo('Внимание: ', f"Выполнено")
def calculate_metrics_(self):
    if not self.borders.get():
        messagebox.showerror('Внимание: ', f"Границы не установлены")
        return
    try:

        for ix, spectr_param in enumerate(self.metric_mass):
            if spectr_param[7].get():

                #TODO: убрать и продумать логику корректнее
                if ix == 0:
                    spectr =  self.sample_spectr
                elif ix == 1:
                    spectr =  self.spectr
                elif ix == 2:
                    spectr =  self.processed_spectr
                else:
                    spectr =  self.cleaned_spectr


                n_at_border = calculate_n_at_borders(spectr, self.left_border.get(), spectr['energy'].iloc[-1])
                n_at_border_error = calculate_n_at_borders_error(self.sample_spectr, spectr, self.left_border.get(),
                                                                 spectr['energy'].iloc[-1])
                s_relation = calculate_s_relation(spectr, self.left_border.get(), self.right_border.get())
                s_relation_error = calculate_s_relation_error(self.sample_spectr, spectr, self.left_border.get(),
                                                              self.right_border.get())
                spectr_param[1].set(str(round(n_at_border)))
                spectr_param[2].set(str(round(n_at_border_error, 2)))
                spectr_param[3].set(str(round(s_relation,3)))
                spectr_param[4].set(str(round(s_relation_error, 2)))

    except Exception as ex:
        print(ex)
        messagebox.showerror('Внимание: ', f"Ошибка в ходе расчёта")
    else:
        messagebox.showinfo('Внимание: ', f"Выполнено")

