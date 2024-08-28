from common import *
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def init_plot_frame_vars_(self):
    SHIFT = 30

    self.metric_spectr_type = tk.StringVar(value=SpectrType.Sample.value)
    self.metric_spectr_type_list = [i.value for i in SpectrType]

    self.sample_show_flag = tk.BooleanVar(value=False)
    self.spectr_show_flag = tk.BooleanVar(value=False)
    self.processed_spectr_show_flag = tk.BooleanVar(value=False)
    self.cleaned_spectr_show_flag = tk.BooleanVar(value=False)

    self.borders_show_flag = tk.BooleanVar(value=False)
    self.gamma_show_flag = tk.BooleanVar(value=False)
    self.gamma_approx_show_flag = tk.BooleanVar(value=False)
    self.analysis_window_show_flag = tk.BooleanVar(value=False)

    self.plot_flag = tk.BooleanVar(value=False)

    self.LScaleX = tk.IntVar(value=0)
    self.RScaleX = tk.IntVar(value=0)
    self.DScaleY = tk.IntVar(value=0)
    self.UScaleY = tk.IntVar(value=0)

    self.sample_spectr_metric_frame = tk.Frame(self.plot_frame)
    self.spectr_metric_frame = tk.Frame(self.plot_frame)
    self.processed_spectr_metric_frame = tk.Frame(self.plot_frame)
    self.cleaned_spectr_metric_frame = tk.Frame(self.plot_frame)

    self.sample_spectr_metric_frame.config(bg='#C0C0C0')  # установили цвет фона
    self.spectr_metric_frame.config(bg='#C0C0C0')  # установили цвет фона
    self.processed_spectr_metric_frame.config(bg='#C0C0C0')  # установили цвет фона
    self.cleaned_spectr_metric_frame.config(bg='#C0C0C0')  # установили цвет фона

    self.sample_spectr_metric_frame.place(x=0, y=7*SHIFT, width=self.width, height=3*SHIFT)

    self.sample_spectr_N_in_border = tk.StringVar(value='-')
    self.sample_spectr_error_N_in_border = tk.StringVar(value='-')
    self.sample_spectr_relative_s = tk.StringVar(value='-')
    self.sample_spectr_error_relative_s = tk.StringVar(value='-')

    self.spectr_N_in_border = tk.StringVar(value='-')
    self.spectr_error_N_in_border = tk.StringVar(value='-')
    self.spectr_relative_s = tk.StringVar(value='-')
    self.spectr_error_relative_s = tk.StringVar(value='-')

    self.processed_spectr_N_in_border = tk.StringVar(value='-')
    self.processed_spectr_error_N_in_border = tk.StringVar(value='-')
    self.processed_spectr_relative_s = tk.StringVar(value='-')
    self.processed_spectr_error_relative_s = tk.StringVar(value='-')

    self.cleaned_spectr_N_in_border = tk.StringVar(value='-')
    self.cleaned_spectr_error_N_in_border = tk.StringVar(value='-')
    self.cleaned_spectr_relative_s = tk.StringVar(value='-')
    self.cleaned_spectr_error_relative_s = tk.StringVar(value='-')

    self.metric_mass = [[self.sample_spectr_metric_frame,
                         self.sample_spectr_N_in_border,
                         self.sample_spectr_error_N_in_border,
                         self.sample_spectr_relative_s,
                         self.sample_spectr_error_relative_s,
                         self.sample_spectr_life_time,
                         self.sample_spectr_real_time,
                         self.sample_spectr_flag ],

                        [self.spectr_metric_frame,
                         self.spectr_N_in_border,
                         self.spectr_error_N_in_border,
                         self.spectr_relative_s,
                         self.spectr_error_relative_s,
                         self.spectr_life_time,
                         self.spectr_real_time,
                         self.spectr_flag

                        ],
                        [self.processed_spectr_metric_frame,
                         self.processed_spectr_N_in_border,
                         self.processed_spectr_error_N_in_border,
                         self.processed_spectr_relative_s,
                         self.processed_spectr_error_relative_s,
                         self.processed_spectr_life_time,
                         self.processed_spectr_real_time,
                         self.processed_spectr_flag

                         ],
                        [self.cleaned_spectr_metric_frame,
                         self.cleaned_spectr_N_in_border,
                         self.cleaned_spectr_error_N_in_border,
                         self.cleaned_spectr_relative_s,
                         self.cleaned_spectr_error_relative_s,
                         self.cleaned_spectr_life_time,
                         self.cleaned_spectr_real_time,
                         self.cleaned_spectr_flag

                         ]
                        ]



