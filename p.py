
import pyautogui
import random
import time
from seleniumwire import webdriver
import threading
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import shutil
from selenium.webdriver.common.action_chains import ActionChains

while True:
    try: 
        proxy_user = "user-jungjunior25_P2mgO"
        proxy_pass = "Resgate27"
        proxy_host = "na.wq08cilx.lunaproxy.net"
        proxy_port = 12233

        options1 = {
            'proxy': {
                'http': f'http://{proxy_user}:{proxy_pass}@{proxy_host}:{proxy_port}',
                'https': f'https://{proxy_user}:{proxy_pass}@{proxy_host}:{proxy_port}',
                'no_proxy': 'localhost,127.0.0.1'
            }
        }

        options2 = {
            'proxy': {
                'http': f'http://{proxy_user}:{proxy_pass}@{proxy_host}:{proxy_port}',
                'https': f'https://{proxy_user}:{proxy_pass}@{proxy_host}:{proxy_port}',
                'no_proxy': 'localhost,127.0.0.1'
            }
        }

        options3 = {
            'proxy': {
                'http': f'http://{proxy_user}:{proxy_pass}@{proxy_host}:{proxy_port}',
                'https': f'https://{proxy_user}:{proxy_pass}@{proxy_host}:{proxy_port}',
                'no_proxy': 'localhost,127.0.0.1'
            }
        }

        options4 = {
            'proxy': {
                'http': f'http://{proxy_user}:{proxy_pass}@{proxy_host}:{proxy_port}',
                'https': f'https://{proxy_user}:{proxy_pass}@{proxy_host}:{proxy_port}',
                'no_proxy': 'localhost,127.0.0.1'
            }
        }

        options5 = {
            'proxy': {
                'http': f'http://{proxy_user}:{proxy_pass}@{proxy_host}:{proxy_port}',
                'https': f'https://{proxy_user}:{proxy_pass}@{proxy_host}:{proxy_port}',
                'no_proxy': 'localhost,127.0.0.1'
            }
        }

        options6 = {
            'proxy': {
                'http': f'http://{proxy_user}:{proxy_pass}@{proxy_host}:{proxy_port}',
                'https': f'https://{proxy_user}:{proxy_pass}@{proxy_host}:{proxy_port}',
                'no_proxy': 'localhost,127.0.0.1'
            }
        }

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("mobileEmulation", {"deviceName": "iPhone X"})

        
        try:
            driver1 = webdriver.Chrome(seleniumwire_options=options1, options=chrome_options)
            driver1.set_window_size(400, 500)
            driver1.set_window_position(0, 0)
            driver1.get("https://dicasdodi.com/cartao-unicred-como-funciona-beneficios-e-como-solicitar-o-seu/?fbclid=IwY2xjawJkGUpleHRuA2FlbQIxMAABHjLXs-4klaLAinvQO_8Yo8Ewsie2Ei41q2_wxbbDFQ2KvSxdirouGvwJ-NC9_aem_IksX6z9k1CoKMLw7Qn6Xzg")
            
            
            clica_anuncio = random.randint(1,1)
            if clica_anuncio == 1:
                print('anuncio sendo clicado')
                tipo_anuncio = random.randint(1,2)  
                if tipo_anuncio == 1:  
                    #anuncio 2
                    print('Anuncio 1')
                    driver1.execute_script("window.scrollBy(0, 30);")
                    time.sleep(0.3)
                    driver1.execute_script("window.scrollBy(0, 30);")
                    time.sleep(0.3)
                    driver1.execute_script("window.scrollBy(0, 30);")
                    time.sleep(0.3)
                    driver1.execute_script("window.scrollBy(0, 30);")
                    time.sleep(0.3)
                    driver1.execute_script("window.scrollBy(0, 30);")
                    time.sleep(0.3)
                    driver1.execute_script("window.scrollBy(0, 30);")   
                    time.sleep(0.3)
                    
                pos = driver1.get_window_position()
                x = pos['x']
                y = pos['y']

                # Pega o tamanho da janela do driver
                size = driver1.get_window_size()
                width = size['width']
                height = size['height']

                # Calcula o centro da janela
                center_x = x + width // 2
                center_y = y + height // 2

                # Move o mouse até o centro da janela com animação
                print('movendo')
                pyautogui.moveTo(center_x, center_y, duration=0.3)
                pyautogui.click()

                print('Clicou anuncio')

                driver1.execute_script("window.scrollBy(0, 30);")
                print('lendo anuncio')
                time.sleep(0.3)
                driver1.execute_script("window.scrollBy(0, 30);")
                time.sleep(0.3)
                driver1.execute_script("window.scrollBy(0, 30);")
                time.sleep(0.3)
                driver1.execute_script("window.scrollBy(0, 30);")
                time.sleep(0.3)
                driver1.execute_script("window.scrollBy(0, 30);")
                time.sleep(0.3)
                driver1.execute_script("window.scrollBy(0, 30);")   
                time.sleep(0.3)

                time.sleep(1)  # espera a aba carregar

                # Fecha a aba (Ctrl + W)
                pyautogui.hotkey('ctrl', 'w')
                print('Aba fechada')    

            time.sleep(1)

            driver1.execute_script("window.scrollBy(0, 30);")
            time.sleep(0.3)
            driver1.execute_script("window.scrollBy(0, 30);")
            time.sleep(0.3)
            driver1.execute_script("window.scrollBy(0, 30);")
            time.sleep(0.3)
            driver1.execute_script("window.scrollBy(0, 30);")
            time.sleep(0.3)
            driver1.execute_script("window.scrollBy(0, 30);")
            time.sleep(0.3)
            driver1.execute_script("window.scrollBy(0, 30);")   
            time.sleep(0.3)
            driver1.execute_script("window.scrollBy(0, 30);")   
            time.sleep(0.3)
            driver1.execute_script("window.scrollBy(0, 30);")
            time.sleep(0.3)
            driver1.execute_script("window.scrollBy(0, 30);")
            time.sleep(0.3)
            driver1.execute_script("window.scrollBy(0, 30);")   
            time.sleep(0.3)
            driver1.execute_script("window.scrollBy(0, 30);")   
            time.sleep(0.3)
            driver1.execute_script("window.scrollBy(0, 30);")
            time.sleep(0.3)
            driver1.execute_script("window.scrollBy(0, 30);")
            time.sleep(0.3)
            driver1.execute_script("window.scrollBy(0, 30);")   
            time.sleep(0.3)
            driver1.execute_script("window.scrollBy(0, 30);")   
            time.sleep(0.3)

            time.sleep(1)
            driver1.quit()
            continue

        except Exception as e:
            print(e)  
    except Exception as e:
            print(e)          