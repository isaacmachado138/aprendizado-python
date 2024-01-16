#  Módulo 2: Conceitos Básicos

# Neste módulo, exploraremos alguns conceitos básicos em Python, incluindo variáveis,
# tipos de dados, operadores e estruturas de controle de fluxo.
# todos esses conceitos são simples e semelhantes ao que acontece em outras linguagens de programação

# Exemplo 1: Variáveis e Tipos de Dados
nome = "Alice"
idade = 25
altura = 1.75
is_estudante = True

# Exemplo 2: Operadores
soma = idade + 5
multiplicacao = altura * 2

# Exemplo 3: Estruturas de Controle de Fluxo
if is_estudante:
    print(f"{nome} é um estudante.")
else:
    print(f"{nome} não é um estudante.")

"""# **EXERCICIOS FOR**

1 - Digitar uma string e verificar quantos caracteres ela tem sem usar o len e nem contar espaços
"""

string = input("Digite um texto: ")

contador = 0
for i in string:
  if i != ' ':
    contador += 1

print("Essa string tem %i caracteres" % contador)

"""2 - Receber um numero e contar fatorial dele"""

num = int(input("Digite um numero: "))
res = num

for i in range(num-1,0,-1):
  resAnt = res
  res *= i

  print("%i * %i = %i" % (resAnt,i, res))

print("O resultado do fatorial de %i é %i" % (num,res))

"""3 - Ler quantidade arbitraria de textos e concatenar numa unica string"""

iNum = int(input("Digite o numero de leituras: "))

sTextoFinal = ""
for i in range(iNum):
  sTextoFinal += input("Digite uma string: ")

print("O texto concatenado é %s " % sTextoFinal)

"""4 - Ler um numero e exibir sua tabuada da divisão"""

iNum = int(input("Digite um numero: "))

res = 0.0

#para percorrer de 1 a 10
for i in range(1,11):
  res = iNum / i
  print("%i / %i = %.1f" % (iNum, i, res))

"""5 - Percorrer numeros de 3 até 30 e printar se o número é primo ou não"""

#para percorrer de 3 ate 30
for i in range(3,31):
  ePrimo = True

  for c in range(2,i):
    if(i % c == 0):
      ePrimo = False
      break

  if(ePrimo):
    print("%i é primo" % i)
  else:
    print("%i não é primo" % i)