def create_metric_widgets_(self):
    FONT = 16
    SHIFT = 30

    for spectr in self.metric_mass:

        tk.Label(spectr[0], text='Живое время, с:', anchor='w', bg='#C0C0C0', padx=0, pady=0,
                 font=(self.font_type, -FONT)).place(x=20, y= 0*SHIFT)
        tk.Label(spectr[0], text='Реальное время, с:', anchor='w', bg='#C0C0C0', padx=0, pady=0,
                 font=(self.font_type, -FONT)).place(x=self.width/2, y=0 * SHIFT)
        tk.Label(spectr[0], text='Отношение площадей:', anchor='w', bg='#C0C0C0', padx=0, pady=0,
                 font=(self.font_type, -FONT)).place(x=20, y= 1*SHIFT)
        tk.Label(spectr[0], text='Относительная ошибка, %:', anchor='w', bg='#C0C0C0', padx=0, pady=0,
                 font=(self.font_type, -FONT)).place(x=20, y= 2*SHIFT)

        tk.Label(spectr[0], text='Счёт в окне:', anchor='w', bg='#C0C0C0', padx=0, pady=0,
                 font=(self.font_type, -FONT)).place(x=self.width/2, y=1 * SHIFT)
        tk.Label(spectr[0], text='Относительная ошибка, %:', anchor='w', bg='#C0C0C0', padx=0, pady=0,
                 font=(self.font_type, -FONT)).place(x=self.width/2, y=2 * SHIFT)

        tk.Label(spectr[0],textvariable=spectr[5], anchor='w',bg='#C0C0C0', padx=0, pady=0,
                 font=(self.font_type, -FONT)).place(x=20 + 120, y=0 * SHIFT)
        tk.Label(spectr[0], textvariable=spectr[6], anchor='w', bg='#C0C0C0', padx=0, pady=0,
                 font=(self.font_type, -FONT)).place(x=self.width / 2 + 140, y=0 * SHIFT)
        tk.Label(spectr[0], textvariable=spectr[3], anchor='w', bg='#C0C0C0', padx=0, pady=0,
                 font=(self.font_type, -FONT)).place(x=20 + 176, y=1 * SHIFT)
        tk.Label(spectr[0], textvariable=spectr[4], anchor='w', bg='#C0C0C0', padx=0, pady=0,
                 font=(self.font_type, -FONT)).place(x=20 + 200, y=2 * SHIFT)

        tk.Label(spectr[0], textvariable=spectr[1], anchor='w', bg='#C0C0C0', padx=0, pady=0,
                 font=(self.font_type, -FONT)).place(x=self.width / 2 + 100, y=1 * SHIFT)
        tk.Label(spectr[0], textvariable=spectr[2], anchor='w', bg='#C0C0C0', padx=0, pady=0,
                 font=(self.font_type, -FONT)).place(x=self.width / 2 + 200, y=2 * SHIFT)


