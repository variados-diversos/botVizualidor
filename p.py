import threading
import time
import random
import shutil
import tempfile
import platform
import zipfile
import pyautogui

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Lock para controlar acesso ao mouse
mouse_lock = threading.Lock()

# Lista de proxies diferentes para 4 janelas
proxies = [
    ("na.wq08cilx.lunaproxy.net", 12233, "user-jungjunior25_P2mgO", "Resgate27"),
    ("na.wq08cilx.lunaproxy.net", 12233, "jungrogerio_S5uwF", "Resgate27"),
    ("na.wq08cilx.lunaproxy.net", 12233, "user-rogeriojung_A0isB", "Resgate27"),
    ("na.wq08cilx.lunaproxy.net", 12233, "user-juniorjung_N3nzV", "Resgate27"),
]

def criar_extensao_proxy(proxy_host, proxy_port, proxy_user, proxy_pass):
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

    chrome.proxy.settings.set({{value: config, scope: "regular"}}, function(){{}});

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

    plugin_path = tempfile.mktemp(suffix=".zip")
    with zipfile.ZipFile(plugin_path, 'w') as zp:
        zp.writestr("manifest.json", manifest_json)
        zp.writestr("background.js", background_js)

    return plugin_path

def navegador_loop(proxy_data, index):
    proxy_host, proxy_port, proxy_user, proxy_pass = proxy_data

    while True:
        user_data_dir = tempfile.mkdtemp()
        extension_path = criar_extensao_proxy(proxy_host, proxy_port, proxy_user, proxy_pass)

        chrome_options = Options()
        chrome_options.add_extension(extension_path)
        chrome_options.add_argument(f"--user-data-dir={user_data_dir}")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")

        # Emula mobile com chance de 66%
        if random.randint(1, 3) != 1:
            mobile_emulation = {"deviceName": "iPhone X"}
            chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

        driver = webdriver.Chrome(options=chrome_options)
        driver.set_window_size(400, 800)

        try:
            driver.get("https://www.facebook.com/61566807274239/posts/122147574176560242/")
            wait = WebDriverWait(driver, 15)

            try:
                modal = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@aria-label="Fechar"]')))
                modal.click()
            except:
                pass

            time.sleep(2)

            try:
                saiba_mais = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="screen-root"]/div/div[3]/div[2]/div/div[3]/div/div[3]/div/div[4]/div')))
                location = saiba_mais.location
                size = saiba_mais.size
                x = location['x'] + size['width'] // 2
                y = location['y'] + size['height'] // 2

                with mouse_lock:
                    pyautogui.moveTo(x, y, duration=1)
                    time.sleep(0.5)
                    saiba_mais.click()
                    print(f"[Bot-{index}] Clicou em 'Saiba mais'")

            except Exception as e:
                print(f"[Bot-{index}] Erro no clique: {e}")
                driver.quit()
                shutil.rmtree(user_data_dir)
                continue

            time.sleep(3)
            if len(driver.window_handles) > 1:
                driver.switch_to.window(driver.window_handles[-1])

            wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

            for _ in range(15):
                driver.execute_script("window.scrollBy(0, 100);")
                time.sleep(0.3)

            if random.randint(1, 3) == 1:
                abas_iniciais = set(driver.window_handles)

                for _ in range(15):
                    if set(driver.window_handles) - abas_iniciais:
                        break
                    driver.execute_script(f"window.scrollBy(0, -{random.randint(50, 300)});")
                    time.sleep(0.5)

                    x = random.randint(100, 300)
                    y = random.randint(200, 600)
                    with mouse_lock:
                        pyautogui.moveTo(x, y, duration=0.3)
                        pyautogui.click()

                time.sleep(random.randint(3, 8))
                with mouse_lock:
                    if platform.system() == "Darwin":
                        pyautogui.hotkey('command', 'w')
                    else:
                        pyautogui.hotkey('ctrl', 'w')

            time.sleep(2)

        except Exception as e:
            print(f"[Bot-{index}] Erro geral: {e}")

        finally:
            driver.quit()
            shutil.rmtree(user_data_dir)
            print(f"[Bot-{index}] Reiniciando...")

def main():
    threads = []
    for i in range(4):
        t = threading.Thread(target=navegador_loop, args=(proxies[i], i + 1))
        t.start()
        threads.append(t)
        time.sleep(1)  # evitar sobrecarga inicial

    for t in threads:
        t.join()

if __name__ == "__main__":
    main()
