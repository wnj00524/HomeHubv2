import os
import json

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KET') or 'basic_key_ok'

def load_settings(settingFile):
    if not os.path.isfile(settingFile):
        init_settings(settingFile)
    with open(settingFile,"r") as fp:
        settings = json.load(fp)
    return settings



def init_settings(settingFile):
    settings = { "user": "Bob" }
    settings["weather_api_key"] = "null"
    settings["location"] = "London, GB"
    with open(settingFile,"w") as p:
        json.dump(settings, p)
    return 0