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
        if request.form.get('Netflix') == 'netflix':
            lg_tv.run_app(user.settings['tv_ip'], 'netflix')
        if request.form.get('GamePass') == 'gamepass':
            lg_tv.run_app(user.settings['tv_ip'], 'com.deltatre.nflgamepass.lgapp')
    return render_template("index.html", user=user.settings['user'], temp=gotWeather.temp, wind_speed=gotWeather.wind_speed, wind_direction=gotWeather.wind_dir, location=gotWeather.location)

@app.route('/debug')
def debug():
    Apps = lg_tv.list_app(user.settings['tv_ip'])
    #print(f"Apps = {Apps}")
    return render_template("debug.html",name=user.settings['user'],tv_ip=user.settings['tv_ip'],tv_mac=user.settings['tv_mac'],apps=Apps, current_tv_app=lg_tv.list_current_app(user.settings['tv_ip']))