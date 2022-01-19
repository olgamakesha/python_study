# coding=utf-8

import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC



drv = webdriver.Chrome('chromedriver.exe')
drv.get('https://google.com/search?q=selenide')

wait = WebDriverWait(drv, 15)

wait.until(EC.presence_of_all_elements_located((By.XPATH, '//div[@class="g"]')))
headings = drv.find_elements_by_xpath('//div[@class="g"]')

assert len(headings) > 0

title = headings[0].find_elements_by_tag_name('h3')
link = headings[0].find_element_by_css_selector('.yuRUbf>a').get_attribute("href")

assert "https://selenide.org" in link

header_links = drv.find_elements_by_xpath('//div[@id="hdtb-msb"]/div/div/div/a')

header_links[0].click()
wait.until(EC.presence_of_all_elements_located((By.XPATH, '//span[@jsslot]')))
images = drv.find_elements_by_xpath('//span[@jsslot]/div/div/div/a/div/img')
assert len(images) > 0
assert 'Selenide' in images[0].get_attribute('alt')

# Переходим на "Все" результаты и проверяем что первая ссылка такая же как в самом начале сценария
header_links = drv.find_elements_by_xpath('//div/c-wiz[@jsrenderer]/div/div/div/div/div/div/a')
assert len(header_links) > 0
header_links[0].click()

wait.until(EC.presence_of_all_elements_located((By.XPATH, '//div[@class="g"]')))
headings = drv.find_elements_by_xpath('//div[@class="g"]')

assert len(headings) > 0

title = headings[0].find_elements_by_tag_name('h3')
link = headings[0].find_element_by_css_selector('.yuRUbf>a').get_attribute("href")

assert "https://selenide.org" in link

drv.close()