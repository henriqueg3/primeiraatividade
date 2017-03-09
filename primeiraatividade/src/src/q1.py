'''
Created on 9 de mar de 2017

@author: Henrique Garrida
'''

from math import log

number = int(input("tamanho da menssagem?"))

bits = int(log(number, 2) + 1)

print("quantidade de bits = (0)", format(bits))