def create_plot_frame_widgets_(self):
    FONT = 16
    SHIFT = 30
    tk.Label(self.plot_frame, text='Метрики алгоритмов:', anchor='w', bg='#C0C0C0', padx=0, pady=0,
             font=(self.font_type, -FONT)).place(x=self.width / 2 - 100, y=2*SHIFT)

    tk.Label(self.plot_frame, text='Левая граница:', anchor='w', bg='#C0C0C0', padx=0, pady=0,
             font=(self.font_type, -FONT)).place(x=20, y=3*SHIFT)
    tk.Label(self.plot_frame, text='Правая граница:', anchor='w', bg='#C0C0C0', padx=0, pady=0,
             font=(self.font_type, -FONT)).place(x=20 + 400, y=3*SHIFT)
    tk.Label(self.plot_frame, textvariable=self.left_border, anchor='w', bg='#C0C0C0', padx=0, pady=0,
             font=(self.font_type, -FONT)).place(x=20+120, y=3*SHIFT)
    tk.Label(self.plot_frame, textvariable=self.right_border, anchor='w', bg='#C0C0C0', padx=0, pady=0,
             font=(self.font_type, -FONT)).place(x=20 + 535, y=3*SHIFT)

    tk.Label(self.plot_frame, text='a:', anchor='w', bg='#C0C0C0', padx=0, pady=0,
             font=(self.font_type, -FONT)).place(x=100, y=4 * SHIFT)
    tk.Label(self.plot_frame, text='k:', anchor='w', bg='#C0C0C0', padx=0, pady=0,
             font=(self.font_type, -FONT)).place(x=332, y=4 * SHIFT)
    tk.Label(self.plot_frame, text='u:', anchor='w', bg='#C0C0C0', padx=0, pady=0,
             font=(self.font_type, -FONT)).place(x=530, y=4 * SHIFT)

    tk.Label(self.plot_frame, textvariable=self.approx_equation_a, anchor='w', bg='#C0C0C0', padx=0, pady=0,
             font=(self.font_type, -FONT)).place(x=100+20, y=4 * SHIFT)
    tk.Label(self.plot_frame, textvariable=self.approx_equation_k, anchor='w', bg='#C0C0C0', padx=0, pady=0,
             font=(self.font_type, -FONT)).place(x=332+20, y=4 * SHIFT)
    tk.Label(self.plot_frame, textvariable=self.approx_equation_u, anchor='w', bg='#C0C0C0', padx=0, pady=0,
             font=(self.font_type, -FONT)).place(x=530+20, y=4 * SHIFT)

    tk.Frame(self.plot_frame, bg='black', height=1, width=self.width).place(x=0, y=5 * SHIFT + 15)
    tk.Label(self.plot_frame, text='Спектр для метрик:',
             anchor='w', bg='#C0C0C0', padx=0, pady=0,
             font=(self.font_type, -FONT)).place(x=self.width / 2 - 150, y=6 * SHIFT)

    self.combobox_metric_spectr_type = ttk.Combobox(self.plot_frame,
                                                values=self.metric_spectr_type_list,
                                                background='#C0C0C0',
                                                foreground='#C0C0C0',

                                                style='TCombobox',
                                                font=(self.font_type, 12),
                                                width=16,
                                                justify='center')
    self.combobox_metric_spectr_type['state'] = 'readonly'
    self.combobox_metric_spectr_type.bind("<<ComboboxSelected>>", self.metric_spectr_type_changed)
    self.combobox_metric_spectr_type.place(x=self.width / 2, y=6 * SHIFT)
    self.combobox_metric_spectr_type.set(self.metric_spectr_type.get())







    tk.Frame(self.plot_frame, bg='black', height=1, width=self.width).place(x=0, y=10 * SHIFT + 15)

    tk.Checkbutton(self.plot_frame, text='Калибровочный спектр', bg='#C0C0C0',padx=0, pady=0,
             font=(self.font_type, -FONT),
                   variable=self.sample_show_flag,
                   offvalue=False,
                   onvalue=True, command=self.animate).place(
        x=20, y=11*SHIFT)
    tk.Checkbutton(self.plot_frame, text='Спектр', bg='#C0C0C0',padx=0, pady=0,
             font=(self.font_type, -FONT),
                   variable=self.spectr_show_flag,
                   offvalue=False,
                   onvalue=True, command=self.animate).place(
        x=20, y=12*SHIFT)
    tk.Checkbutton(self.plot_frame, text='Преобразованный спектр', bg='#C0C0C0',padx=0, pady=0,
             font=(self.font_type, -FONT),
                   variable=self.processed_spectr_show_flag, offvalue=False,
                   onvalue=True, command=self.animate).place(x=20,
                                                             y=13*SHIFT)
    tk.Checkbutton(self.plot_frame, text='Очищенный спектр', bg='#C0C0C0',padx=0, pady=0,
             font=(self.font_type, -FONT),
                   variable=self.cleaned_spectr_show_flag, offvalue=False,
                   onvalue=True, command=self.animate).place(x=20,
                                                             y=14*SHIFT)



    tk.Checkbutton(self.plot_frame, text='Границы', bg='#C0C0C0',padx=0, pady=0,
             font=(self.font_type, -FONT),
                   variable=self.borders_show_flag,
                   offvalue=False,
                   onvalue=True, command=self.animate).place(
        x=240+20, y=11*SHIFT)
    tk.Checkbutton(self.plot_frame, text='Детектированная гамма', bg='#C0C0C0',padx=0, pady=0,
             font=(self.font_type, -FONT),
                   variable=self.gamma_show_flag,
                   offvalue=False,
                   onvalue=True, command=self.animate).place(
        x=240+20, y=12*SHIFT)
    tk.Checkbutton(self.plot_frame, text='Аппроксимированная гамма', bg='#C0C0C0',padx=0, pady=0,
             font=(self.font_type, -FONT),
                   variable=self.gamma_approx_show_flag, offvalue=False,
                   onvalue=True, command=self.animate).place(x=240+20,
                                                             y=13*SHIFT)
    tk.Checkbutton(self.plot_frame, text='Анализ окон', bg='#C0C0C0',padx=0, pady=0,
             font=(self.font_type, -FONT),
                   variable=self.analysis_window_show_flag, offvalue=False,
                   onvalue=True, command=self.animate).place(x=240+20,
                                                             y=14*SHIFT)

    show_plot_button = tk.Button(self.plot_frame,
                                        text="Монитор",
                                        command=self.create_plot,
                                        font=(self.font_type, 12),


                                        width=12,
                                        height=1,
                                        justify='center'
                                        )
    show_plot_button.place(
        x=self.width/2-50,
        y=15*SHIFT)




