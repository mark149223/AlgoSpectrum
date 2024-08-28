import enum
import tkinter as tk
import pandas as pd
import json
from tkinter import ttk
# class SpectrumStatusEnum(enum.Enum):
#     process = 0
#     pause = 1
#     stop = 2

def init_common_var_(self):
    self.config_setting = None
    self.sample_spectr = None
    self.spectr = None
    self.processed_spectr = None
    self.cleaned_spectr = None

    self.gamma_spectr = None
    self.gamma_approx_spectr = None

    self.sample_spectr_flag = tk.BooleanVar(value=False)
    self.spectr_flag = tk.BooleanVar(value=False)
    self.processed_spectr_flag = tk.BooleanVar(value=False)
    self.cleaned_spectr_flag = tk.BooleanVar(value=False)
    self.borders = tk.BooleanVar(value=False)

    self.sample_spectr_life_time = tk.StringVar(value='-')
    self.sample_spectr_real_time = tk.StringVar(value='-')
    self.spectr_life_time  = tk.StringVar(value='-')
    self.spectr_real_time = tk.StringVar(value='-')
    self.processed_spectr_life_time  = self.spectr_life_time
    self.processed_spectr_real_time = self.spectr_real_time
    self.cleaned_spectr_life_time  = self.spectr_life_time
    self.cleaned_spectr_real_time = self.spectr_real_time

    self.spectrum_frame = tk.Frame(self)
    self.setting_frame = tk.Frame(self)
    self.plot_frame = tk.Frame(self)

    self.spectrum_frame.config(bg='#C0C0C0')  # установили цвет фона
    self.setting_frame.config(bg='#C0C0C0')  # установили цвет фона
    self.plot_frame.config(bg='#C0C0C0')  # установили цвет фона


    self.count = 0
    self.load = 0
    self.error = 0

    self.count_tk = tk.StringVar(value='-')
    self.load_tk = tk.StringVar(value='-')
    self.error_tk = tk.StringVar(value='-')
    self.show_border_tk = tk.StringVar(value='-')

    self.window_mode = WindowMode.Spectrum.value


def open_config_(self):
    with open(self.config_file_path, 'r') as file:
        self.config_setting = json.load(file)

def set_config_(self):
    self.transfer_speed.set(self.config_setting['BaudRate'])
    self.number_of_channels.set(self.config_setting['NumberOfChannels'])
def write_config_(self):
    with open(self.config_file_path, 'w') as file:
        json.dump(self.config_setting, file)
def set_window_mode_(self, mode):
    self.window_mode = mode
    if self.window_mode == WindowMode.Spectrum.value:
        self.setting_frame.place_forget()
        self.plot_frame.place_forget()
        self.spectrum_frame.place(x=0, y=0, width=self.width, height=self.height)



    elif self.window_mode == WindowMode.Setting.value:
        self.plot_frame.place_forget()
        self.spectrum_frame.place_forget()
        self.setting_frame.place(x=0, y=0, width=self.width, height=self.height)


    elif self.window_mode == WindowMode.Plot.value:
        self.setting_frame.place_forget()
        self.spectrum_frame.place_forget()
        self.plot_frame.place(x=0, y=0, width=self.width, height=self.height)



class WindowMode(enum.Enum):
    Spectrum = "Спектрометр"
    Setting = "Настройка"
    Plot = "Монитор"

class ConnectionStatus(enum.Enum):
    ON = "Подключен"
    OFF = "Отключен"

class SpectrometrStatus(enum.Enum):
    ON = 'Идёт набор'
    OFF = 'Остановлен'

class SamplingSpectrType(enum.Enum):
    Sample = "Калибровочный"
    Ordinary = "Обычный"

class BodSpeed(enum.Enum):
    s_2400 = 2400
    s_4800 = 4800
    s_9600 = 9600
    s_19200 = 19200
    s_38400 = 38400
    s_57600 = 57600
    s_115200 = 115200

class NumberOfChannels(enum.Enum):
    s_256 = 256
    s_512 = 512
    s_1024 = 1024


class OpenSpectrumType(enum.Enum):
    SpFe = 'SpFe'
    Spectrum = 'Spectrum'
    AlgoSpectrum = 'AlgoSpectrum'

class AlgoType(enum.Enum):
    Standart_1_2 = 'Алгоритм 1/2'
    MAPE = 'Алгоритм MAPE'

class SpectrType(enum.Enum):
    Sample = 'Калибровочный'
    Ordinary = 'Спектр'
    Processed = 'Преобразованный'
    Cleaned = 'Очищенный'
