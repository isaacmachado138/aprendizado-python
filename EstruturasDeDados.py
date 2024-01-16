#  Módulo 3: Estruturas de dados

"""# **LISTAS**

## Manipulando (aula 70)
"""

array = [10, 2, 3]

#insere um novo valor ao final da lista
array.append(2)
print("Array com o 2 inserido ao final: %s \n" % array)

#insere um novo valor em determinada posição
array.insert(2, "quatro")
print("Array com o \'quatro\' inserido na posição 2: %s \n" % array)

#remove um valor pelo seu valor
array.remove(10)
print("Array com o 10 removido: %s \n" % array)

#remove um valor pelo seu indice
array.pop(2)
print("Array com o 2 indice removido: %s \n" % array)

#função len lê o comprimento do array
print("Comprimento do array: %i \n" % len(array))

#clear limpa o array
array.clear()
print("Array limpo: %s \n" % array)

#Testar se elemento esta no array
array = [1, 'teste', 2.3, False, 1]
print("1 está no array?: %s \n" % (1 in array))

print("False não está no array?: %s \n" % (False not in array))

#Contar quantas vezes ocorre um va,lor no array
teste = array.count(1)
print("1 está no array quantas vezes?: %i \n" % teste)



"""## Operações (soma, mult e distribuição)"""

lista1 = [1,2,3]
lista2 = [3,4,5]

#somar arrays
soma   = lista1 + lista2
print("Arrays somados: %s \n" % soma)

#somar arrays
mult   = lista1 * 3
print("Array 1 repetido 3 vezes: %s \n" % mult)

#atribuir cada elemento a uma variável
numeros = ["um", "dois", "três"]
x,y,z = numeros
print("Variável x: %s " % x)
print("Variável y: %s " % y)
print("Variável z: %s " % z)

"""##Percorrer"""

cores = ["azul", "preto", "amarelo"]

for x in cores:
  print(x)

"""##Matriz (lista com listas)"""

lista = [[1,2,3] , [3,4,5]]

lista1 = lista[0]
lista2 = lista[1]

print("Primeira lista: %s" % lista1)
print("Segunda  lista: %s \n" % lista2)

primeiro_elemento_primeira_lista = lista[0][0]
print("Primeiro elemento da primeira lista: %s" % primeiro_elemento_primeira_lista)

"""## Set"""

lista_set  = {}
lista2_set = {1, 2, 3}
lista3_set = set({4,5, 6})

lista2_set.add(5)    #adiciona um valor ao set
lista2_set.remove(1) #remove um valor do set
print(lista_set)
print(lista2_set)
print(lista3_set)

lista_union = lista2_set.union(lista3_set)
print("\n União = %s \n" % lista_union)

lista_intersection = lista2_set.intersection(lista3_set)
print("\n Interseção = %s \n" % lista_intersection)

lista_dif = lista2_set.difference(lista3_set)
print("\n Diferença = %s \n" % lista_dif)

c = 0
for i in lista3_set:
  print(" Elemento posição %i = %s " % (c, i))
  c+= 1

"""##Tuple
tipo de lista que não pode ser modificada, nº fixo de elementos, e tem uma ordem definida
"""

doces = (("chocolate", "bom bom", "paçoca", "confete", "brigadeiro"))
print(doces)
print("posição 2: %s" % doces[2])
sub_tupla = doces[1:3]
print(sub_tupla)

"""##Dictionaries
lista que o indice e o valor sao definidos, formado por um conjunto chave/valor
"""

#nesse caso, ana tem 10 anos, isaac 20 e etc
idades = {'ana':10 , 'isaac': 20 , 'joão':34 , 'fernando':'indefinido'}
#print(idades)
print("Idade de Isaac %s" % idades['isaac'])

#metodo get
idades.get('joão')

#atualizar, ambos os metodos abaixo servem para atualizar um registro
idades['ana'] = 47
idades.update({'fernando':55})
#print(idades)

#remover
idades.pop('fernando')

idades.popitem() #remove o ultimo item

#adicionar
idades['marcos'] = 22 #adiciona ao final

#limpar
idades.clear()

"""Populando lista com for"""

lista = [x for x in range(0,10)]
print(lista)

lista = [x for x in range(-10,20) if x < 10 if x > -5]
print(lista)

"""## Exercícios

Criando uma lista com os numeros 1,10,6,7,8,10 e somando esses numeros
"""

aList = [1,10,6,7,8,10]

soma = 0

for i in aList:
  soma += i

print("A soma dos numeros da lista é: %i" % soma)

"""Crie uma lista com numeros de 1 a 100 e printe esses valores"""

aList = [x for x in range(0,100)]

for i in aList:
  print("%i" % i)

"""Crie duas listas com os valores definidos e faça a junção dessas listas, sem valores repetidos"""

aList1 = {30,4,43,52,65,-10}
aList2 = {43,2,4,76,32,65,3}

aListFinal = aList1.union(aList2)

print(aListFinal)

"""Crie uma lista com todos os meses do ano, receba por input o mes que voce nasceu e imprima o nome do mes"""

aMeses = ('Janeiro', 'Fevereiro', 'Março','Abril','Maio','Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')

iMes = int(input('Digite qual número do mês em que voce nasceu: '))

print("Você nasceu no mês %s" % aMeses[iMes-1])