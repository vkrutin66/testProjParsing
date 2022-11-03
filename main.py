from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

url = "https://home-club.com.ua/ua/sku-90507603?gclid=CjwKCAjwzY2bBhB6EiwAPpUpZhSieA2DRWXhLcbNCpIvJcC9dLHc534Djx5FKNpL9iXaLZlSQaNyLBoCEwYQAvD_BwE"
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


def open_browser():
    driver.get(url)
    driver.maximize_window()


def get_info():
    article = driver.find_element(By.CSS_SELECTOR, '.overview .additional-details .sku').text + "\n"
    supply = driver.find_element(By.CSS_SELECTOR, '.overview .additional-details div:nth-child(2)').text + "\n"
    poland = driver.find_element(By.CSS_SELECTOR, '.overview .additional-details div:nth-child(3)').text + "\n"
    lviv = driver.find_element(By.CSS_SELECTOR, '.overview .additional-details div:last-child').text + "\n"
    return article + supply + poland + lviv


def output_info(text):
    file = open('output/output.txt', 'w+', encoding="utf-8")
    file.write(text)
    file.close()


def close_browser():
    driver.quit()


open_browser()
info_from_site = get_info()
output_info(info_from_site)
close_browser()