def animate_(self):
    if self.plot_flag.get():
        self.ax.clear()
        self.ax.set_xlim(self.LScaleX.get(), self.RScaleX.get())
        self.ax.set_ylim(self.DScaleY.get(), self.UScaleY.get())
        self.show_plot()

        # self.canvas.draw()
        self.fig.canvas.draw()
        # print('work')

def create_plot_(self):
    if self.plot_flag.get():
        return
    self.fig = plt.figure(2, figsize=(12, 8), dpi=280)
    self.ax = self.fig.add_subplot(111)
    self.fig.canvas.mpl_connect('key_press_event', self.key_on_plot_pressed)
    self.fig.canvas.mpl_connect('close_event', self.plot_closed)


    # self.canvas = FigureCanvasTkAgg(self.fig, master=self.plot_frame)
    # self.canvas_widget = self.canvas.get_tk_widget()
    # self.canvas.mpl_connect('key_press_event', self.key_on_plot_pressed)
    # self.canvas.mpl_connect('close_event', self.plot_closed)
    # # Размещаем график с помощью метода place
    # self.canvas_widget.place(x=50, y=50, width=400, height=300)

    self.plot_flag.set(True)
    plt.autoscale(True)
    self.show_plot()
    plt.show(block=False)

    xl, xr = self.ax.get_xlim()
    yd, yu = self.ax.get_ylim()

    # Первичная установка границ
    plt.autoscale(False)



    self.LScaleX.set(0)
    self.RScaleX.set(self.number_of_channels.get())
    self.DScaleY.set(0)
    self.UScaleY.set(yu+1)

    self.ax.set_xlim(self.LScaleX.get(), self.RScaleX.get())
    self.ax.set_ylim(self.DScaleY.get(), self.UScaleY.get())





