from flask import Flask
import pickle
import numpy as np


APP = Flask(__name__)

#print hello woled

@APP.route("/")
def hello():
    return "Hello World"

if __name__ == '__main__':
    APP.run(debug=True)
