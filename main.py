import os
from flask import Flask, render_template, request, redirect, url_for


template_dir = os.path.abspath('/Users/danlellouche/Desktop/ITC_FEB_2023/pythonProject1')

app = Flask(__name__, template_folder=template_dir)

# Routes et autres configurations...
