import requests

def get_info_by_ip(ip):
    try:
        responsev = requests.get(url=f'http://ipwho.is/{ip}').json()
        return responsev
        # print(responsev)
    except requests.exceptions.ConnectionError:
        return '[!] ~ Error ~ [!]'
        # print('[!] ~ Error ~ [!]')
# get_info_by_ip('127.160.102.91')