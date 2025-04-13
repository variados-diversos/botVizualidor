from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pyautogui
import random
import time
import threading

proxy_host = "na.wq08cilx.lunaproxy.net"
proxy_port = 12233
proxy_user = "user-jungjunior25_P2mgO"
proxy_pass = "Resgate27"

print('Iniciando conexão com proxy...')

while True:
    try:
        chrome_options1 = Options()
        chrome_options1.add_experimental_option("mobileEmulation", {"deviceName": "iPhone X"})
        # Configura o proxy
        #chrome_options1.add_argument(f'--proxy-server=http://{proxy_user}:{proxy_pass}@{proxy_host}:{proxy_port}')

        # Configura o tamanho da janela (400x500) e a posição (0,0)
        chrome_options1.add_argument("--window-size=400,500")
        chrome_options1.add_argument("--window-position=0,0")

        # Inicia o Chrome com as opções configuradas
        driver1 = webdriver.Chrome(options=chrome_options1)

        # Acessa uma página para testar
        driver1.get("https://dicasdodi.com/")
        chrome_options2 = Options()
        chrome_options2.add_experimental_option("mobileEmulation", {"deviceName": "iPhone X"})
        # Configura o proxy
        #chrome_options2.add_argument(f'--proxy-server=http://{proxy_user}:{proxy_pass}@{proxy_host}:{proxy_port}')

        # Configura o tamanho da janela (400x500) e a posição (0,0)
        chrome_options2.add_argument("--window-size=400,500")
        chrome_options2.add_argument("--window-position=500,0")

        # Inicia o Chrome com as opções configuradas
        driver2 = webdriver.Chrome(options=chrome_options2)

        # Acessa uma página para testar
        driver2.get("https://dicasdodi.com")

        chrome_options3 = Options()
        chrome_options3.add_experimental_option("mobileEmulation", {"deviceName": "iPhone X"})
        # Configura o proxy
        #chrome_options2.add_argument(f'--proxy-server=http://{proxy_user}:{proxy_pass}@{proxy_host}:{proxy_port}')

        # Configura o tamanho da janela (400x500) e a posição (0,0)
        chrome_options3.add_argument("--window-size=400,500")
        chrome_options3.add_argument("--window-position=1000,0")

        # Inicia o Chrome com as opções configuradas
        driver3 = webdriver.Chrome(options=chrome_options3)

        # Acessa uma página para testar
        driver3.get("https://dicasdodi.com")

        chrome_options4 = Options()
        chrome_options4.add_experimental_option("mobileEmulation", {"deviceName": "iPhone X"})
        # Configura o proxy
        #chrome_options2.add_argument(f'--proxy-server=http://{proxy_user}:{proxy_pass}@{proxy_host}:{proxy_port}')

        # Configura o tamanho da janela (400x500) e a posição (0,0)
        chrome_options4.add_argument("--window-size=400,500")
        chrome_options4.add_argument("--window-position=0,500")

        # Inicia o Chrome com as opções configuradas
        driver4 = webdriver.Chrome(options=chrome_options4)

        # Acessa uma página para testar
        driver4.get("https://dicasdodi.com") 

        chrome_options5 = Options()
        chrome_options5.add_experimental_option("mobileEmulation", {"deviceName": "iPhone X"})
        # Configura o proxy
        #chrome_options2.add_argument(f'--proxy-server=http://{proxy_user}:{proxy_pass}@{proxy_host}:{proxy_port}')

        # Configura o tamanho da janela (400x500) e a posição (0,0)
        chrome_options5.add_argument("--window-size=400,500")
        chrome_options5.add_argument("--window-position=500,500")

        # Inicia o Chrome com as opções configuradas
        driver5 = webdriver.Chrome(options=chrome_options5)

        # Acessa uma página para testar
        driver5.get("https://dicasdodi.com")
        
        chrome_options6 = Options()
        chrome_options6.add_experimental_option("mobileEmulation", {"deviceName": "iPhone X"})
        # Configura o proxy
        #chrome_options2.add_argument(f'--proxy-server=http://{proxy_user}:{proxy_pass}@{proxy_host}:{proxy_port}')

        # Configura o tamanho da janela (400x500) e a posição (0,0)
        chrome_options6.add_argument("--window-size=400,500")
        chrome_options6.add_argument("--window-position=1000,500")

        # Inicia o Chrome com as opções configuradas
        driver6 = webdriver.Chrome(options=chrome_options6)

        # Acessa uma página para testar
        driver6.get("https://www.facebook.com/61566807274239/posts/122147574176560242/")

        pyautogui.moveTo(95, 415, duration=2)
        pyautogui.click()
        time.sleep(1)
        pyautogui.moveTo(365, 160, duration=2)
        pyautogui.click()
        time.sleep(1)
        pyautogui.scroll(-600)
        pyautogui.moveTo(210, 390, duration=2)
        pyautogui.click()
        time.sleep(1)
        pyautogui.moveTo(210, 390, duration=2)
        pyautogui.click()
        time.sleep(1)
        pyautogui.moveTo(320, 460, duration=2)
        pyautogui.click()
        time.sleep(1)

        print('janela 2')
        pyautogui.moveTo(600, 420, duration=2)
        pyautogui.click()
        time.sleep(2)
        pyautogui.moveTo(865, 170, duration=2)
        pyautogui.click()
        time.sleep(1)
        pyautogui.moveTo(700, 450, duration=2)
        pyautogui.click()
        time.sleep(1)
        pyautogui.moveTo(740, 425, duration=2)
        pyautogui.click()
        time.sleep(1)

        
        print('janela 3')
        time.sleep(1)
        pyautogui.moveTo(1100, 420, duration=2)
        pyautogui.click()
        time.sleep(1)
        pyautogui.moveTo(1365, 170, duration=2)
        pyautogui.click()
        time.sleep(1)
        pyautogui.scroll(-800)
        pyautogui.moveTo(1200, 255, duration=2)
        pyautogui.click()
        time.sleep(1)
        pyautogui.moveTo(1290, 475, duration=2)
        pyautogui.click()
        time.sleep(1)


        print('janela 4')
        time.sleep(1)
        pyautogui.moveTo(100, 920, duration=2)
        pyautogui.click()
        time.sleep(1)
        pyautogui.moveTo(365, 670, duration=2)
        pyautogui.click()
        time.sleep(1)
        pyautogui.moveTo(230, 930, duration=2)
        pyautogui.scroll(-200)
        time.sleep(1)
        pyautogui.scroll(-100)
        time.sleep(1)
        pyautogui.scroll(-300)
        time.sleep(1)
        pyautogui.click()
        time.sleep(1)
        


        print('janela 5')
        pyautogui.click()
        time.sleep(1)
        pyautogui.moveTo(600, 920, duration=2)
        pyautogui.click()
        time.sleep(1)
        pyautogui.moveTo(865, 670, duration=2)
        pyautogui.click()
        time.sleep(1)
        pyautogui.scroll(-1100)
        pyautogui.moveTo(725, 920, duration=2)
        pyautogui.click()
        time.sleep(1)

        print('janela 6')
        time.sleep(1)
        pyautogui.moveTo(1025, 900, duration=2)
        time.sleep(1)
        pyautogui.click()
        pyautogui.moveTo(1335, 850, duration=2)
        pyautogui.click()
        time.sleep(1)
        pyautogui.moveTo(1330, 880, duration=2)
        pyautogui.click()
        time.sleep(2)
        pyautogui.moveTo(1035, 920, duration=2)
        pyautogui.click()
        time.sleep(1)
        pyautogui.moveTo(1400, 975, duration=2)
        pyautogui.click()
        time.sleep(1)
        pyautogui.moveTo(1350, 935, duration=2)
        pyautogui.click()
        time.sleep(1)

        driver1.quit()
        driver2.quit()
        driver3.quit()
        driver4.quit()
        driver5.quit()
        driver6.quit()
        time.sleep(2)
        print('reiniciando processo')

    except:
        driver1.quit()
        driver2.quit()
        driver3.quit()
        driver4.quit()
        driver5.quit()
        driver6.quit()
        print('reiniciando processo')
        time.sleep(2)
        continue
