from flask import Flask
from app.modules import settings



settings.load_settings("settings.dat")
app = Flask(__name__)
app.config.from_object(settings.Config)


from app import routes