import numpy as np
import os

def get_setting(setting, file):
    dirs = os.getcwd().split("\\")[-1].lower()
    if dirs == "HomeHubv2":
        file = os.getcwd() + "\\app\\" + file
    if os.path.isfile(file):
        read_dictionary = np.load(file,allow_pickle='TRUE').item()
        #print(read_dictionary)
        got_setting = read_dictionary[setting]

    else:
        print(f"{file} not found, {setting} not loaded.")
        got_setting = ""
    return got_setting

def save_setting(setting, setting_value,file):
    dirs = os.getcwd().split("\\")[-1].lower()
    if dirs == "HomeHubv2":
        file = os.getcwd() + "\\app\\" + file
    if os.path.isfile(file):
        read_dictionary = np.load(file,allow_pickle='TRUE').item()
    else:
        read_dictionary = dict()
    read_dictionary[setting] = setting_value
    np.save(file, read_dictionary, allow_pickle='TRUE')