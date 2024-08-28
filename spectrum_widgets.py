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



def create_spectrum_static_widgets_(self):
    FONT = 16
    SHIFT = 30


    tk.Label(self.spectrum_frame, text='Выбор порта:', anchor='w', bg='#C0C0C0', padx=0, pady=0,
             font=(self.font_type, -FONT)).place(x=0, y= 2*SHIFT)
    tk.Label(self.spectrum_frame, text='Статус подключения к порту:', anchor='w', bg='#C0C0C0', padx=0, pady=0,
             font=(self.font_type, -FONT)).place(x=0, y=3*SHIFT)

    tk.Label(self.spectrum_frame, textvariable=self.connection_port_status, anchor='w', bg='#C0C0C0', padx=0, pady=0,
             font=(self.font_type, -FONT)).place(x=220, y=3 * SHIFT)

    tk.Label(self.spectrum_frame, textvariable=self.spectrometr_status, anchor='w', bg='#C0C0C0', padx=0, pady=0,
             font=(self.font_type, -FONT)).place(x=160, y=4 * SHIFT)

    tk.Label(self.spectrum_frame, text='Статус спектрометра:', anchor='w', bg='#C0C0C0', padx=0, pady=0,
             font=(self.font_type, -FONT)).place(x=0, y=4*SHIFT)
    tk.Label(self.spectrum_frame, text='Тип набираемого спектра:', anchor='w', bg='#C0C0C0', padx=0, pady=0,
             font=(self.font_type, -FONT)).place(x=self.width/2, y=2*SHIFT)
    tk.Label(self.spectrum_frame, text='Платформа спектра извне:', anchor='w', bg='#C0C0C0', padx=0, pady=0,
             font=(self.font_type, -FONT)).place(x=self.width / 2, y=3 * SHIFT)

    tk.Label(self.spectrum_frame, text='Скорость, бод:', anchor='w', bg='#C0C0C0', padx=0, pady=0,
             font=(self.font_type, -FONT)).place(x=0, y=5 * SHIFT)
    tk.Label(self.spectrum_frame, text='Число каналов:', anchor='w', bg='#C0C0C0', padx=0, pady=0,
             font=(self.font_type, -FONT)).place(x=self.width/2, y=5* SHIFT)

    tk.Frame(self.spectrum_frame, bg='black', height=1, width=self.width).place(x=0, y=6*SHIFT+15)

    tk.Label(self.spectrum_frame, text='Время набора, с:', anchor='w', bg='#C0C0C0', padx=0, pady=0,
             font=(self.font_type, -FONT)).place(x=0, y= 7*SHIFT)
    tk.Label(self.spectrum_frame, text='Живое время, с:', anchor='w', bg='#C0C0C0', padx=0, pady=0,
             font=(self.font_type, -FONT)).place(x=0, y= 8*SHIFT)
    tk.Label(self.spectrum_frame, text='Реальное время, с:', anchor='w', bg='#C0C0C0', padx=0, pady=0,
             font=(self.font_type, -FONT)).place(x=self.width/2, y=8 * SHIFT)

    tk.Label(self.spectrum_frame, textvariable=self.port, anchor='w', bg='#C0C0C0', padx=0, pady=0,
             font=(self.font_type, -FONT)).place(x=102, y=2 * SHIFT)

    tk.Label(self.spectrum_frame, textvariable=self.life_time, anchor='w', bg='#C0C0C0', padx=0, pady=0,
             font=(self.font_type, -FONT)).place(x=120, y=8 * SHIFT)
    tk.Label(self.spectrum_frame, textvariable=self.real_time, anchor='w', bg='#C0C0C0', padx=0, pady=0,
             font=(self.font_type, -FONT)).place(x=self.width / 2+140, y=8 * SHIFT)

    '''-------------------------------------------------------------------------------------------------'''
    sampling_time_entry = tk.Entry(self.spectrum_frame, width=9, bg='#C0C0C0',
                                   font=(self.font_type, -FONT),
                                   textvariable=self.sampling_time_tk,
                                   justify='center',
                                   ).place( x=130, y=7 * SHIFT+3, height=22)


