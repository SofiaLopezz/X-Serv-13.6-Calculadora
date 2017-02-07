#!-/usr/bin/python3
# -*- coding: utf-8 -*-

#Calculadora 13.6

import sys

comandos  = sys.argv

if len(comandos) != 4:
	sys.exit("Comandos inválidos")

_, operador, num1, num2 = sys.argv

num1 = int(num1)
num2 = int(num2)

if operador == 'suma':
	resultado=num1+num2

elif operador == 'resta':
	resultado=num1-num2

elif operador == 'multiplica':
	resultado=num1*num2
	
elif operador == 'dividir':
	try:	
		resultado=num1/num2
	except ZeroDivisionError:
		print("Infinito")

print(resultado)

