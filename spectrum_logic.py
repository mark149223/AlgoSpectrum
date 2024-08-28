import tkinter as tk

from tkinter import ttk
from common import *
import serial
import enum
import modbus_tk
import modbus_tk.defines as cst
from modbus_tk import modbus_rtu
from modbus_tk import utils
from tkinter import messagebox
from deploy_setting import *
from threading import Thread
import threading
import random
import time

class TimerClass:
    def __init__(self) -> None:
        self.start_time_ = 0
    def stop(self):
        self.start_time_ = 0
    def start(self):
        self.start_time_ = time.time()
    def get_real_time(self):
        return time.time()-self.start_time_

def init_spectrum_vars_(self):
    self.port = tk.StringVar(value='COM1')
    self.sampling_time_tk = tk.StringVar(value='100')
    self.sampling_time_tk.trace_add('write', self.update_sampling_time)
    self.sampling_time = round(float(100), 3)
    self.real_time = tk.StringVar(value='-')
    self.life_time = tk.StringVar(value='-')
    self.sampling_spectr_type = tk.StringVar(value=SamplingSpectrType.Ordinary.value)

    self.sampling_spectr = None
    self.sampling_life_time = None
    self.sampling_real_time = None

    self.connection_port_status = tk.StringVar(value=ConnectionStatus.OFF.value)
    self.spectrometr_status = tk.StringVar(value=SpectrometrStatus.OFF.value)
    self.usr_socket = None
    self.spectrum_commander = None
    self.responce_timeout = 2
    self.realtime_timer = TimerClass()

    self.transfer_speed = tk.IntVar(value=BodSpeed.s_9600.value)
    self.number_of_channels = tk.IntVar(value=NumberOfChannels.s_256.value)

    self.transfer_speed_set = tk.IntVar(value=self.transfer_speed.get())
    self.number_of_channels_set = tk.IntVar(value=self.number_of_channels.get())

    self.transfer_speed_list = [i.value for i in BodSpeed]
    self.number_of_channels_list = [i.value for i in NumberOfChannels]
    self.open_spectr_type_list = [i.value for i in OpenSpectrumType]

    self.open_spectr_type = tk.StringVar(value=OpenSpectrumType.AlgoSpectrum.value)




def set_port_(self, port):
    self.port.set(f'COM{port}')

def disconnect_from_port_(self):
    if not self.usr_socket:
        return
    self.usr_socket.close()
    self.usr_socket = None
    self.combobox_transfer_speed['state'] = 'readonly'
    self.connection_port_status.set(ConnectionStatus.OFF.value)



def connect_to_port_(self):
    #TODO: подключение к порту бага

    if self.usr_socket:
        self.usr_socket.close()
        self.usr_socket = None
    if not self.usr_socket:
        try:
            self.usr_socket = modbus_rtu.RtuMaster(
                serial.Serial(port=self.port.get(), baudrate=int(self.transfer_speed.get()), bytesize=8, parity='E', stopbits=1, xonxoff=0)
            )

            self.usr_socket.set_timeout(self.responce_timeout)
            self.usr_socket.set_verbose(False)  # without log info
        except Exception as ex:
            print(ex)
            self.usr_socket = None
            messagebox.showerror('Внимание: ', f"Не удалось подключиться")
            self.connection_port_status.set(ConnectionStatus.OFF.value)
        else:
            self.connection_port_status.set(ConnectionStatus.ON.value)
            self.combobox_transfer_speed['state'] = 'disabled'


