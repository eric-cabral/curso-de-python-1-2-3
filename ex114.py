import urllib.request

try:
    site = urllib.request.urlopen("http://pudim.com.br/")
except:
    print('\033[1;30;41mO site está inacessível no momento : (\033[m')
else:
    print('\033[1;33mO site está acessível no momento : )\033[m')
