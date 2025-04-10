
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

    def bot1():
      while True:
        try:
          driver1 = webdriver.Chrome(seleniumwire_options=options1, options=chrome_options)
          driver1.set_window_size(400, 500)
          driver1.set_window_position(0, 0)
          driver1.get("https://www.facebook.com/61566807274239/posts/122147574176560242/")
          wait = WebDriverWait(driver1, 15)

          #fechar modal
          try:
            fechar_modal = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@aria-label="Fechar"]')))
            fechar_modal.click()
            print("Modal de login fechado.")
          except:
            print("Nenhum modal de login visível.")
            driver1.quit()
            continue
          
          #click saiba mais 
          try:
            # Espera o botão ser clicável
            saiba_mais = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="screen-root"]/div/div[3]/div[2]/div/div[3]/div/div[3]/div/div[4]/div')))

            # Clica com Selenium (mais estável)
            saiba_mais.click()
            print("Botão 'Saiba mais' clicado.")
          except:
            print("Nenhum botão 'saiba mais' vizivel ")
            driver1.quit()
            continue
          
          time.sleep(5)
          
          #click anuncio
          try:
            clica_anuncio = random.randint(1,3)
            time.sleep(1)
            print(clica_anuncio)
            if clica_anuncio == 1:
              print('anuncio sendo clicado')

              time.sleep(1)      
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
              time.sleep(0.5)
              
              # Move o mouse e clica
              for _ in range(15):
                # Move para o centro inicialmente (como se fosse um "reset")
                pyautogui.moveTo(center_x, center_y, duration=0.1)
                time.sleep(0.5)
                # Move o mouse aleatoriamente próximo ao centro e clica
                pyautogui.moveTo(
                    center_x + random.randint(-100, 100),
                    center_y + random.randint(1, 10),
                    duration=0.1
                )
                pyautogui.click()
                time.sleep(0.2)
                print('Clicou anuncio')

              time.sleep(10)  

              for _ in range(5):
                driver1.execute_script("window.scrollBy(0, 30);")
                time.sleep(0.3)

              time.sleep(1)  # espera a aba carregar
              # Fecha a aba (Ctrl + W)
              pyautogui.hotkey('ctrl', 'w')
              print('Aba fechada')    

            time.sleep(1)

            for _ in range(15):
              driver1.execute_script("window.scrollBy(0, 30);")
              time.sleep(0.3)

            time.sleep(1)
            driver1.quit()
            continue
          except:
            print("Nenhum anuncio visível.")
            driver1.quit()
            continue
        
        except:
          print('error')
          driver1.quit()

        print('reiniciando bot 1')
        driver1.quit()
          
        


    def bot2():
      while True:
        try:
          driver2 = webdriver.Chrome(seleniumwire_options=options2, options=chrome_options)
          driver2.set_window_size(400, 500)
          driver2.set_window_position(500, 0)
          driver2.get("https://www.facebook.com/61566807274239/posts/122147574176560242/")
          wait = WebDriverWait(driver2, 15)

          #fechar modal
          try:
            fechar_modal = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@aria-label="Fechar"]')))
            fechar_modal.click()
            print("Modal de login fechado.")
          except:
            print("Nenhum modal de login visível.")
            driver2.quit()
            continue
          
          #click saiba mais 
          try:
            # Espera o botão ser clicável
            saiba_mais = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="screen-root"]/div/div[3]/div[2]/div/div[3]/div/div[3]/div/div[4]/div')))

            # Clica com Selenium (mais estável)
            saiba_mais.click()
            print("Botão 'Saiba mais' clicado.")
          except:
            print("Nenhum botão 'saiba mais' vizivel ")
            driver2.quit()
            continue
          
          time.sleep(5)
          
          #click anuncio
          try:
            clica_anuncio = random.randint(1,3)
            time.sleep(1)
            print(clica_anuncio)
            if clica_anuncio == 1:
              print('anuncio sendo clicado')

              time.sleep(1)      
              pos = driver2.get_window_position()
              x = pos['x']
              y = pos['y']

              # Pega o tamanho da janela do driver
              size = driver2.get_window_size()
              width = size['width']
              height = size['height']

              # Calcula o centro da janela
              center_x = x + width // 2
              center_y = y + height // 2

              # Move o mouse até o centro da janela com animação
              print('movendo')
              pyautogui.moveTo(center_x, center_y, duration=0.3)
              time.sleep(0.5)
              
              # Move o mouse e clica
              for _ in range(15):
                # Move para o centro inicialmente (como se fosse um "reset")
                pyautogui.moveTo(center_x, center_y, duration=0.1)
                time.sleep(0.5)
                # Move o mouse aleatoriamente próximo ao centro e clica
                pyautogui.moveTo(
                    center_x + random.randint(-100, 100),
                    center_y + random.randint(1, 10),
                    duration=0.1
                )
                pyautogui.click()
                time.sleep(0.2)
                print('Clicou anuncio')

              time.sleep(10)  

              for _ in range(5):
                driver2.execute_script("window.scrollBy(0, 30);")
                time.sleep(0.3)

              time.sleep(1)  # espera a aba carregar
              # Fecha a aba (Ctrl + W)
              pyautogui.hotkey('ctrl', 'w')
              print('Aba fechada')    

            time.sleep(1)

            for _ in range(15):
              driver2.execute_script("window.scrollBy(0, 30);")
              time.sleep(0.3)

            time.sleep(1)
            driver2.quit()
            continue
          except:
            print("Nenhum anuncio visível.")
            driver2.quit()
            continue
        
        except:
          print('error')
          driver2.quit()

        print('reiniciando bot 1')
        driver2.quit()

    def bot3():  
      while True:
        try:
          driver3 = webdriver.Chrome(seleniumwire_options=options3, options=chrome_options)
          driver3.set_window_size(400, 500)
          driver3.set_window_position(1000, 0)
          driver3.get("https://www.facebook.com/61566807274239/posts/122147574176560242/")
          wait = WebDriverWait(driver3, 15)

          #fechar modal
          try:
            fechar_modal = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@aria-label="Fechar"]')))
            fechar_modal.click()
            print("Modal de login fechado.")
          except:
            print("Nenhum modal de login visível.")
            driver3.quit()
            continue
          
          #click saiba mais 
          try:
            # Espera o botão ser clicável
            saiba_mais = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="screen-root"]/div/div[3]/div[2]/div/div[3]/div/div[3]/div/div[4]/div')))

            # Clica com Selenium (mais estável)
            saiba_mais.click()
            print("Botão 'Saiba mais' clicado.")
          except:
            print("Nenhum botão 'saiba mais' vizivel ")
            driver3.quit()
            continue
          
          time.sleep(5)
          
          #click anuncio
          try:
            clica_anuncio = random.randint(1,3)
            time.sleep(1)
            print(clica_anuncio)
            if clica_anuncio == 1:
              print('anuncio sendo clicado')

              time.sleep(1)      
              pos = driver3.get_window_position()
              x = pos['x']
              y = pos['y']

              # Pega o tamanho da janela do driver
              size = driver3.get_window_size()
              width = size['width']
              height = size['height']

              # Calcula o centro da janela
              center_x = x + width // 2
              center_y = y + height // 2

              # Move o mouse até o centro da janela com animação
              print('movendo')
              pyautogui.moveTo(center_x, center_y, duration=0.3)
              time.sleep(0.5)
              
              # Move o mouse e clica
              for _ in range(15):
                # Move para o centro inicialmente (como se fosse um "reset")
                pyautogui.moveTo(center_x, center_y, duration=0.1)
                time.sleep(0.5)
                # Move o mouse aleatoriamente próximo ao centro e clica
                pyautogui.moveTo(
                    center_x + random.randint(-100, 100),
                    center_y + random.randint(1, 10),
                    duration=0.1
                )
                pyautogui.click()
                time.sleep(0.2)
                print('Clicou anuncio')

              time.sleep(10)  

              for _ in range(5):
                driver3.execute_script("window.scrollBy(0, 30);")
                time.sleep(0.3)

              time.sleep(1)  # espera a aba carregar
              # Fecha a aba (Ctrl + W)
              pyautogui.hotkey('ctrl', 'w')
              print('Aba fechada')    

            time.sleep(1)

            for _ in range(15):
              driver3.execute_script("window.scrollBy(0, 30);")
              time.sleep(0.3)

            time.sleep(1)
            driver3.quit()
            continue
          except:
            print("Nenhum anuncio visível.")
            driver3.quit()
            continue
        
        except:
          print('error')
          driver3.quit()

        print('reiniciando bot 1')
        driver3.quit()

    def bot4():  
      while True:
        try:
          driver4 = webdriver.Chrome(seleniumwire_options=options4, options=chrome_options)
          driver4.set_window_size(400, 500)
          driver4.set_window_position(0, 500)
          driver4.get("https://www.facebook.com/61566807274239/posts/122147574176560242/")
          wait = WebDriverWait(driver4, 15)

          #fechar modal
          try:
            fechar_modal = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@aria-label="Fechar"]')))
            fechar_modal.click()
            print("Modal de login fechado.")
          except:
            print("Nenhum modal de login visível.")
            driver4.quit()
            continue
          
          #click saiba mais 
          try:
            # Espera o botão ser clicável
            saiba_mais = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="screen-root"]/div/div[3]/div[2]/div/div[3]/div/div[3]/div/div[4]/div')))

            # Clica com Selenium (mais estável)
            saiba_mais.click()
            print("Botão 'Saiba mais' clicado.")
          except:
            print("Nenhum botão 'saiba mais' vizivel ")
            driver4.quit()
            continue
          
          time.sleep(5)
          
          #click anuncio
          try:
            clica_anuncio = random.randint(1,3)
            time.sleep(1)
            print(clica_anuncio)
            if clica_anuncio == 1:
              print('anuncio sendo clicado')

              time.sleep(1)      
              pos = driver4.get_window_position()
              x = pos['x']
              y = pos['y']

              # Pega o tamanho da janela do driver
              size = driver4.get_window_size()
              width = size['width']
              height = size['height']

              # Calcula o centro da janela
              center_x = x + width // 2
              center_y = y + height // 2

              # Move o mouse até o centro da janela com animação
              print('movendo')
              pyautogui.moveTo(center_x, center_y, duration=0.3)
              time.sleep(0.5)
              
              # Move o mouse e clica
              for _ in range(15):
                # Move para o centro inicialmente (como se fosse um "reset")
                pyautogui.moveTo(center_x, center_y, duration=0.1)
                time.sleep(0.5)
                # Move o mouse aleatoriamente próximo ao centro e clica
                pyautogui.moveTo(
                    center_x + random.randint(-100, 100),
                    center_y + random.randint(1, 10),
                    duration=0.1
                )
                pyautogui.click()
                time.sleep(0.2)
                print('Clicou anuncio')

              time.sleep(10)  

              for _ in range(5):
                driver4.execute_script("window.scrollBy(0, 30);")
                time.sleep(0.3)

              time.sleep(1)  # espera a aba carregar
              # Fecha a aba (Ctrl + W)
              pyautogui.hotkey('ctrl', 'w')
              print('Aba fechada')    

            time.sleep(1)

            for _ in range(15):
              driver4.execute_script("window.scrollBy(0, 30);")
              time.sleep(0.3)

            time.sleep(1)
            driver4.quit()
            continue
          except:
            print("Nenhum anuncio visível.")
            driver4.quit()
            continue
        
        except:
          print('error')
          driver4.quit()

        print('reiniciando bot 1')
        driver4.quit()

    def bot5(): 
      while True:
        try: 
          driver5 = webdriver.Chrome(seleniumwire_options=options5, options=chrome_options)
          driver5.set_window_size(400, 500)
          driver5.set_window_position(500, 500)
          driver5.get("https://www.facebook.com/61566807274239/posts/122147574176560242/")
          wait = WebDriverWait(driver5, 15)

          #fechar modal
          try:
            fechar_modal = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@aria-label="Fechar"]')))
            fechar_modal.click()
            print("Modal de login fechado.")
          except:
            print("Nenhum modal de login visível.")
            driver5.quit()
            continue
          
          #click saiba mais 
          try:
            # Espera o botão ser clicável
            saiba_mais = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="screen-root"]/div/div[3]/div[2]/div/div[3]/div/div[3]/div/div[4]/div')))

            # Clica com Selenium (mais estável)
            saiba_mais.click()
            print("Botão 'Saiba mais' clicado.")
          except:
            print("Nenhum botão 'saiba mais' vizivel ")
            driver5.quit()
            continue
          
          time.sleep(5)
          
          #click anuncio
          try:
            clica_anuncio = random.randint(1,3)
            time.sleep(1)
            print(clica_anuncio)
            if clica_anuncio == 1:
              print('anuncio sendo clicado')

              time.sleep(1)      
              pos = driver5.get_window_position()
              x = pos['x']
              y = pos['y']

              # Pega o tamanho da janela do driver
              size = driver5.get_window_size()
              width = size['width']
              height = size['height']

              # Calcula o centro da janela
              center_x = x + width // 2
              center_y = y + height // 2

              # Move o mouse até o centro da janela com animação
              print('movendo')
              pyautogui.moveTo(center_x, center_y, duration=0.3)
              time.sleep(0.5)
              
              # Move o mouse e clica
              for _ in range(15):
                # Move para o centro inicialmente (como se fosse um "reset")
                pyautogui.moveTo(center_x, center_y, duration=0.1)
                time.sleep(0.5)
                # Move o mouse aleatoriamente próximo ao centro e clica
                pyautogui.moveTo(
                    center_x + random.randint(-100, 100),
                    center_y + random.randint(1, 10),
                    duration=0.1
                )
                pyautogui.click()
                time.sleep(0.2)
                print('Clicou anuncio')

              time.sleep(10)  

              for _ in range(5):
                driver5.execute_script("window.scrollBy(0, 30);")
                time.sleep(0.3)

              time.sleep(1)  # espera a aba carregar
              # Fecha a aba (Ctrl + W)
              pyautogui.hotkey('ctrl', 'w')
              print('Aba fechada')    

            time.sleep(1)

            for _ in range(15):
              driver5.execute_script("window.scrollBy(0, 30);")
              time.sleep(0.3)

            time.sleep(1)
            driver5.quit()
            continue
          except:
            print("Nenhum anuncio visível.")
            driver5.quit()
            continue
        
        except:
          print('error')
          driver5.quit()

        print('reiniciando bot 1')
        driver5.quit()

    def bot6():  
      while True:
        try: 
          driver6 = webdriver.Chrome(seleniumwire_options=options6, options=chrome_options)
          driver6.set_window_size(400, 500)
          driver6.set_window_position(1000, 500)
          driver6.get("https://www.facebook.com/61566807274239/posts/122147574176560242/")
          wait = WebDriverWait(driver6, 15)

          #fechar modal
          try:
            fechar_modal = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@aria-label="Fechar"]')))
            fechar_modal.click()
            print("Modal de login fechado.")
          except:
            print("Nenhum modal de login visível.")
            driver6.quit()
            continue
          
          #click saiba mais 
          try:
            # Espera o botão ser clicável
            saiba_mais = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="screen-root"]/div/div[3]/div[2]/div/div[3]/div/div[3]/div/div[4]/div')))

            # Clica com Selenium (mais estável)
            saiba_mais.click()
            print("Botão 'Saiba mais' clicado.")
          except:
            print("Nenhum botão 'saiba mais' vizivel ")
            driver6.quit()
            continue
          
          time.sleep(5)
          
          #click anuncio
          try:
            clica_anuncio = random.randint(1,3)
            time.sleep(1)
            print(clica_anuncio)
            if clica_anuncio == 1:
              print('anuncio sendo clicado')

              time.sleep(1)      
              pos = driver6.get_window_position()
              x = pos['x']
              y = pos['y']

              # Pega o tamanho da janela do driver
              size = driver6.get_window_size()
              width = size['width']
              height = size['height']

              # Calcula o centro da janela
              center_x = x + width // 2
              center_y = y + height // 2

              # Move o mouse até o centro da janela com animação
              print('movendo')
              pyautogui.moveTo(center_x, center_y, duration=0.3)
              time.sleep(0.5)
              
              # Move o mouse e clica
              for _ in range(15):
                # Move para o centro inicialmente (como se fosse um "reset")
                pyautogui.moveTo(center_x, center_y, duration=0.1)
                time.sleep(0.5)
                # Move o mouse aleatoriamente próximo ao centro e clica
                pyautogui.moveTo(
                    center_x + random.randint(-100, 100),
                    center_y + random.randint(1, 10),
                    duration=0.1
                )
                pyautogui.click()
                time.sleep(0.2)
                print('Clicou anuncio')

              time.sleep(10)  

              for _ in range(5):
                driver6.execute_script("window.scrollBy(0, 30);")
                time.sleep(0.3)

              time.sleep(1)  # espera a aba carregar
              # Fecha a aba (Ctrl + W)
              pyautogui.hotkey('ctrl', 'w')
              print('Aba fechada')    

            time.sleep(1)

            for _ in range(15):
              driver6.execute_script("window.scrollBy(0, 30);")
              time.sleep(0.3)

            time.sleep(1)
            driver6.quit()
            continue
          except:
            print("Nenhum anuncio visível.")
            driver6.quit()
            continue
        
        except:
          print('error')
          driver6.quit()

        print('reiniciando bot 1')
        driver6.quit()

  
    t1 = threading.Thread(target=bot1)
    t2 = threading.Thread(target=bot2)
    t3 = threading.Thread(target=bot3)
    t4 = threading.Thread(target=bot4)
    t5 = threading.Thread(target=bot5)
    t6 = threading.Thread(target=bot6)

    # Iniciando as threads
    t1.start()
    time.sleep(1)
    t2.start()
    time.sleep(1)
    t3.start()
    time.sleep(1)
    t4.start()
    time.sleep(1)
    t5.start()
    time.sleep(1)
    t6.start()

    # Esperando todas terminarem
    t1.join()
    time.sleep(1)
    t2.join()
    time.sleep(1)
    t3.join()
    time.sleep(1)
    t4.join()
    time.sleep(1)
    t5.join()
    time.sleep(1)
    t6.join()

  except Exception as e:
      print(e)  