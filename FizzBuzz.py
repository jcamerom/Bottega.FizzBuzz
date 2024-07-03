"""
FIZZBUZZ. Programa de entrega de Bottega-DevCamp.

Este programa escrito en Python imprimirá los números del 1 al número que le cedamos, con los siguientes criterios:

Si el número es divisible por 3, imprime "Fizz" en lugar del número.
Si el número es divisible por 5, imprime "Buzz" en lugar del número.
Si el número es divisible por 3 y 5, imprime "FizzBuzz" en lugar del número.
Este desafío de programación clásico se llama FizzBuzz y es común en entrevistas técnicas 

"""

def fizzBuzz(max_num):
	for num in range(1, max_num + 1):
		if num % 3 == 0 and num % 5 == 0:
		  print('FizzBuzz')
		elif num % 5 == 0:
		  print('Buzz')
		elif num % 3 == 0:
		  print('Fizz')
		else:
		  print(num)
	
	
fizzBuzz(100)