import os
import sys
import glob

from flask import Flask, flash, request, redirect, url_for, render_template
from flask import send_from_directory
from werkzeug.utils import secure_filename
from PIL import Image

import io
import base64

from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

import os
import glob
import argparse


import logging
from orcacnnapp.config import Config

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

logging.getLogger('matplotlib.font_manager').disabled = True

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    from orcacnnapp.main.routes import main
    from orcacnnapp.upload.routes import upload
    from orcacnnapp.errors.handlers import errors
    app.register_blueprint(main)
    app.register_blueprint(upload)
    app.register_blueprint(errors)

    return app
