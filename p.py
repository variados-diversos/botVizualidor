import zipfile
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

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

# (opcional) emulação de mobile
mobile_emulation = {"deviceName": "iPhone X"}
chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

# Inicia o driver
driver = webdriver.Chrome(options=chrome_options)

# Testa o IP
driver.get("https://api.ipify.org/?format=json")  # mostra o IP atual

time.sleep(3000)