from app import app
from flask import render_template
from app.modules import user

@app.route('/')
@app.route('/index/')
def index():
    return render_template("index.html", user=user.settings['user'])
