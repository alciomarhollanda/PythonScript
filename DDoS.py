import urllib.request
import time


preço = float('99.99')
print(preço)
anterior = preço
while preço >= 3.24:
    pagina = urllib.request.urlopen(
    'http://beans.itcarlow.ie/prices-loyalty.html')
    texto = pagina.read().decode('utf8')
    onde = texto.find('>$')
    inicio = onde + 2
    fim = inicio + 4    
    if(texto[inicio:fim] is not ''):
        preço = float(texto[inicio:fim])
        if preço >= 5.00:
            time.sleep(600)
        if(anterior != preço):
            print('Valor Atual: %s' %texto[inicio:fim])    
        anterior = preço
        
    
print('Comprar! Preço: %5.2f' %preço)
        
