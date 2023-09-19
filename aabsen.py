from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os
import time

USERNAME = ''
PASSWORD = ''
HEADLESS = False

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, 'secret.txt')
if not os.path.isfile(file_path):
    print('File secret.txt tidak ditemukan..')
    USERNAME = input('Masukkan username: ')
    import getpass
    PASSWORD = getpass.getpass(prompt='Masukkan password: ')
    with open(file_path, 'w') as f:
        f.write(USERNAME + '\n')
        f.write(PASSWORD + '\n')
        f.close()
else:
    with open(file_path, 'r') as f:
        USERNAME = f.readline().strip()
        PASSWORD = f.readline().strip()
        f.close()

options = webdriver.ChromeOptions()
if HEADLESS:
    options.add_argument('--headless')
driver = webdriver.Chrome(options=options)

url = 'https://portal.uad.ac.id/login'
driver.get(url)
driver.find_element(By.NAME, 'login').send_keys(USERNAME)
driver.find_element(By.NAME, 'password').send_keys(PASSWORD)
driver.find_element(By.ID, 'form').find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

url = 'https://portal.uad.ac.id/presensi/Kuliah'
driver.get(url)
note = driver.find_element(By.CSS_SELECTOR, '.note-info').text
if 'Tidak ada Presensi Kelas Matakuliah saat ini.' in note:
    print('Tidak ada Presensi Kelas saat ini.')
    driver.quit()
    exit()
else:
    print('Ada Presensi Kelas Matakuliah saat ini.')
driver.quit()