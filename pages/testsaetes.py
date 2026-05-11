from faker.contrib.pytest.plugin import faker
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.chrome.options import Options

# options = Options()
# options.add_experimental_option("detach", True)
# options.add_argument('guest')
# options.add_argument("--headless=new")
# driver = webdriver.Chrome(options=options)
# base_url = 'https://pitergsm.ru/personal/order/make/'
# driver.get(base_url)
# driver.maximize_window()
# wait = WebDriverWait(driver, 10)
from faker import Faker

f = Faker('ru_RU')

print(f.street_name())
print(f.building_number())

# time.sleep(2)
# driver.close()

