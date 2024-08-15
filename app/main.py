import re

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless=new")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-renderer-backgrounding")
chrome_options.add_argument("--disable-background-timer-throttling")
chrome_options.add_argument("--disable-backgrounding-occluded-windows")
chrome_options.add_argument("--disable-client-side-phishing-detection")
chrome_options.add_argument("--disable-crash-reporter")
chrome_options.add_argument("--disable-oopr-debug-crash-dump")
chrome_options.add_argument("--no-crash-upload")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-low-res-tiling")
chrome_options.add_argument("--log-level=3")
chrome_options.add_argument("--silent")
# chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")

driver = webdriver.Chrome(options=chrome_options)
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
        title_element = driver.find_elements(By.TAG_NAME, "h1")[0].text
        price = price_element
        title = title_element


    except Exception as e:
        print("Ошибка при поиске заголовка страницы:", e)
        return None

    response_data = {'status': 'success', 'message': f'{price}, {title}'}
    return jsonify(response_data)
