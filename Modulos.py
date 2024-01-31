"""#Módulo 6: MÓDULOS

Módulos são bibliotecas prontas e empacotadas. Podem ter muitas funções já prontas, com funções úteis para ler arquivos, ciência de dados, conectar ao BD, interagir com serviços da núvem, entre outros. Podem ser criados, importados ou instalados
"""

import datetime
data = datetime.datetime(2022,5,15,4,5,33)

print(data)

dir(datetime) #serve para ver funcoes, atributos e classes do modulo

"""A importação também pode ser feita dando uma espécie de alias para o módulo, como:"""

import random as testeModulo

print(testeModulo.randrange(10,100)) #traz um numero aleatorio entre 10 e 100

"""ou importar somente uma função, como:

```
# from random import randrange

```

isso fará com que possa utilizar randrange diretamente

## Instalando um módulo

Comando pip instala o módulo nas dependências
"""

#!pip install pmdarima

"""Do mesmo modo, é possível criar um arquivo .py e importar ele, do mesmo modo que se faz com um módulo já existente

##Listando módulos instalados
 O comando !pip list lista todos os módulos instalados

##Exercicios

1 - Importe um modulo random e a função randrange e crie um programa que gere a soma de 100 números aleatórios e mostre o resultado final
"""

from random import randrange

total = 0
for i in range(0,100,1):
  total += randrange(2,100)

print("O valor total da soma desses numeros é %i" % total)

"""2 - Crie um módulo que dispoe de duas funções, uma que subtrai dois números e uma que soma. Importe essas funções e as use. Gere a documentação dessas funções e mostre na saída de seu programa."""

from modules import CalcPython

print("Segue abaixo documentação do módulo: \n")

help(CalcPython)

print("Segue abaixo documentação da função soma: \n")

print("Valor da chamada teste de soma(8,12): %i" % CalcPython.soma(8,12))


help(CalcPython.soma)

print("Segue abaixo documentação da função subtracao: \n")
help(CalcPython)

print("Valor da chamada teste de subtracao(8,12): %i" % CalcPython.soma(8,12))