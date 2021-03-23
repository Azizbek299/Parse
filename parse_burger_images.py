import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests

driver = webdriver.Firefox(executable_path='/home/alex/Downloads/geckodriver')


def get_image(list_url):
    count = 0
    for i in list_url:
        v = f'https://.ru/{i}'
        count += 1
        response_image = requests.get(v).content
        with open(f'/home/alex/Desktop/burger/{i[24:]}.webp', 'wb') as fb:
            fb.write(response_image)
            print('write', count)
    print('all find')


def bs(htmll):
    soup = BeautifulSoup(htmll, 'html.parser')
    burger_ul = soup.find('ul', class_='base-grid-container menu-catalog')
    burger_li = burger_ul.findAll('li', class_='catalog-product base-grid-item')
    print(len(burger_li))
    l = []
    for i in burger_li:
        c = i.find('div', class_='catalog-product__image')['style'][23:-3]
        l.append(c)
    return get_image(l)


def parse_burger_image():
    driver.maximize_window()
    driver.get('https://.ru/')
    time.sleep(10)
    driver.execute_script("window.scrollTo(0,2142)")
    time.sleep(10)
    driver.find_element(By.CSS_SELECTOR,
                        ".menu-categories__wrap > .menu-categories__item:nth-child(5) > span").click()

    time.sleep(10)
    driver.execute_script("window.scrollTo(0,1481)")
    time.sleep(10)
    driver.execute_script("window.scrollTo(0,2081)")
    time.sleep(10)
    driver.execute_script("window.scrollTo(0,2485)")
    time.sleep(10)
    driver.execute_script("window.scrollTo(1800,0)")
    time.sleep(10)
    html = driver.page_source
    return bs(html)


# parse_burger_image()


def get_image1(list_urll):
    count = 0
    for i in list_urll:
        v = f'https://.ru/{i}'
        count += 1
        response_image = requests.get(v).content
        with open(f'/home/alex/Desktop/burger/_image/potato_image/{i[24:]}.webp', 'wb') as fb:
            fb.write(response_image)
            print('write', count)
    print('all find')


def bs1(htmlll):
    soup = BeautifulSoup(htmlll, 'html.parser')
    burger_ul = soup.find('ul', class_='base-grid-container menu-catalog')
    burger_li = burger_ul.findAll('li', class_='catalog-product base-grid-item')
    ll = []
    for i in burger_li:
        c = i.find('div', class_='catalog-product__image')['style'][23:-3]
        ll.append(c)
    return get_image1(ll)


def parse_potato_image():
    driver.maximize_window()
    driver.get('https://.ru/')
    time.sleep(10)
    driver.execute_script("window.scrollTo(0,2142)")
    time.sleep(10)
    driver.find_element(By.CSS_SELECTOR,
                        ".menu-categories__wrap > .menu-categories__item:nth-child(6) > span").click()

    time.sleep(10)
    driver.execute_script("window.scrollTo(0,1481)")
    time.sleep(10)
    driver.execute_script("window.scrollTo(0,2081)")
    time.sleep(10)
    driver.execute_script("window.scrollTo(0,2485)")
    time.sleep(10)
    driver.execute_script("window.scrollTo(0,2485)")
    time.sleep(10)
    driver.execute_script("window.scrollTo(1800,0)")
    time.sleep(10)
    driver.execute_script("window.scrollTo(1800,0)")
    time.sleep(10)
    html1 = driver.page_source
    return bs1(html1)


# parse_potato_image()


def get_image2(list_urll):
    count = 0
    for i in list_urll:
        v = f'https://.ru/{i}'
        count += 1
        response_image = requests.get(v).content
        with open(f'/home/alex/Desktop/burger/_image/roll_image/{i[24:]}.webp', 'wb') as fb:
            fb.write(response_image)
            print('write', count)
    print('all find')


def bs2(htmlll):
    soup = BeautifulSoup(htmlll, 'html.parser')
    burger_ul = soup.find('ul', class_='base-grid-container menu-catalog')
    burger_li = burger_ul.findAll('li', class_='catalog-product base-grid-item')
    ll = []
    for i in burger_li:
        c = i.find('div', class_='catalog-product__image')['style'][23:-3]
        ll.append(c)
    return get_image2(ll)


