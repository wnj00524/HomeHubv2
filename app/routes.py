from app import app
from flask import render_template, request
from app.modules import user
from app.modules import weather
from app.modules import lg_tv

@app.route('/', methods=['GET', 'POST'])
@app.route('/index/', methods=['GET', 'POST'])
def index():
    gotWeather = weather.get_weather(user.settings['location'], user.settings['weather_api_key'])
    if request.method == 'POST':
        if request.form.get('Wake') == 'wake':
            lg_tv.wakeup(user.settings['tv_mac'])
    return render_template("index.html", user=user.settings['user'], temp=gotWeather.temp, wind_speed=gotWeather.wind_speed, wind_direction=gotWeather.wind_dir, location=gotWeather.location)
