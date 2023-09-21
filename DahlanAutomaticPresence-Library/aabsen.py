from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os

USERNAME = ''
PASSWORD = ''
NIM = ''
HEADLESS = False

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, 'account.txt')
if not os.path.isfile(file_path):
    print('File account.txt tidak ditemukan..')
    USERNAME = input('Masukkan username: ')
    import getpass
    PASSWORD = getpass.getpass(prompt='Masukkan password: ')
    NIM = input('Masukkan NIM: ')
    with open(file_path, 'w') as f:
        f.write(USERNAME + '\n')
        f.write(PASSWORD + '\n')
        f.write(NIM + '\n')
        f.close()
else:
    with open(file_path, 'r') as f:
        USERNAME = f.readline().strip()
        PASSWORD = f.readline().strip()
        NIM = f.readline().strip()
        f.close()

options = webdriver.EdgeOptions()
if HEADLESS:
    options.add_argument('--headless')
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Edge(options=options)

url = 'http://simpus.uad.ac.id/'
driver.get(url)

driver.find_element(By.NAME, 'user').send_keys(USERNAME)
driver.find_element(By.NAME, 'pass').send_keys(PASSWORD)
driver.find_element(By.ID, 'form-login').find_element(By.CSS_SELECTOR, 'input[type="submit"]').click()
url = "http://simpus.uad.ac.id/?mod=pengunjung&sub=pengunjung&do=daftar"
driver.get(url)

driver.find_element(By.NAME, 'nim').send_keys(NIM)
driver.find_element(By.NAME, 'simpan').click()