def set_spectrometr_setting_(self):
    self.spectrometr_setting_window = tk.Toplevel(self)
    self.spectrometr_setting_window.title("Настройки спектрометра")
    w = 204
    h = 204
    self.spectrometr_setting_window.geometry(f'{w}x{h}+{self.x_coordinate}+{self.y_coordinate}')  # размер окна и сдвиги в пикселях от левого верхнего угла
    self.spectrometr_setting_window.config(bg='#C0C0C0')  # установили цвет фона

    FONT = 16
    SHIFT = 50

    tk.Label(self.spectrometr_setting_window, text='Скорость, бод:', anchor='w', bg='#C0C0C0', padx=0, pady=0,
             font=(self.font_type, -FONT)).place(x=0, y=1 * SHIFT)
    tk.Label(self.spectrometr_setting_window, text='Число каналов:', anchor='w', bg='#C0C0C0', padx=0, pady=0,
             font=(self.font_type, -FONT)).place(x=0, y=2* SHIFT)

    self.combobox_transfer_speed_set = ttk.Combobox(self.spectrometr_setting_window,
                                                values=self.transfer_speed_list,
                                                background='#C0C0C0',
                                                foreground='#C0C0C0',
                                                style='TCombobox',
                                                font=(self.font_type, 12),
                                                width=7,
                                                justify='center')
    self.combobox_transfer_speed_set['state'] = 'readonly'
    self.combobox_transfer_speed_set.bind("<<ComboboxSelected>>", self.transfer_speed_set_changed)
    self.combobox_transfer_speed_set.place(x=0 + 115, y=1 * SHIFT)
    self.combobox_transfer_speed_set.set(self.transfer_speed_set.get())
    '''-------------------------------------------------------------------------------------------------'''

    self.combobox_number_of_channels_set = ttk.Combobox(self.spectrometr_setting_window,
                                                    values=self.number_of_channels_list,
                                                    background='#C0C0C0',
                                                    foreground='#C0C0C0',
                                                    style='TCombobox',
                                                    font=(self.font_type, 12),
                                                    width=7,
                                                    justify='center')
    self.combobox_number_of_channels_set['state'] = 'readonly'
    self.combobox_number_of_channels_set.bind("<<ComboboxSelected>>", self.number_of_channels_set_changed)
    self.combobox_number_of_channels_set.place(x=0 + 115, y=2 * SHIFT)
    self.combobox_number_of_channels_set.set(self.number_of_channels_set.get())

    '''-------------------------------------------------------------------------------------------------'''

    setting_button_ok = tk.Button(self.spectrometr_setting_window, text="Ок", command=self.send_spectrometr_setting,
                                                    # background='#C0C0C0',
                                                    # foreground='#C0C0C0',
                                                    font=(self.font_type, 12),
                                                    width=7,
                                                    justify='center')
    setting_button_ok.place(x=0 + 70, y=3 * SHIFT)

def send_spectrometr_setting_(self):
    '''Проверка включения'''
    if self.usr_socket == None:
        messagebox.showerror('Внимание: ', f"Подлкючитесь к порту")
        self.spectrometr_setting_window.destroy()
        return
    self.spectrum_commander = SpectrumCommander(self.usr_socket, self.number_of_channels.get())
    try:
        self.spectrum_commander.write_spectrometer_param(self.transfer_speed_set.get(),
                                                         self.number_of_channels_set.get())
    except Exception:
        messagebox.showerror('Внимание: ', f"Не удалось отправить данные спектрометру")
        self.spectrum_commander = None
    else:
        messagebox.showinfo('Внимание: ', f"Новые данные установлены. Переподключитесь к порту")
        self.number_of_channels.set(self.number_of_channels_set.get())
        self.transfer_speed.set(self.transfer_speed_set.get())
        self.combobox_number_of_channels.set(self.number_of_channels.get())
        self.combobox_transfer_speed.set(self.transfer_speed.get())
        self.config_setting['BaudRate'] = self.transfer_speed.get()
        self.config_setting['NumberOfChannels'] = self.number_of_channels.get()
        self.write_config()
        self.spectrum_commander = None
        self.disconnect_from_port()
    self.spectrometr_setting_window.destroy()




