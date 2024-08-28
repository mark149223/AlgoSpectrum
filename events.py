from common import *
def window_mode_changed_(self, event):
    self.window_mode = self.combobox_window_mode.get()
    self.set_window_mode(self.window_mode)
    # print(self.window_mode)


def getting_spectr_type_changed_(self, event):
    self.sampling_spectr_type.set(self.combobox_getting_spectr_type.get())
    # print(self.getting_spectr_type)

def transfer_speed_changed_(self, event):
    self.transfer_speed.set(self.combobox_transfer_speed.get())
    # print(self.transfer_speed)

def number_of_channels_changed_(self, event):
    self.number_of_channels.set(self.combobox_number_of_channels.get())
    # print(self.number_of_channels)

def open_spectr_type_changed_(self,event):
    self.open_spectr_type.set(self.combobox_open_spectr_type.get())
    print(self.open_spectr_type.get())

def transfer_speed_set_changed_(self, event):
    self.transfer_speed_set.set(self.combobox_transfer_speed_set.get())
    print(self.transfer_speed_set.get())
    # print(self.transfer_speed)

def stabilization_algo_type_changed_(self, event):
    self.stabilization_algo_type.set(self.combobox_stabilization_algo_type.get())
    print(self.stabilization_algo_type.get())

def number_of_channels_set_changed_(self, event):
    self.number_of_channels_set.set(self.combobox_number_of_channels_set.get())
    print(self.number_of_channels_set.get())
    # print(self.number_of_channels)

def used_spectr_type_changed_(self, event):
    self.used_spectr_type.set(self.combobox_used_spectr_type.get())

def metric_spectr_type_changed_(self, event):
    self.metric_spectr_type.set(self.combobox_metric_spectr_type.get())
    SHIFT = 30
    self.sample_spectr_metric_frame.config(bg='#C0C0C0')  # установили цвет фона
    self.spectr_metric_frame.config(bg='#C0C0C0')  # установили цвет фона
    self.processed_spectr_metric_frame.config(bg='#C0C0C0')  # установили цвет фона
    self.cleaned_spectr_metric_frame.config(bg='#C0C0C0')  # установили цвет фона

    if self.metric_spectr_type.get() == SpectrType.Sample.value:

        self.spectr_metric_frame.place_forget()
        self.processed_spectr_metric_frame.place_forget()
        self.cleaned_spectr_metric_frame.place_forget()

        self.sample_spectr_metric_frame.place(x=0, y=7 * SHIFT, width=self.width, height=3 * SHIFT)

    elif self.metric_spectr_type.get() == SpectrType.Ordinary.value:

        self.sample_spectr_metric_frame.place_forget()
        self.processed_spectr_metric_frame.place_forget()
        self.cleaned_spectr_metric_frame.place_forget()

        self.spectr_metric_frame.place(x=0, y=7 * SHIFT, width=self.width, height=3 * SHIFT)

    elif self.metric_spectr_type.get() == SpectrType.Processed.value:
        self.sample_spectr_metric_frame.place_forget()
        self.spectr_metric_frame.place_forget()
        self.cleaned_spectr_metric_frame.place_forget()

        self.processed_spectr_metric_frame.place(x=0, y=7 * SHIFT, width=self.width, height=3 * SHIFT)

    else:
        self.sample_spectr_metric_frame.place_forget()
        self.processed_spectr_metric_frame.place_forget()
        self.spectr_metric_frame.place_forget()

        self.cleaned_spectr_metric_frame.place(x=0, y=7 * SHIFT, width=self.width, height=3 * SHIFT)




    # self.combobox_metric_spectr_type.selection_clear()
    print(self.metric_spectr_type.get())

def plot_closed_(self, event):
    self.plot_flag.set(False)
    print("График закрыт. Выполняю дополнительное действие.")

def key_on_plot_pressed_(self, event):
    xl, xr = self.ax.get_xlim()
    yd, yu = self.ax.get_ylim()

    # Первые чтобы обеспечить 0 после автомасштабирования
    if event.key == 'up':
        yu += 1
        yu *= (1 - 0.2)

        self.UScaleY.set(yu)

        self.animate()
    if event.key == 'down':
        yu += 1
        yu *= (1 + 0.2)
        self.UScaleY.set(yu)
        self.animate()
    if event.key == 'left':
        xr += 1
        xr *= (1 + 0.2)
        self.RScaleX.set(xr)
        self.animate()

    if event.key == 'right':
        xr += 1
        xr *= (1 - 0.2)
        self.RScaleX.set(xr)
        self.animate()

def analysis_spectr_type_changed_(self,event):
    self.analysis_spectr_type.set(self.combobox_analysis_spectr_type.get())



    self.count = 0
    self.load = 0
    self.error = 0
    if self.combobox_analysis_spectr_type.get() == SpectrType.Sample.value:
        spectr = self.sample_spectr
    elif self.combobox_analysis_spectr_type.get() == SpectrType.Ordinary.value:
        spectr = self.spectr
    elif self.combobox_analysis_spectr_type.get() == SpectrType.Processed.value:
        spectr = self.processed_spectr
    elif self.combobox_analysis_spectr_type.get() == SpectrType.Cleaned.value:
        spectr = self.cleaned_spectr


    try:
        g = 0
        for i in spectr['N']:
            if g>=self.left_analysis_border.get() and g<=self.right_analysis_border.get():
                self.count+= i
            g+=1
        if self.combobox_analysis_spectr_type.get() == SpectrType.Sample.value:
            self.load = self.count/float(self.sample_spectr_life_time.get())
        elif self.combobox_analysis_spectr_type.get() == SpectrType.Ordinary.value:
            self.load = self.count/float(self.spectr_life_time.get())
        elif self.combobox_analysis_spectr_type.get() == SpectrType.Processed.value:
            self.load = self.count/float(self.processed_spectr_life_time.get())
        elif self.combobox_analysis_spectr_type.get() == SpectrType.Cleaned.value:
            self.load = self.count/float(self.cleaned_spectr_life_time.get())
        try:
            self.error = 100/(self.count**(1/2))
        except Exception:
            self.error = 0

    except Exception as ex:
        self.count = 0
        self.load = 0
        self.error = 0

        self.count_tk.set('-')
        self.load_tk.set('-')
        self.error_tk.set('-')
        self.show_border_tk.set('-')
        print(ex)

    else:
        self.show_border_tk.set(f'{self.left_analysis_border.get()}-{self.right_analysis_border.get()}')
        self.count_tk.set(str(self.count))
        self.load_tk.set(str(round(self.load,2)))
        self.error_tk.set(str(round(self.error,2)))

def update_sampling_time_(self, *args):

    try:
        # Пробуем преобразовать значение из Entry в тип float
        var = round(float(self.sampling_time_tk.get()),3)
        if var <= 0:
            raise ValueError
    except ValueError:
        # Если введено некорректное значение, оставляем текущее значение
        pass
    else:
        self.sampling_time = var
    # print(self.sampling_time)


