from common import *
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from events import *

def ok_button_analysis_window_(self):
    try:
        self.show_analysis_window.destroy()
        self.show_analysis_window_func()
    except Exception:
        pass
    self.animate()
    self.analysis_window.destroy()

def set_analysis_window_(self):
    self.analysis_window = tk.Toplevel(self)
    self.analysis_window.title("Окно анализа")
    w = 300
    h = 204
    self.analysis_window.geometry(
        f'{w}x{h}+{self.x_coordinate}+{self.y_coordinate}')  # размер окна и сдвиги в пикселях от левого верхнего угла
    self.analysis_window.config(bg='#C0C0C0')  # установили цвет фона
    FONT = 16
    SHIFT = 50

    l_entry = tk.Entry(self.analysis_window, width=10, bg='#C0C0C0',
                                   font=(self.font_type, -FONT),
                                   textvariable=self.left_analysis_border,
                                   justify='center',
                                   ).place( x=20, y=50, height=18)

    r_entry = tk.Entry(self.analysis_window, width=10, bg='#C0C0C0',
                                   font=(self.font_type, -FONT),
                                   textvariable=self.right_analysis_border,
                                   justify='center',
                                   ).place( x=20+140, y=50, height=18)

    tk.Label(self.analysis_window, text='Левая граница:', anchor='w', bg='#C0C0C0', padx=0, pady=0,
             font=(self.font_type, -FONT)).place( x=20, y=20, height=18)

    tk.Label(self.analysis_window, text='Правая граница:', anchor='w', bg='#C0C0C0', padx=0, pady=0,
         font=(self.font_type, -FONT)).place( x=20+140, y=20, height=18)

    ok_button = tk.Button(self.analysis_window,
                                        text="Ок",
                                        command=self.ok_button_analysis_window,
                                        font=(self.font_type, 12),
                                        width=12,
                                        height=1,
                                        justify='center'
                                        )
    ok_button.place(x=20 + 140, y=20+SHIFT)


def show_analysis_window_func_(self):
    self.show_analysis_window = tk.Toplevel(self)
    self.show_analysis_window.title("Окно анализа")
    w = 450
    h = 300
    self.show_analysis_window.geometry(
        f'{w}x{h}+{self.x_coordinate}+{self.y_coordinate}')  # размер окна и сдвиги в пикселях от левого верхнего угла
    self.show_analysis_window.config(bg='#C0C0C0')  # установили цвет фона
    FONT = 16
    SHIFT = 50


    self.analysis_spectr_type = tk.StringVar(value=SpectrType.Sample.value)
    self.analysis_spectr_type_list = [SpectrType.Sample.value, SpectrType.Ordinary.value,
                                      SpectrType.Processed.value, SpectrType.Cleaned.value]



    self.combobox_analysis_spectr_type = ttk.Combobox(self.show_analysis_window,
                                                values=self.analysis_spectr_type_list,
                                                background='#C0C0C0',
                                                foreground='#C0C0C0',
                                                style='TCombobox',
                                                font=(self.font_type, 12),
                                                width=14,
                                                justify='center')
    self.combobox_analysis_spectr_type['state'] = 'readonly'
    self.combobox_analysis_spectr_type.bind("<<ComboboxSelected>>", self.analysis_spectr_type_changed)
    self.combobox_analysis_spectr_type.place(x=200, y=250)
    self.combobox_analysis_spectr_type.set(self.analysis_spectr_type.get())




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

    tk.Label(self.show_analysis_window, text=f"    Окно        ",font=(self.font_type, -FONT)).grid(row=0, column=0)
    tk.Label(self.show_analysis_window, text=f"Счёт, имп        ",font=(self.font_type, -FONT)).grid(row=0, column=1)
    tk.Label(self.show_analysis_window, text=f"Загрузка, имп/с        ",font=(self.font_type, -FONT)).grid(row=0, column=2)
    tk.Label(self.show_analysis_window, text=f"Ошибка, %    ",font=(self.font_type, -FONT)).grid(row=0, column=3)

    tk.Label(self.show_analysis_window,
             textvariable=self.show_border_tk,
                           font=(self.font_type, -FONT)).grid(row=1, column=0)
    tk.Label(self.show_analysis_window, textvariable=self.count_tk,font=(self.font_type, -FONT)).grid(row=1, column=1)
    tk.Label(self.show_analysis_window, textvariable=self.load_tk,font=(self.font_type, -FONT)).grid(row=1, column=2)
    tk.Label(self.show_analysis_window, textvariable=self.error_tk,font=(self.font_type, -FONT)).grid(row=1, column=3)

    # tk.Label(self.show_analysis_window, textvariable=f"021",font=(self.font_type, -FONT)).grid(row=1, column=1)