class SpectrumCommander:
    def __init__(self, usr_socket, number_of_channels):
        self.usr_socket_ = usr_socket
        self.number_of_channels_ = number_of_channels
        self.ADC_sample_list_ = []


    def read_adc_coils(self, i):
        reg_quantity = 64
        if not DEBUG:
            result = self.usr_socket_.execute(1, cst.READ_HOLDING_REGISTERS, i * 64, reg_quantity, returns_raw=True)
            if not result:
                # messagebox.showerror("Ошибка работы спектрометра")
                raise Exception
            else:
                for g in range(reg_quantity):
                    number = int.from_bytes(result[2 * g:2 * (g + 1)], byteorder='little')
                    self.ADC_sample_list_.append(number)
        else:

            for g in range(reg_quantity):   
                a = random.randint(20, 100)
                self.ADC_sample_list_.append(a)

            time.sleep(0.02)

    def erase_spectrum_param(self):
        if not DEBUG:
            result = self.usr_socket_.execute(1, cst.WRITE_SINGLE_COIL, 0, output_value=1, returns_raw=True)
        else:
            result = 1
        if not result:
            raise Exception

    def write_spectrometer_param(self, transfer_speed_set, number_of_channels_set):

        # if not DEBUG:
        #     result = self.usr_socket_.execute(1, cst.WRITE_MULTIPLE_REGISTERS, starting_adress=3002, quantity_of_x = 3, returns_raw=True)
        #     if not result:
        #         raise Exception
        # else:
        #     result = 1

        if not DEBUG:
            try:
                result = self.usr_socket_.execute(1, cst.READ_HOLDING_REGISTERS, 2000, 2, returns_raw=True)
            except Exception:
                pass
            result = 1

    def enable_spectrum(self):
        if not DEBUG:
            result = self.usr_socket_.execute(1, cst.WRITE_SINGLE_COIL, 1, output_value=1, returns_raw=True)
        else:
            result = 1
        if not result:
            raise Exception

    def disable_spectrum(self):
        if not DEBUG:
            result = self.usr_socket_.execute(1, cst.WRITE_SINGLE_COIL, 1, output_value=0, returns_raw=True)
        else:
            result = 1
        if not result:
            raise Exception

    def get_lifetime(self):
        if not DEBUG:
            '''TODO: поменять на 3000'''
            result = self.usr_socket_.execute(1, cst.READ_HOLDING_REGISTERS, self.number_of_channels_, 2, returns_raw=True)

            if not result:
                raise Exception
            number = int.from_bytes(result[0:4], byteorder='little')
            time = number * 4 / 1000000
        else:

            time = random.randint(30, 99)
        return time

    def get_spectr(self):
        self.ADC_sample_list_ = []
        for i in range(int(self.number_of_channels_ / 64)):
            self.read_adc_coils(i)



        return pd.Series(self.ADC_sample_list_)

def start_sampling_(self):

    '''Проверка включения'''
    if self.usr_socket == None:
        messagebox.showerror('Внимание: ', f"Подлкючитесь к порту")
        return
    if self.spectrometr_status.get()==SpectrometrStatus.ON.value:
        messagebox.showerror('Внимание: ', f"Набор уже идёт")
        return
    self.spectrum_commander = SpectrumCommander(self.usr_socket, self.number_of_channels.get())
    '''Запуск спектрометра'''
    try:
        self.spectrum_commander.disable_spectrum()  # на всякий случай
        self.spectrum_commander.erase_spectrum_param()
        self.spectrum_commander.enable_spectrum()
        '''Ожидание пока дойдет сообщение'''
        time.sleep(11*6/self.transfer_speed.get())
        self.realtime_timer.start()
    except Exception:
        self.spectrometr_status.set(SpectrometrStatus.OFF.value)
        messagebox.showerror('Внимание: ', f"Не удалось связаться со спектрометром")
        return

    '''Создание массива спектра'''
    #TODO: Вынести в отдельную функцию
    if self.sampling_spectr_type.get() == SamplingSpectrType.Ordinary.value:
        self.spectr = pd.DataFrame({'energy': [i for i in range(self.number_of_channels.get())],
                           'N': [0 for i in range(self.number_of_channels.get())]})
        self.sampling_spectr = self.spectr
        self.spectr_flag.set(True)
    # elif self.getting_spectr_type.get() == GettingSpectrType.Sample.value:
    #     spectr = self.sample_spectr
    else:
        self.sample_spectr = pd.DataFrame({'energy': [i for i in range(self.number_of_channels.get())],
                           'N': [0 for i in range(self.number_of_channels.get())]})
        self.sampling_spectr = self.sample_spectr
        self.sample_spectr_flag.set(True)




    self.combobox_getting_spectr_type['state'] = 'disabled'

    self.combobox_number_of_channels['state'] = 'disabled'
    '''Запуск спектрометрического потока'''
    self.sampling_process = SamplingProcess(self.life_time, self.real_time,
                                            self.sampling_spectr, self.spectrum_commander, self.realtime_timer,
                                            self.transfer_speed)
    self.sampling_process.start()
    self.monitor(self.sampling_process)

    # self.spectrum_commander.enable_spectrum()
    self.spectrometr_status.set(SpectrometrStatus.ON.value)

