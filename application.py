import os 
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash

from rest_api import twilio

application = Flask(__name__)

@application.route('/')
def hello():
    return render_template('home.html')

@application.route('/twilio')
def twilio():
    return render_template('twilio.html')

@application.route('/weather')
def weather():
    return render_template('weather.html')

@application.route('/googleApi')
def googleA():
    return render_template('googleApi.html')

@application.route('/numbers')
def numbers():
    return render_template('numbers.html')

@application.route('/music')
def music():
    return render_template('music.html')

@application.route('/photoGarage')
def photo():
    return render_template('photoGarage.html')

@application.route('/me')
def me():
    return redirect("dayoasaolu.com")