def create_spectrum_combobox_widgets_(self):
    FONT = 16
    SHIFT = 30
    combobox_getting_spectr_type_list = [SamplingSpectrType.Ordinary.value,
                                         SamplingSpectrType.Sample.value]


    self.combobox_getting_spectr_type = ttk.Combobox(self.spectrum_frame,
                                                     values=combobox_getting_spectr_type_list,
                                                      background = '#C0C0C0',
                                                      foreground = '#C0C0C0',
                                                      style='TCombobox',
                                                      font=(self.font_type, 12),
                                                      width=15,
                                                      justify='center' )
    self.combobox_getting_spectr_type['state'] = 'readonly'
    self.combobox_getting_spectr_type.bind("<<ComboboxSelected>>", self.getting_spectr_type_changed)
    self.combobox_getting_spectr_type.place(x=self.width/2+200, y=2*SHIFT)
    self.combobox_getting_spectr_type.set(self.sampling_spectr_type.get())
    '''-------------------------------------------------------------------------------------------------'''



    self.combobox_transfer_speed = ttk.Combobox(self.spectrum_frame,
                                                     values=self.transfer_speed_list,
                                                      background = '#C0C0C0',
                                                      foreground = '#C0C0C0',
                                                      style='TCombobox',
                                                      font=(self.font_type, 12),
                                                      width=7,
                                                      justify='center' )
    self.combobox_transfer_speed['state'] = 'readonly'
    self.combobox_transfer_speed.bind("<<ComboboxSelected>>", self.transfer_speed_changed)
    self.combobox_transfer_speed.place(x=0+115, y=5*SHIFT)
    self.combobox_transfer_speed.set(self.transfer_speed.get())
    '''-------------------------------------------------------------------------------------------------'''



    self.combobox_number_of_channels = ttk.Combobox(self.spectrum_frame,
                                                     values=self.number_of_channels_list,
                                                      background = '#C0C0C0',
                                                      foreground = '#C0C0C0',
                                                      style='TCombobox',
                                                      font=(self.font_type, 12),
                                                      width=7,
                                                      justify='center' )
    self.combobox_number_of_channels['state'] = 'readonly'
    self.combobox_number_of_channels.bind("<<ComboboxSelected>>", self.number_of_channels_changed)
    self.combobox_number_of_channels.place(x=self.width/2+115, y=5*SHIFT)
    self.combobox_number_of_channels.set(self.number_of_channels.get())
    '''-------------------------------------------------------------------------------------------------'''
    self.combobox_open_spectr_type = ttk.Combobox(self.spectrum_frame,
                                                    values=self.open_spectr_type_list,
                                                    background='#C0C0C0',
                                                    foreground='#C0C0C0',
                                                    style='TCombobox',
                                                    font=(self.font_type, 12),
                                                    width=13,
                                                    justify='center')
    self.combobox_open_spectr_type['state'] = 'readonly'
    self.combobox_open_spectr_type.bind("<<ComboboxSelected>>", self.open_spectr_type_changed)
    self.combobox_open_spectr_type.place(x=self.width/2+200, y=3 * SHIFT)
    self.combobox_open_spectr_type.set(self.open_spectr_type.get())









# def create_check_buttons(self):
#
#     tk.Checkbutton(self, text='Калибровочный спектр', font=('Times New Roman', -FONT), bg='#C0C0C0',
#                    variable=self.graph_spectr_for_border_definition,
#                    offvalue=False,
#                    onvalue=True, command=self.animate).place(
#         x=10, y=9 * SHIFT)
#     tk.Checkbutton(self, text='Спектр', font=('Times New Roman', -FONT), bg='#C0C0C0',
#                    variable=self.graph_spectr_for_gain,
#                    offvalue=False,
#                    onvalue=True, command=self.animate).place(
#         x=10, y=10 * SHIFT)
#     tk.Checkbutton(self, text='Преобразованный спектр', font=('Times New Roman', -FONT), bg='#C0C0C0',
#                    variable=self.graph_spectr_after_gain,
#                    offvalue=False,
#                    onvalue=True, command=self.graph_spectr_after_gain_command).place(
#         x=10, y=11 * SHIFT)
#     tk.Checkbutton(self, text='Границы для алгоритма', font=('Times New Roman', -FONT), bg='#C0C0C0',
#                    variable=self.graph_borders, offvalue=False,
#                    onvalue=True, command=self.animate).place(x=10,
#                                                              y=12 * SHIFT)
#     tk.Checkbutton(self, text='Границы для счета', font=('Times New Roman', -FONT), bg='#C0C0C0',
#                    variable=self.graph_N_borders, offvalue=False,
#                    onvalue=True, command=self.animate).place(x=10,
#                                                              y=13 * SHIFT)
#     tk.Button(self, text='Вывести график', bg='#C0C0C0', font=('Times New Roman', -FONT),
#               command=self.CreateThreadChart).place(
#         x=242,
#         y=13 * SHIFT)