def stop_sampling_(self):
    if self.usr_socket == None:
        messagebox.showerror('Внимание: ', f"Подлкючитесь к порту")
        return
    if self.spectrometr_status.get()==SpectrometrStatus.OFF.value:
        return
    self.spectrometr_status.set(SpectrometrStatus.OFF.value)




def monitor_(self, sampling_process):

        if sampling_process.is_alive():
            # check the thread every 100ms
            self.after(100, lambda: self.monitor(sampling_process))
        else:
            if self.spectrometr_status.get()==SpectrometrStatus.OFF.value:
                #TODO: Сделать такой универсальный обработчик ошибок
                try:
                    self.spectrum_commander.disable_spectrum()
                except Exception:
                    messagebox.showerror('Внимание: ', f"Не удалось отправит команду остановки спектрометру")
                '''Разблокирование combobox выбора'''
                self.combobox_getting_spectr_type['state'] = 'readonly'
                self.combobox_number_of_channels['state'] = 'readonly'


            elif sampling_process.is_error:
                self.stop_sampling()
                messagebox.showerror('Внимание: ', f"В ходе работы случилась ошибка передачи")

                try:
                    self.spectrum_commander.disable_spectrum()
                except Exception:
                    messagebox.showerror('Внимание: ', f"Не удалось отправит команду остановки спектрометру")
                self.combobox_getting_spectr_type['state'] = 'readonly'
                self.combobox_number_of_channels['state'] = 'readonly'

            elif float(self.life_time.get())<self.sampling_time:
                '''Запуск спектрометрического потока'''
                self.sampling_process = SamplingProcess(self.life_time, self.real_time,
                                                        self.sampling_spectr, self.spectrum_commander, self.realtime_timer,
                                                        self.transfer_speed)
                self.sampling_process.start()
                self.monitor(self.sampling_process)


                #                     self.CountNInBorder()
                #                       if anima
                #                     self.animate()
            elif float(self.life_time.get())>=self.sampling_time:
                self.stop_sampling()
                try:
                    self.spectrum_commander.disable_spectrum()
                except Exception:
                    messagebox.showerror('Внимание: ', f"Не удалось отправит команду остановки спектрометру")
                '''Разблокирование combobox выбора'''
                self.combobox_getting_spectr_type['state'] = 'readonly'
                self.combobox_number_of_channels['state'] = 'readonly'
            self.animate()

            '''Установка временных метрик для спектров'''
            if self.sampling_spectr_type.get() == SamplingSpectrType.Ordinary.value:
                self.spectr_life_time.set(self.life_time.get())
                self.spectr_real_time.set(self.real_time.get())
            else:
                self.sample_spectr_life_time.set(self.life_time.get())
                self.sample_spectr_real_time.set(self.real_time.get())



class SamplingProcess(Thread):
    def __init__(self, life_time, real_time, spectr,
                 spectrum_commander, realtime_timer, transfer_speed):
        super().__init__()
        self.transfer_speed = transfer_speed
        self.realtime_timer = realtime_timer
        self.spectrum_commander = spectrum_commander
        self.life_time = life_time
        self.real_time = real_time
        self.spectr = spectr
        self.is_error = 0
        self.delay = 8 * 11/self.transfer_speed.get()

        #
        # self.i = 0


    def run(self):
        if DEBUG:
            random.seed()
        try:
            '''Порядок важен. Запись времени производится когда сообщение на прием спектра будет получено
            контроллером'''
            self.real_time.set(round(self.realtime_timer.get_real_time() + self.delay,3))
            self.spectr.loc[:, 'N'] = self.spectrum_commander.get_spectr()
            # print(self.spectr)
            self.life_time.set(round(self.spectrum_commander.get_lifetime(),3))
        except Exception:
            self.is_error = 1


