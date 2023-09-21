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

options = webdriver.EdgeOptions()
if HEADLESS:
    options.add_argument('--headless')
driver = webdriver.Edge(options=options)

url = 'https://portal.uad.ac.id/login'
driver.get(url)
driver.find_element(By.NAME, 'login').send_keys(USERNAME)
driver.find_element(By.NAME, 'password').send_keys(PASSWORD)
driver.find_element(By.ID, 'form').find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

url = 'https://portal.uad.ac.id/presensi/Kuliah'
driver.get(url)

try:
    try:
        driver.find_element(By.CSS_SELECTOR, 'div.note.note-info')
        print('Tidak ada presensi saat ini..')
        pass
    except:
        form = driver.find_element(By.CSS_SELECTOR, 'form.form-horizontal')
        rows = form.find_elements(By.CSS_SELECTOR, 'tbody tr')
        for row in rows:
            print(row.text)
        driver.find_element(By.CSS_SELECTOR, 'div.note.note-info')
        print('Anda sudah melakukan presensi..')
except:
    form = driver.find_element(By.CSS_SELECTOR, 'form.form-horizontal')
    rows = form.find_elements(By.CSS_SELECTOR, 'tbody tr')
    for row in rows:
        print(row.text)
    form.find_element(By.CSS_SELECTOR, 'button[value="btnpresensi"]').click()
    print('Presensi berhasil dilakukan..')

driver.quit()
quit()