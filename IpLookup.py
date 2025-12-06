import os
import time
import json
import requests
import colorama
import sys

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
