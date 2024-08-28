import tkinter as tk
from tkinter import Menu
from tkinter import ttk
from common import *
def init_app_param_(self):
    self.title('AlgoSpectrum')  # название программы
    w_screen = self.winfo_screenwidth()
    h_screen = self.winfo_screenheight()
    self.width = 720
    self.height = 520

    self.x_coordinate = (w_screen - self.width ) // 2
    self.y_coordinate = (h_screen - self.height) // 2
    self.geometry(
        f'{self.width}x{self.height}+{self.x_coordinate}+{self.y_coordinate}')  # размер окна и сдвиги в пикселях от левого верхнего угла
    self.resizable(False, False)

    self.photo_path = r'.\config\energy.png'
    self.config_file_path =  r'.\config\config.json'
    photo = tk.PhotoImage(file=self.photo_path)  # выгружаем фото
    self.iconphoto(False, photo)  # устанавливаем фото
    self.config(bg='#C0C0C0')  # установили цвет фона

    self.font_type = 'Segoe UI'
    # self.combostyle = ttk.Style()
    # self.font_type = 'Segoe UI'
    # self.combostyle.theme_create('combostyle', parent='alt',
    #                         settings={'TCombobox':
    #                                       {'configure':
    #                                            {'selectbackground': '#C0C0C0',
    #                                             'fieldbackground': '#C0C0C0',
    #                                             'background': '#C0C0C0',
    #                                             'foreground': '#C0C0C0',
    #                                             'selectforeground':' black',
    #                                             'relief': 'flat',
    #                                             'font': (self.font_type, 30)  # Размер и шрифт текста
    #                                             }}}
    #                         )
    # self.combostyle.configure('TCombobox',
    #                             relief = 'flat')
    # self.combostyle.theme_use('combostyle')


def flash_setting_(self):
    if self.plot_flag.get():
        self.fig.close()
    self.init_common_var()
    self.init_spectrum_vars()
    self.init_setting_vars()
    self.init_plot_frame_vars()
    self.open_config()
    self.set_config()
    self.create_menu()
    self.create_common_static_widgets()
    self.create_common_combobox_widgets()
    self.create_spectrum_static_widgets()
    self.create_spectrum_combobox_widgets()
    self.create_plot_frame_widgets()
    self.create_metric_widgets()
    self.create_setting_widgets()
    self.set_window_mode(WindowMode.Spectrum.value)
    #+ сброс графика

def create_menu_(self):
    menu_bar = Menu(self)
    self.config(menu=menu_bar)
    '''______________________________________________________________________________________'''
    file_menu = Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="Файл", menu=file_menu)

    file_menu.add_command(label="Сбросить настройки", command=self.flash_setting)

    open_menu = tk.Menu(file_menu, tearoff=0)
    open_menu.add_command(label="Калибровочный спектр", command=self.open_calibrate_spec)
    open_menu.add_command(label="Спектр", command=self.open_spec)
    file_menu.add_cascade(label="Открыть", menu=open_menu)



    save_menu = tk.Menu(file_menu, tearoff=0)
    save_menu.add_command(label="Калибровочный", command=self.save_sample_spec)
    save_menu.add_command(label="Спектр", command=self.save_spec)
    save_menu.add_command(label="Преобразованный спектр", command=self.save_processed_spec)
    save_menu.add_command(label="Очищенный спектр", command=self.save_cleaned_spec)
    file_menu.add_cascade(label="Сохранить", menu=save_menu)

    '''______________________________________________________________________________________'''
    connection_menu = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="Коммуникация", menu=connection_menu)
    port_menu = tk.Menu(connection_menu, tearoff=0)
    connection_menu.add_cascade(label="Выбрать порт", menu=port_menu)
    port_menu.add_command(label=f'Порт {0}', command=lambda: self.set_port(0))
    port_menu.add_command(label=f'Порт {1}', command=lambda: self.set_port(1))
    port_menu.add_command(label=f'Порт {2}', command=lambda: self.set_port(2))
    port_menu.add_command(label=f'Порт {3}', command=lambda: self.set_port(3))
    port_menu.add_command(label=f'Порт {4}', command=lambda: self.set_port(4))
    port_menu.add_command(label=f'Порт {5}', command=lambda: self.set_port(5))
    port_menu.add_command(label=f'Порт {6}', command=lambda: self.set_port(6))
    port_menu.add_command(label=f'Порт {7}', command=lambda: self.set_port(7))
    port_menu.add_command(label=f'Порт {8}', command=lambda: self.set_port(8))
    port_menu.add_command(label=f'Порт {9}', command=lambda: self.set_port(9))
    port_menu.add_command(label=f'Порт {10}', command=lambda: self.set_port(10))
    port_menu.add_command(label=f'Порт {11}', command=lambda: self.set_port(11))

    connection_menu.add_command(label="Подключиться к порту", command=self.connect_to_port)
    connection_menu.add_command(label="Отключиться от порта", command=self.disconnect_from_port)
    '''Задать настройки с записью в конфиг и обновлением в главном меню'''
    connection_menu.add_command(label="Задать настройки связи", command=self.set_spectrometr_setting)

    connection_menu.add_command(label="Начать набор спектра", command=self.start_sampling)
    #
    connection_menu.add_command(label="Остановить набор спектра", command=self.stop_sampling)
    '''______________________________________________________________________________________'''

    '''______________________________________________________________________________________'''
    complement_menu = Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="Дополнительно", menu=complement_menu)

    complement_menu.add_command(label="Установить окна", command=self.set_analysis_window)

    complement_menu.add_command(label="Анализ окон", command=self.show_analysis_window_func)

    complement_menu.add_command(label="Домножить на число", command=self.multiply_to_number)
    '''______________________________________________________________________________________'''
    menu_bar.add_command(label="О программе", command=self.show_programm_info)


