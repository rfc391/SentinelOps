from dotenv import load_dotenv
import os
load_dotenv()
from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to the SentinelOps Project"

@app.route('/test')
def test():
    return "This is a test route"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
