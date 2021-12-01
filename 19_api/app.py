# Team TSP: Sean Ging, Patrick Ging, Theo Fahey
# SoftDev
# K19 -- A RESTful Journey Skyward; API Keys, JSON, urllib.request
# 2021-11-23
# time spent: 1hr
from flask import Flask, render_template
import urllib.request
from urllib.request import urlopen
import json
app = Flask(__name__) # Q0: Where have you seen similar syntax in other langs?

@app.route("/") # Q1: What points of reference do you have for meaning of '/'?
def hello_world():
    r = urllib.request.urlopen("https://api.nasa.gov/planetary/apod?api_key=LPfJmwHEcDyxTs2fZBZdAAOTjElf7Q4hTNZLFZiJ").read()
    x = json.loads(r)
    return render_template("main.html", pic = x["url"], para = x["explanation"])
app.run()