def multiply_to_number_(self):
    self.multiplier_spectr_window = tk.Toplevel(self)
    self.multiplier_spectr_window.title("Настройки спектрометра")
    w = 300
    h = 204
    self.multiplier_spectr_window.geometry(
        f'{w}x{h}+{self.x_coordinate}+{self.y_coordinate}')  # размер окна и сдвиги в пикселях от левого верхнего угла
    self.multiplier_spectr_window.config(bg='#C0C0C0')  # установили цвет фона
    FONT = 16
    SHIFT = 50

    self.used_spectr_type = tk.StringVar(value=SpectrType.Sample.value)
    self.used_spectr_type_list = [SpectrType.Sample.value, SpectrType.Ordinary.value]
    self.multiplied_number = tk.StringVar(value="1")


    self.combobox_used_spectr_type = ttk.Combobox(self.multiplier_spectr_window,
                                                values=self.used_spectr_type_list,
                                                background='#C0C0C0',
                                                foreground='#C0C0C0',
                                                style='TCombobox',
                                                font=(self.font_type, 12),
                                                width=14,
                                                justify='center')
    self.combobox_used_spectr_type['state'] = 'readonly'
    self.combobox_used_spectr_type.bind("<<ComboboxSelected>>", self.used_spectr_type_changed)
    self.combobox_used_spectr_type.place(x=20 + 65, y=20)
    self.combobox_used_spectr_type.set(self.used_spectr_type.get())

    multiplied_entry = tk.Entry(self.multiplier_spectr_window, width=10, bg='#C0C0C0',
                                   font=(self.font_type, -FONT),
                                   textvariable=self.multiplied_number,
                                   justify='center',
                                   ).place( x=20, y=20+SHIFT, height=18)

    life_time_button = tk.Button(self.multiplier_spectr_window,
                                        text="Живое время",
                                        command=self.set_multiply_life_time,
                                        font=(self.font_type, 12),
                                        width=12,
                                        height=1,
                                        justify='center'
                                        )
    life_time_button.place(x=20 + 140, y=10+SHIFT)


    multiplied_spectr_button = tk.Button(self.multiplier_spectr_window,
                                        text="Применить",
                                        command=self.multiply,
                                        font=(self.font_type, 12),
                                        width=12,
                                        height=1,
                                        justify='center'
                                        )
    multiplied_spectr_button.place(x=20 + 75, y=20+2*SHIFT)


def multiply_(self):
    try:
        if float(self.multiplied_number.get())<=0:
            messagebox.showerror('Внимание: ', f"Некорректное значение")
            return
        if self.used_spectr_type.get() == SpectrType.Sample.value:
            if self.sample_spectr_flag.get() == False:
                messagebox.showerror('Внимание: ', f"Отсутствует спектр")
                return
            else:
                self.sample_spectr.loc[:,'N'] = self.sample_spectr['N']*float(self.multiplied_number.get())
        else:
            if self.spectr_flag.get() == False:
                messagebox.showerror('Внимание: ', f"Отсутствует спектр")
                return
            else:
                self.spectr.loc[:,'N'] = self.spectr['N']*float(self.multiplied_number.get())
                if self.processed_spectr_flag.get():
                    self.processed_spectr.loc[:,'N'] = self.processed_spectr['N'] * float(self.multiplied_number.get())
                if self.cleaned_spectr_flag.get():
                    self.cleaned_spectr.loc[:,'N'] = self.cleaned_spectr['N'] * float(self.multiplied_number.get())
    except Exception:
        messagebox.showerror('Внимание: ', f"Ошибка")

    self.animate()
    self.multiplier_spectr_window.destroy()

def set_multiply_life_time_(self):
    if self.used_spectr_type.get() == SpectrType.Sample.value:
        if self.sample_spectr_flag.get():
            self.multiplied_number.set(round(1/(float(self.sample_spectr_life_time.get())),6))
    else:
        if self.spectr_flag.get():
            self.multiplied_number.set(round(1/(float(self.spectr_life_time.get())),6))


def show_programm_info_(self):
    about_text = "AlgoSpectrum\n\nВерсия: 2.0\n\nРазработана в АО \"НИИТФА\" в " \
        "рамках магистерской дипломной работы.\n\n" \
        "Программа предназначена для работы со спектрами нейтронного счетчика,"\
        " оснащена алгоритмами стабилизации и устранения гамма-составляющей.\n\n"\
        "По вопросам о работе программы обращаться в НПО 59."
    messagebox.showinfo("О программе", about_text)
