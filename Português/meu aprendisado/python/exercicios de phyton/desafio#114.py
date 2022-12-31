import urllib
import urllib.request
try:
    site = urllib.request.urlopen('http://www.unitel.ao')
except:
    print('O site não esta acessivel no momento')
else:
    print('Consegui acessar o site com sucesso!')
    print(site.read())
