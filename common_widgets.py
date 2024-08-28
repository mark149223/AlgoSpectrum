import tkinter as tk
from common import *
from tkinter import ttk
def create_common_static_widgets_(self):
    FONT = 16
    SHIFT = 30
    tk.Label(self, text='Режим окна:', anchor='w', bg='#C0C0C0', padx=0, pady=0,
             font=(self.font_type, -FONT)).place(x=self.width/2 - 100, y=SHIFT)


def create_common_combobox_widgets_(self):
    FONT = 16
    SHIFT = 30
    combobox_window_mode_list = [WindowMode.Spectrum.value,  WindowMode.Setting.value, WindowMode.Plot.value]


    self.combobox_window_mode = ttk.Combobox(self,
                                             values=combobox_window_mode_list,
                                             style='TCombobox',
                                             background='#C0C0C0',
                                             foreground='#C0C0C0',
                                             font=(self.font_type, 12),
                                             width=13,
                                             justify='center')
    # self.combobox_window_mode = ttk.Combobox(self.setting_frame, values=combobox_window_mode_list)
    # self.combobox_window_mode = ttk.Combobox(self.plot_frame, values=combobox_window_mode_list)
    # Устанавливаем цвет фона
    self.combobox_window_mode.set(combobox_window_mode_list[0])
    self.combobox_window_mode['state'] = 'readonly'
    self.combobox_window_mode.bind("<<ComboboxSelected>>", self.window_mode_changed)
    self.combobox_window_mode.place(x=self.width/2, y=SHIFT)