def parse_roll_image():
    driver.maximize_window()
    driver.get('https://.ru/')
    time.sleep(10)
    driver.execute_script("window.scrollTo(0,2142)")
    time.sleep(10)
    driver.find_element(By.CSS_SELECTOR,
                        ".menu-categories__wrap > .menu-categories__item:nth-child(7) > span").click()

    time.sleep(10)
    driver.execute_script("window.scrollTo(0,1481)")
    time.sleep(10)
    driver.execute_script("window.scrollTo(0,2081)")
    time.sleep(10)
    driver.execute_script("window.scrollTo(1800,0)")
    time.sleep(10)
    html = driver.page_source
    return bs2(html)


# parse_roll_image()


def parse_desert_image():
    driver.maximize_window()
    driver.get('https://.ru/')
    time.sleep(10)
    driver.execute_script("window.scrollTo(0,2142)")
    time.sleep(10)
    driver.find_element(By.CSS_SELECTOR,
                        ".menu-categories__wrap > .menu-categories__item:nth-child(8) > span").click()

    time.sleep(10)
    driver.execute_script("window.scrollTo(0,1481)")
    time.sleep(10)
    driver.execute_script("window.scrollTo(0,2081)")
    time.sleep(10)
    driver.execute_script("window.scrollTo(0,2081)")
    time.sleep(10)
    driver.execute_script("window.scrollTo(1800,0)")
    time.sleep(10)
    html = driver.page_source
    return bs(html)


# parse_desert_image()


def parse_drinks_image():
    driver.maximize_window()
    driver.get('https://.ru/')
    time.sleep(10)
    driver.execute_script("window.scrollTo(0,1596)")
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, ".menu-categories_parent-fixed .menu-categories__more ").click()
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, ".menu-categories__item_hidden:nth-child(1) > span").click()
    time.sleep(10)
    driver.execute_script("window.scrollTo(0,1710)")
    time.sleep(5)
    driver.execute_script("window.scrollTo(0,2906)")
    time.sleep(5)
    driver.execute_script("window.scrollTo(0,3192)")
    time.sleep(5)
    driver.execute_script("window.scrollTo(0,1187)")
    time.sleep(5)
    html = driver.page_source
    return bs(html)


# parse_drinks_image()


def parse_source_image():
    driver.maximize_window()
    driver.get('https://.ru/')
    time.sleep(10)
    driver.execute_script("window.scrollTo(0,1596)")
    time.sleep(10)
    driver.find_element(By.CSS_SELECTOR, ".menu-categories_parent-fixed .menu-categories__more ").click()
    time.sleep(10)
    driver.find_element(By.CSS_SELECTOR, ".menu-categories__item_hidden:nth-child(2) > span").click()
    time.sleep(10)
    driver.execute_script("window.scrollTo(0,1710)")
    time.sleep(5)
    driver.execute_script("window.scrollTo(0,2906)")
    time.sleep(5)
    driver.execute_script("window.scrollTo(0,3192)")
    time.sleep(5)
    driver.execute_script("window.scrollTo(0,1187)")
    time.sleep(5)
    html = driver.page_source
    return bs(html)


# parse_source_image()


def parse_breakfast_image():
    driver.maximize_window()
    driver.get('https://.ru/')
    time.sleep(10)
    driver.execute_script("window.scrollTo(0,1596)")
    time.sleep(10)
    driver.find_element(By.CSS_SELECTOR, ".menu-categories_parent-fixed .menu-categories__more ").click()
    time.sleep(10)
    driver.find_element(By.CSS_SELECTOR, ".menu-categories__item_hidden:nth-child(3) > span").click()
    time.sleep(10)
    driver.execute_script("window.scrollTo(0,1710)")
    time.sleep(10)
    driver.execute_script("window.scrollTo(0,2906)")
    time.sleep(10)
    driver.execute_script("window.scrollTo(0,3192)")
    time.sleep(10)
    driver.execute_script("window.scrollTo(0,1187)")
    time.sleep(10)
    driver.execute_script("window.scrollTo(0,1710)")
    time.sleep(10)
    driver.execute_script("window.scrollTo(2906,0)")
    time.sleep(10)
    driver.execute_script("window.scrollTo(3192,0)")
    time.sleep(10)
    driver.execute_script("window.scrollTo(1187,0)")
    time.sleep(10)
    driver.execute_script("window.scrollTo(1710,0)")
    time.sleep(10)
    driver.execute_script("window.scrollTo(2906,0)")
    time.sleep(10)
    driver.execute_script("window.scrollTo(3192, 0)")
    time.sleep(10)
    driver.execute_script("window.scrollTo(1187,0)")
    time.sleep(10)
    html = driver.page_source
    return bs(html)


# parse_breakfast_image()