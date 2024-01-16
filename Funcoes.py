#  Módulo 4: Funcoes

def ola(nome):
  print('Olá %s' % nome)

ola('Isaac')

"""## Funções Lambda
Funções anônimas, que serão utilizadas apenas uma vez
"""

somar = lambda x,y : x + y

valor = somar(1,5)

print(valor)

"""##Exercícios

Crie uma função que receba uma lista de elementos e um valor qualquer. Em seguida retorne um booleano dizendo se o valor foi ou não encontrado na lista
"""

def busca(lista, valor):
  for i in lista:
    if(i == valor):
      return  True
  return  False



lista = [1,4,6,8,9,12,19]
valor = int(input('Digite um valor para buscar na lista: '))

print(busca(lista, valor))

"""Crie uma função que receba um número arbitrário de parâmetros e diga qual o tipo de cada parametro"""

def mostraTipo(*args):
  for i in args:
    print(type(i))

mostraTipo(1,7,12,'teste', [4,5,6], False);

"""Crie uma função recursiva que itere os numeros de 0 ate 10 e printe o resultado de usa divisão inteira com o número 3"""

def printaDivisao3(num):

  if num >= 11:
    return

  print(num // 3)
  printaDivisao3(num+1)


printaDivisao3(0)

"""# FUNÇÕES PRONTAS

##Abs
Pega o valor absoluto do número
"""

num1 = 10
num2 = -20

print(abs(num1))
print(abs(num2))

print(abs(num1) + abs(num2))

"""##Max e Min
Pega o valor máximo dentre alguns valores ou uma lista
"""

lista = [-20,1,2,5]
print(max(lista))

stringLista = (-20,1,2,5)
print(min(stringLista))

"""##Potência
Eleva um número a outro, exemplo:
2 elevado a 3
"""
