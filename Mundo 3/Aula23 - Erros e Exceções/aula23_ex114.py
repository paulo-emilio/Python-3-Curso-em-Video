import urllib
import urllib.request
from time import sleep

try:
    site = urllib.request.urlopen('https://www.google.com/')
except:
    print('\033[31mNão deu :(\033[m')
else:
    print('\033[36mAcessei!\033[m')
    print('\033[35mLENDO O SITE:\033[m')
    sleep(1)
    print('.', end='')
    sleep(1)
    print('.', end='')
    sleep(1)
    print('.')
    sleep(1)
    print(site.read())
