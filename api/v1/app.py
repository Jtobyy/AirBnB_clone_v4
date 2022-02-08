#!/usr/bin/python3
"""
default flask app
"""

from flask import Flask
from models import storage
from api.v1.views import app_views

app = Flask(__name__)
