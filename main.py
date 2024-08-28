from main_tk import *
from init_tk_app import *
from rw_action import *
from spectrum_widgets import *
from spectrum_logic import *
from common_widgets import *
from common import *
from events import *
from algo_setting import *
from plot_logic import *
from added_func import *

'''installing

 pyinstaller -w -F -i config\energy.png main.py   
'''

def Init():
    AlgoSpectrumApp.init_app_param = init_app_param_
    AlgoSpectrumApp.create_menu = create_menu_
    AlgoSpectrumApp.flash_setting = flash_setting_
    AlgoSpectrumApp.create_spectrum_static_widgets = create_spectrum_static_widgets_
    AlgoSpectrumApp.create_common_static_widgets = create_common_static_widgets_
    AlgoSpectrumApp.init_common_var = init_common_var_

    AlgoSpectrumApp.create_common_combobox_widgets = create_common_combobox_widgets_
    AlgoSpectrumApp.create_spectrum_combobox_widgets = create_spectrum_combobox_widgets_
    AlgoSpectrumApp.set_window_mode = set_window_mode_
    AlgoSpectrumApp.window_mode_changed = window_mode_changed_
    AlgoSpectrumApp.getting_spectr_type_changed = getting_spectr_type_changed_
    AlgoSpectrumApp.init_spectrum_vars = init_spectrum_vars_
    AlgoSpectrumApp.transfer_speed_changed = transfer_speed_changed_
    AlgoSpectrumApp.number_of_channels_changed = number_of_channels_changed_

    AlgoSpectrumApp.transfer_speed_set_changed = transfer_speed_set_changed_
    AlgoSpectrumApp.number_of_channels_set_changed = number_of_channels_set_changed_

    AlgoSpectrumApp.update_sampling_time = update_sampling_time_

    AlgoSpectrumApp.start_sampling = start_sampling_
    AlgoSpectrumApp.set_port = set_port_
    AlgoSpectrumApp.connect_to_port = connect_to_port_
    AlgoSpectrumApp.disconnect_from_port = disconnect_from_port_
    AlgoSpectrumApp.open_config = open_config_
    AlgoSpectrumApp.set_config = set_config_
    AlgoSpectrumApp.write_config = write_config_

    AlgoSpectrumApp.open_spectr_type_changed = open_spectr_type_changed_

    AlgoSpectrumApp.set_spectrometr_setting = set_spectrometr_setting_
    AlgoSpectrumApp.send_spectrometr_setting = send_spectrometr_setting_

    AlgoSpectrumApp.monitor = monitor_
    AlgoSpectrumApp.stop_sampling = stop_sampling_

    AlgoSpectrumApp.main_save_spec = main_save_spec_
    AlgoSpectrumApp.main_open_spec = main_open_spec_
    AlgoSpectrumApp.open_calibrate_spec = open_calibrate_spec_
    AlgoSpectrumApp.open_spec = open_spec_
    AlgoSpectrumApp.save_sample_spec = save_sample_spec_
    AlgoSpectrumApp.save_spec = save_spec_
    AlgoSpectrumApp.save_processed_spec = save_processed_spec_
    AlgoSpectrumApp.save_cleaned_spec = save_cleaned_spec_


    AlgoSpectrumApp.create_setting_widgets = create_setting_widgets_
    AlgoSpectrumApp.init_setting_vars = init_setting_vars_

    AlgoSpectrumApp.calculate_border = calculate_border_
    AlgoSpectrumApp.calculate_processed_spectr = calculate_processed_spectr_
    AlgoSpectrumApp.calculate_cleaned_spectr = calculate_cleaned_spectr_
    AlgoSpectrumApp.calculate_metrics = calculate_metrics_

    AlgoSpectrumApp.stabilization_algo_type_changed = stabilization_algo_type_changed_

    AlgoSpectrumApp.init_plot_frame_vars = init_plot_frame_vars_
    AlgoSpectrumApp.create_plot_frame_widgets = create_plot_frame_widgets_

    AlgoSpectrumApp.metric_spectr_type_changed = metric_spectr_type_changed_
    AlgoSpectrumApp.animate = animate_
    AlgoSpectrumApp.create_plot = create_plot_
    AlgoSpectrumApp.plot_closed = plot_closed_
    AlgoSpectrumApp.key_on_plot_pressed = key_on_plot_pressed_

    AlgoSpectrumApp.show_plot = show_plot_
    AlgoSpectrumApp.create_metric_widgets = create_metric_widgets_
    AlgoSpectrumApp.analysis_spectr_type_changed = analysis_spectr_type_changed_

    AlgoSpectrumApp.multiply_to_number = multiply_to_number_
    AlgoSpectrumApp.multiply = multiply_
    AlgoSpectrumApp.set_multiply_life_time = set_multiply_life_time_
    AlgoSpectrumApp.used_spectr_type_changed = used_spectr_type_changed_
    AlgoSpectrumApp.show_programm_info = show_programm_info_

    AlgoSpectrumApp.set_analysis_window = set_analysis_window_
    AlgoSpectrumApp.show_analysis_window_func = show_analysis_window_func_
    AlgoSpectrumApp.ok_button_analysis_window = ok_button_analysis_window_
if __name__ == "__main__":
    Init()
    App = AlgoSpectrumApp()
    App.mainloop()
