from common import *
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
def main_open_spec_(self):
    file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])

    if self.open_spectr_type.get() == OpenSpectrumType.SpFe.value:
        with open(file_path, 'r', encoding="utf-8") as file:
            lines = file.readlines()
            life_time = lines[0].split(": ")[-1]
            life_time = life_time.replace('\n', '')
            life_time = life_time.replace(',', '.')  # убираем также запятую
            life_time = str(round(float(life_time), 3))

            real_time = lines[1].split(": ")[-1]
            real_time = real_time.replace('\n', '')
            real_time = real_time.replace(',', '.')  # убираем также запятую
            real_time = str(round(float(real_time), 3))
        with open(file_path, 'r', encoding="utf-8") as file:
            spectr = pd.read_table(file, skiprows=[i for i in range(2)], header=None,
                                   names=['N'])
            spectr['energy'] = spectr.index

        return life_time, real_time, spectr
    elif self.open_spectr_type.get() == OpenSpectrumType.Spectrum.value:
        with open(file_path, 'r', encoding="utf-8") as file:
            lines = file.readlines()
            life_time = lines[22].split(": ")[-1]
            life_time = life_time.replace('\n', '')
            life_time = life_time.replace(',', '.')  # убираем также запятую
            life_time = str(round(float(life_time),3))

            real_time = lines[21].split(": ")[-1]
            real_time = real_time.replace('\n', '')
            real_time = real_time.replace(',', '.')  # убираем также запятую
            real_time = str(round(float(real_time),3))
        with open(file_path, 'r', encoding="utf-8") as file:
            spectr = pd.read_table(file, skiprows=[i for i in range(27)], header=None,
                                   names=['energy', 'N'], sep=' ')
        return life_time, real_time, spectr


    else: # self.open_spectr_type.get() == OpenSpectrumType.AlgoSpectrum.value
        with open(file_path, 'r', encoding="utf-8") as file:
            lines = file.readlines()
            life_time = lines[0].split(": ")[-1]
            life_time = life_time.replace('\n', '')
            life_time = life_time.replace(',', '.')  # убираем также запятую
            life_time = str(round(float(life_time), 3))

            real_time = lines[1].split(": ")[-1]
            real_time = real_time.replace('\n', '')
            real_time = real_time.replace(',', '.')  # убираем также запятую
            real_time = str(round(float(real_time), 3))
        with open(file_path, 'r', encoding="utf-8") as file:
            spectr = pd.read_table(file, skiprows=[i for i in range(2)], header=None,
                                   names=['energy', 'N'], sep=' ')
        return life_time, real_time, spectr


def main_save_spec_(self, spectr, life_time, real_time):
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(f'Живое время: {life_time}\n')
        file.write(f'Реальное время: {real_time}\n')
        for i, row in spectr.iterrows():
            file.write(f'{row["energy"]} {round(row["N"], 3)}\n')


def open_calibrate_spec_(self):
    try:
        life_time,\
        real_time,\
        spectr = self.main_open_spec()

        if spectr.isnull().sum().any():
            raise Exception
        spectr.astype({'energy': 'int32', 'N': 'float'})
    except Exception  as ex:
        print(ex)
        messagebox.showerror('Внимание: ', f"Не удалось открыть")
    else:
        self.sample_spectr_life_time.set(life_time)
        self.sample_spectr_real_time.set(real_time)
        self.sample_spectr = spectr

        self.sample_spectr_flag.set(True)


#TODO: Если меню открытия закрылось досрочно до не выводить ошибку

def open_spec_(self):
    try:
        life_time,\
        real_time,\
        spectr = self.main_open_spec()
        if spectr.isnull().sum().any():
            raise Exception
        spectr.astype({'energy': 'int32', 'N': 'float'})
    except Exception  as ex:
        print(ex)
        messagebox.showerror('Внимание: ', f"Не удалось открыть спектр")
    else:
        self.spectr_life_time.set(life_time)
        self.spectr_real_time.set(real_time)
        self.spectr = spectr


        self.spectr_flag.set(True)

def save_sample_spec_(self):
    if not self.sample_spectr_flag.get():
        messagebox.showerror('Внимание: ', f"Спектр не загружен")
        return
    try:
        self.main_save_spec(self.sample_spectr,
                            self.sample_spectr_life_time.get(),
                            self.sample_spectr_real_time.get()
                            )
    except Exception as ex:
        print(ex)
        messagebox.showerror('Внимание: ', f"Не удалось сохранить")

def save_spec_(self):
    if not self.spectr_flag.get():
        messagebox.showerror('Внимание: ', f"Спектр не загружен")
        return
    try:
        self.main_save_spec(self.spectr,
                            self.spectr_life_time.get(),
                            self.spectr_real_time.get()
                            )
    except Exception as ex:
        print(ex)
        messagebox.showerror('Внимание: ', f"Не удалось сохранить")



def save_processed_spec_(self):
    if not self.processed_spectr_flag.get():
        messagebox.showerror('Внимание: ', f"Спектр не загружен")
        return
    try:
        self.main_save_spec(self.processed_spectr,
                            self.processed_spectr_life_time.get(),
                            self.processed_spectr_real_time.get()
                            )
    except Exception as ex:
        print(ex)
        messagebox.showerror('Внимание: ', f"Не удалось сохранить")



def save_cleaned_spec_(self):
    if not self.cleaned_spectr_flag.get():
        messagebox.showerror('Внимание: ', f"Спектр не загружен")
        return
    try:
        self.main_save_spec(self.cleaned_spectr,
                            self.cleaned_spectr_life_time.get(),
                            self.cleaned_spectr_real_time.get()
                            )
    except Exception as ex:
        print(ex)
        messagebox.showerror('Внимание: ', f"Не удалось сохранить")
