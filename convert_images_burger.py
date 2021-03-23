from selenium import webdriver
import time
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(executable_path='/home/alex/Downloads/chromedriver')
import os


def test():
    driver.maximize_window()
    c = os.listdir('/home/alex/Desktop/burger/all_images')
    for i in c:
        print('1')
        driver.get('https://onlineconvertfree.com/ru/complete/webp-png/')
        print('2')
        time.sleep(5)
        print('3')
        driver.execute_script("window.scrollTo(0,171)")
        time.sleep(5)
        print('4')
        driver.execute_script("window.scrollTo(0,1087)")
        time.sleep(10)
        driver.execute_script("window.scrollTo(500,0)")
        print('5')
        time.sleep(10)
        print('6')
        driver.find_element(By.CSS_SELECTOR, ".file-loader__input:nth-child(2)").send_keys(
            f"/home/alex/Desktop/burger/all_images/{i}")
        time.sleep(15)
        print('7')
        driver.execute_script("window.scrollTo(0,200)")
        driver.find_element(By.CSS_SELECTOR, ".file-item-res-box__btn").click()
        time.sleep(10)
        print('8')
        driver.find_element(By.CSS_SELECTOR, ".file-item-res-box__search-input").click()
        time.sleep(6)
        print('9')
        time.sleep(3)
        driver.find_element(By.CSS_SELECTOR, ".file-item-res-box__search-input").send_keys("png")
        time.sleep(3)
        print('10')
        driver.find_element(By.CSS_SELECTOR, ".file-item-res-box__formats-item").click()
        time.sleep(3)
        driver.execute_script("window.scrollTo(500,0)")
        print('11')
        driver.find_element(By.CSS_SELECTOR, ".button--start").click()
        time.sleep(20)
        print('12')
        driver.execute_script("window.scrollTo(0,1087)")
        time.sleep(5)
        time.sleep(5)
        driver.find_element(By.CSS_SELECTOR, ".file-item__link").click()
        print('13')
        time.sleep(10)
        driver.refresh()
        time.sleep(10)
        driver.execute_script("window.scrollTo(500,0)")


# test()
