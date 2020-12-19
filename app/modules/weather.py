from pyowm import OWM
import app.modules.tools as tools
import time as t
import os
import ast



class weather():
    temp = ""
    wind_speed = ""
    wind_dir = ""
    rain = ""
    clouds = ""
    desc = ""
    time_got = ""
    hr_time_got = ""
    location = ""

wt = weather()

def first_run_check():
    file = 'weather.npy'
    dirs = os.getcwd().split("\\")[-1].lower()
    if dirs == "HomeHubv2":
        file = os.getcwd() + "\\app\\" + file
    if os.path.isfile(file) == False:
        return True
    else:
        return False

def saved_weather_file_path(file):
    dirs = os.getcwd().split("\\")[-1].lower()
    if dirs == "HumHubv2":
        file = os.getcwd() + "\\app\\" + file
    return file

#w.detailed_status         # 'clouds'
#w.wind()                  # {'speed': 4.6, 'deg': 330}
#w.humidity                # 87
#print(w.temperature('celsius'))  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
#w.rain                    # {}
#w.heat_index              # None
#w.clouds                  # 75

def save_weather(w, rec_time):
    fileN = "weather.npy"
    tools.save_setting("time_got",rec_time,fileN)
    tools.save_setting("temp", w.temperature('celsius')['temp'], fileN)
    tools.save_setting("wind_speed",w.wind('miles_hour'),fileN)
    #tools.save_setting("wind_dir",w.wind('deg'),fileN)
    tools.save_setting("rain",w.rain,fileN)
    tools.save_setting("clouds",w.clouds,fileN)



def load_weather_from_file(fileName):
    #print("Reading from file....")
    wt.temp = tools.get_setting("temp",fileName)
    wt.time_got = tools.get_setting("time_got", fileName)
    wind_dict = ast.literal_eval(str(tools.get_setting("wind_speed",fileName)))
    wt.wind_speed = wind_dict['speed']
    wt.wind_dir = wind_dict['deg']
    #wt.wind_dir = tools.get_setting("win_dir",fileName)
    #todo work out what rain is returning and use it.
    wt.rain = tools.get_setting("rain",fileName)
    wt.clouds = tools.get_setting("clouds",fileName)
    wt.hr_time_got = t.asctime(t.localtime(float(wt.time_got)))



def get_weather(location, key):
    owm = OWM(key)
    mgr = owm.weather_manager()
    if first_run_check():
        #print("Weather file not found, updating...")
        obs = mgr.weather_at_place(location)
        w = obs.weather
        save_weather(w, obs.rec_time)
    else:
        #todo 2: Check when the weather last updated and if more than ten minutes update the weather.
        time = float(tools.get_setting("time_got","weather.npy"))
        if (t.time() - time) > 600:
            #print("Time for an update...")
            obs = mgr.weather_at_place(location)
            w = obs.weather
            save_weather(w, obs.rec_time)
    load_weather_from_file("weather.npy")
    wt.location = location
    wt.wind_speed = round(wt.wind_speed, 1)
    return wt















