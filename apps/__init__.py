from flask import Flask
#from apps.forms import LinkForm

app = Flask(__name__)
from apps import Config
from apps import views,models
