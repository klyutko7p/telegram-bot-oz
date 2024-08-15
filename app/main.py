import re

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

chrome_options = webdriver.ChromeOptions()
# chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")

driver = webdriver.Chrome()
print("Браузер успешно открыт")

from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/post_endpoint', methods=['POST'])
def handle_post():
    url = request.json['url']
    print(url)
    driver.implicitly_wait(10)
    driver.get(url)

    try:
        price_element = driver.find_elements(By.CLASS_NAME, "m6n_27")[0].text
        title_element = driver.find_elements(By.CLASS_NAME, "m2o_27")[0].text
        price = price_element
        title = title_element


    except Exception as e:
        print("Ошибка при поиске заголовка страницы:", e)
        return None

    response_data = {'status': 'success', 'message': f'{price}, {title}'}
    return jsonify(response_data)