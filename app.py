#!/usr/bin/env python3.9
from flask import Flask, render_template, request, jsonify
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.edge.service import Service
import warnings

warnings.filterwarnings("ignore")

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/validate', methods=['POST'])
def validate():
    data = request.json
    edge_options = EdgeOptions()
    edge_options.use_chromium = True  # Use Chromium Edge
    edge_options.add_argument("--headless")  # Enable headless mode
    msedgedriver_path = "msedgedriver.exe"
    edge_service = Service(msedgedriver_path)
    browser = webdriver.Edge(service=edge_service, options=edge_options)
    browser_name = "Edge"
    browser.get("http://192.168.100.1:8090/httpclient.html")
    # Find and fill form elements
    input_field = browser.find_element(By.NAME, "username")
    input_field.send_keys(data['username'])
    input_field = browser.find_element(By.NAME, "password")
    input_field.send_keys(data['password'])
    # Submit the form
    button_row = browser.find_element(By.ID, "loginbutton")
    button_row.click()
    return jsonify({"status": "success"})

@app.route('/api/scheduleAuth')
def scheduleAuth():
    pass

if __name__ == '__main__':
    app.run(debug=True)