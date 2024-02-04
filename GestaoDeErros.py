"""#Módulo 7: Gestão de Exeções e Logs

##Logs

Módulo logging, que pode salvar em disco os logs ou mostrar na saída
Criado em uma função separada
"""

from inc import *

print("Exemplo 1 try e catch")
lista = [1,2,3]

try:
  print(lista[6]) #codigo que pode dar erro
except Exception as error:
    Logger('error', str(error))
    #print("ERRO!!! Mensagem: " + str(error)) #executado quando ocorre o erro

else:
  print("Não houve erro!") #quando nao da erro
finally:
  del lista #sempre executado
  print('Fim da execução')

"""**try**: bloco em que pode ocorrer o erro

**except**: caso de erro

**else**: um else do except, para caso nao de erro

**finally**: sempre será executado, com ou sem erro

##Gerar erro
Também é possível gerar um erro, utilizando raise
"""

num = 25
if(10 < num):
  raise("ERRO! Número é maior que 10")

"""##Tipo

Também é possível gerar erro com um tipo...
No exemplo abaixo temos o tratamento para caso o erro seja do tipo ValueError e também um except do tipo Exception, para erros geneéricos
"""

try:
  num = -1

  if(num < 0):
    raise ValueError("Valor não pode ser negativo")
except ValueError as erro:
  print("Value error, erro: " + str(erro))
except Exception as erro:
  print("Erro genérico: " + str(erro))

"""##Assert
Também é possível utilizar assert, a execução só continua se o teste feito em assert for verdadeiro
"""

try:
  num = -1

  assert(num > 0)
except AssertionError as erro:
  print("Value error, erro: " + str(erro))
except Exception as erro:
  print("Erro genérico: " + str(erro))

"""##Atividades

1 - Criar uma função que receba uma lista e um número e retorne o elemento da lista na posição deste número. Faça o tratamento para caso haja um acesso fora do índice a função retorne o valor None
"""

def valorLista(lst, index):
  try:
    return lst[index]
  except IndexError:
    return None

print(valorLista([1,2,3,4,5,6], 5))