def show_plot_(self):


    if self.sample_spectr_flag.get() and self.sample_show_flag.get():
        sample_plt = self.ax.plot(self.sample_spectr['energy'], self.sample_spectr['N'],
                                  color='green', label='Калибровочный спектр')



    if self.spectr_flag.get() and self.spectr_show_flag.get():
        spectr_plt = self.ax.plot(self.spectr['energy'], self.spectr['N'], color='orange', label='Спектр')
        # print(self.spectr)
    if self.processed_spectr_flag.get() and self.processed_spectr_show_flag.get():
        processed_plt = self.ax.plot(self.processed_spectr['energy'], self.processed_spectr['N'], color='blue',
                                     label='Преобразованный спектр')
    if self.cleaned_spectr_flag.get():
        if self.cleaned_spectr_show_flag.get():
            cleaned_plt = self.ax.plot(self.cleaned_spectr['energy'], self.cleaned_spectr['N'], color='pink',
                                       label='Очищенный спектр')
        if self.gamma_show_flag.get():
            gamma_plt = self.ax.plot(self.gamma_spectr['energy'], self.gamma_spectr['N'], color='red',
                                       label='Детектируемая гамма')
        if self.gamma_approx_show_flag.get():
            gamma_approx_plt = self.ax.plot(self.gamma_approx_spectr['energy'], self.gamma_approx_spectr['N'], color='purple',
                                     label='Аппроксимированная гамма')
    if self.borders.get() and self.borders_show_flag.get():
        border_l_plt = self.ax.plot([self.left_border.get(), self.left_border.get()],
                                    [0, self.sample_spectr['N'].max()], color='black')
        border_r_plt = self.ax.plot([self.right_border.get(), self.right_border.get()],
                                    [0 , self.sample_spectr['N'].max()], color='black')

    if self.analysis_window_show_flag.get() and self.sample_spectr_flag.get():
        border_l_plt = self.ax.plot([self.left_analysis_border.get(), self.left_analysis_border.get()],
                                    [0, self.sample_spectr['N'].max()], color='brown')
        border_r_plt = self.ax.plot([self.right_analysis_border.get(), self.right_analysis_border.get()],
                                    [0 , self.sample_spectr['N'].max()], color='brown')
    if self.sampling_spectr_type.get() == SamplingSpectrType.Ordinary.value:
        real_time = self.spectr_real_time.get()
        life_time = self.spectr_life_time.get()
        type = SamplingSpectrType.Ordinary.value
    else:
        real_time = self.sample_spectr_real_time.get()
        life_time = self.sample_spectr_life_time.get()
        type = SamplingSpectrType.Sample.value

    plt.annotate(f'Real Time: {real_time}', xy=(0,1.02), xycoords='axes fraction',fontsize=6)
    plt.annotate(f'Life Time: {life_time}', xy=(0.5,1.02), xycoords='axes fraction',fontsize=6)
    # plt.annotate(f'Spectr: {type}', xy=(0.7,1.02), xycoords='axes fraction',fontsize=6)
        # color = ['black', 'gray', 'brown', 'blue']
        # for window in range(4):
        #     plt35 = plt.plot([self.LeftBorderN[window], self.LeftBorderN[window]],
        #                      [0, self.spectr_for_gain['N'].max() + 50], color=color[window])
        #     plt36 = plt.plot([self.RightBorderN[window], self.RightBorderN[window]],
        #                      [0, self.spectr_for_gain['N'].max() + 50], color=color[window])

    handles, labels = self.ax.get_legend_handles_labels()
    # if handles and labels:
    #     self.ax.legend(loc='upper right')
    plt.yticks(fontsize=6,)
    plt.xticks(fontsize=6,)
    self.ax.grid()