from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui
import random
import time
import platform
from http_request_randomizer.requests.proxy.requestProxy import RequestProxy
import zipfile
import tempfile
import shutil

# Cria uma pasta temporária
user_data_dir = tempfile.mkdtemp()

while True:
    # Suas credenciais Luna Proxy
    proxy_host = "na.wq08cilx.lunaproxy.net"
    proxy_port = 12233
    proxy_user = "user-jungjunior25_P2mgO"
    proxy_pass = "Resgate27"

    # Cria os arquivos da extensão
    plugin_path = 'luna_proxy_auth_plugin.zip'

    manifest_json = """
    {
        "version": "1.0.0",
        "manifest_version": 2,
        "name": "Luna Proxy Auth Extension",
        "permissions": [
            "proxy",
            "tabs",
            "unlimitedStorage",
            "storage",
            "<all_urls>",
            "webRequest",
            "webRequestBlocking"
        ],
        "background": {
            "scripts": ["background.js"]
        }
    }
    """

    background_js = f"""
    var config = {{
            mode: "fixed_servers",
            rules: {{
            singleProxy: {{
                scheme: "http",
                host: "{proxy_host}",
                port: parseInt({proxy_port})
            }},
            bypassList: ["localhost"]
            }}
        }};

    chrome.proxy.settings.set({{value: config, scope: "regular"}}, function() {{}});

    function callbackFn(details) {{
        return {{
            authCredentials: {{
                username: "{proxy_user}",
                password: "{proxy_pass}"
            }}
        }};
    }}

    chrome.webRequest.onAuthRequired.addListener(
        callbackFn,
        {{urls: ["<all_urls>"]}},
        ['blocking']
    );
    """

    # Cria o arquivo zip da extensão
    with zipfile.ZipFile(plugin_path, 'w') as zp:
        zp.writestr("manifest.json", manifest_json)
        zp.writestr("background.js", background_js)


    # Configura o Chrome com a extensão
    chrome_options = Options()
    chrome_options.add_extension(plugin_path)
    chrome_options.add_argument(f"--user-data-dir={user_data_dir}")
    # (opcional) emulação de mobile
    disposivito = random.randint(1, 3)

    if disposivito != 1:
        mobile_emulation = {"deviceName": "iPhone X"}
        chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

    # Inicia o driver
    driver = webdriver.Chrome(options=chrome_options)  
    driver.set_window_size(400, 800)

    # Access the post URL
    driver.get("https://www.facebook.com/61566807274239/posts/122147574176560242/")

    wait = WebDriverWait(driver, 15)
    # Tenta fechar modal de login (se aparecer)
    try:
        fechar_modal = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@aria-label="Fechar"]')))
        fechar_modal.click()
        print("Modal de login fechado.")
    except:
        print("Nenhum modal de login visível.")
        driver.quit()
        shutil.rmtree(user_data_dir)
        continue  # reinicia o while True
        

    time.sleep(2)


    #bt saiba mais
    try:
        # Espera o botão ser clicável
        saiba_mais = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="screen-root"]/div/div[3]/div[2]/div/div[3]/div/div[3]/div/div[4]/div')))

        # Obtém posição do botão (já está visível)
        location = saiba_mais.location
        size = saiba_mais.size

        # Calcula centro do botão
        x = location['x'] + size['width'] // 2
        y = location['y'] + size['height'] // 2

        # Move o mouse até o centro do botão
        pyautogui.moveTo(x, y, duration=1)
        time.sleep(1)

        # Clica com Selenium (mais estável)
        saiba_mais.click()
        print("Botão 'Saiba mais' clicado.")

    except Exception as e:
        print("Botão 'Saiba mais' não encontrado.")
        driver.quit()
        shutil.rmtree(user_data_dir)
        continue  # reinicia o while True

    # Aguarda a nova aba abrir
    time.sleep(3)
    abas = driver.window_handles
    if len(abas) > 1:
        driver.switch_to.window(abas[-1])  # Foca na nova aba
        print("Mudou para nova aba:", driver.current_url)

    # Aguarda o carregamento da nova página
    try:
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        print("Nova página carregada.")
    except:
        print("Timeout ao carregar nova aba.")


    # Faz scroll na página
    for _ in range(15):
        if driver.window_handles:
            driver.execute_script("window.scrollBy(0, 100);")  # scroll para baixo
        time.sleep(0.5)


    # Salva abas antes dos cliques aleatórios
    abas_antes = set(driver.window_handles)

    clica = random.randint(1,3)
    print
    if clica == 1:
        
        # Scroll para cima + clique aleatório por 8 vezes
        for _ in range(15):
            abas_atuais = set(driver.window_handles)
            if len(abas_atuais - abas_antes) > 0:
                print("Nova aba detectada! Interrompendo cliques aleatórios.")
                break
            # Scroll para cima
            scroll_amount = random.randint(50, 300)
            if driver.window_handles:
                driver.execute_script(f"window.scrollBy(0, -{scroll_amount});")
            time.sleep(0.5)

            # Gera coordenadas aleatórias dentro de um quadrado 100x100
            x = random.randint(100, 300)
            y = random.randint(200, 600)

            # Move o mouse e clica
            pyautogui.moveTo(x, y, duration=0.3)
            pyautogui.click()
            print(f"Clique aleatório em ({x}, {y})")

        # Espera aleatória
        time.sleep(random.randint(3, 8))
        # Fecha aba atual com Ctrl+W ou Command+W
        if platform.system() == "Darwin":
            pyautogui.hotkey('command', 'w')
        else:
            pyautogui.hotkey('ctrl', 'w')
        print("Aba atual fechada.")

    
        for _ in range(5):
            if driver.window_handles:
                driver.execute_script(f"window.scrollBy(0, 100);")  # scroll para baixo
            time.sleep(0.2)

        for _ in range(5):
            if driver.window_handles:
                driver.execute_script(f"window.scrollBy(0, -100);")  # scroll para baixo
            time.sleep(0.2)    
    
    time.sleep(2)
    driver.quit()
    shutil.rmtree(user_data_dir)
