import re

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium_stealth import stealth
from flask import Flask, request, jsonify
import time
import json
import os

options = Options()
options.add_argument("--headless");
options.add_argument("--disable-gpu");
options.add_argument("--no-sandbox");

def init_webdriver():
    driver = webdriver.Chrome(options=options)
    stealth(driver, platform="Win32")
    return driver
    
print("Браузер успешно открыт")

app = Flask(__name__)

driver = init_webdriver()
@app.route('/post_endpoint', methods=['POST'])
def handle_post():
    url = request.json['url']
    print(url)
    driver.get(url)
    time.sleep(5)
    jsonData = driver.find_element(By.TAG_NAME, "body").text
    jsonDataReturn = json.loads(jsonData)["seo"]["script"][0]['innerHTML']

    response_data = {'status': 'success', 'message': f'{jsonDataReturn}'}
    return jsonify(response_data)
