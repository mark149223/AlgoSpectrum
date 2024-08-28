import tkinter as tk
from tkinter import messagebox
from tkinter import TclError
from tkinter import filedialog
from common import *


class AlgoSpectrumApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.init_app_param()
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


    def init_setting_vars(self):
        pass

    def calculate_border(self):
        pass
    def calculate_processed_spectr(self):
        pass
    def calculate_cleaned_spectr(self):
        pass
    def calculate_metrics(self):
        pass

    def plot_closed(self, event):
        pass

    def key_on_plot_pressed(self, event):
        pass

    def show_plot(self):
        pass

    def init_common_var(self):
        pass
    def init_app_param(self):
        pass
    def create_menu(self):
        pass
    def flash_setting(self):
        pass
    def init_spectr_variable(self):
        pass
    def create_spectrum_static_widgets(self):
        pass
    def create_spectrum_combobox_widgets(self):
        pass

    def create_common_static_widgets(self):
        pass

    def create_common_combobox_widgets(self):
        pass
    def set_window_mode(self, mode):
        pass
    def window_mode_changed(self, event):
        pass
    def getting_spectr_type_changed(self, event):
        pass
    def transfer_speed_changed(self, event):
        pass
    def number_of_channels_changed(self, event):
        pass

    def transfer_speed_set_changed(self, event):
        pass
    def number_of_channels_set_changed(self, event):
        pass

    def open_spectr_type_changed(self, event):
        pass

    def stabilization_algo_type_changed(self, event):
        pass

    def metric_spectr_type_changed(self, event):
        pass

    def create_metric_widgets(self):
        pass

    def init_plot_frame_vars(self):
        pass

    def create_plot_frame_widgets(self):
        pass

    def create_setting_widgets(self):
        pass

    def animate(self):
        pass

    def create_plot(self):
        pass

    def update_sampling_time(self,*args):
        pass

    def ok_button_analysis_window(self):
        pass


    def monitor(self, sampling_process):
        pass
    def stop_sampling(self):
        pass

    def set_spectrometr_setting(self):
        pass
    def send_spectrometr_setting(self):
        pass


    def set_port(self, port):
        pass

    def connect_to_port(self):
        pass
    def disconnect_from_port(self):
        pass

    def open_config(self):
        pass

    def set_config(self):
        pass

    def write_config(self):
        pass


    def init_spectrum_vars(self):
        pass

    def main_open_spec(self):
        pass
    def main_save_spec(self, spectr):
        pass
    def open_calibrate_spec(self):
        pass
    def open_spec(self):
        pass
    def save_sample_spec(self):
        pass
    def save_spec(self):
        pass
    def save_processed_spec(self):
        pass
    def save_cleaned_spec(self):
        pass


    def set_analysis_window(self):
        pass

    def show_analysis_window_func(self):
        pass

    def multiply_to_number(self):
        pass

    def multiply(self):
        pass

    def set_multiply_life_time(self):
        pass

    def used_spectr_type_changed(self, event):
        pass

    def analysis_spectr_type_changed(self,event):
        pass

    def show_programm_info(self):
        pass