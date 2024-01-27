

"""#Módulo 5: ORIENTAÇÃO A OBJETOS

*   **__init__** : é o construtor da instancia
*   **self**: é a variável da instancia que está sendo utilizada, não precisa ser passada no parâmetro mas precisa ser recebida
*
"""

class Pessoa:
  especie = "Homo Sapiens"
  num_pessoas = 0

  def __init__(self, nome, idade):
    self.nome = nome
    self.idade = idade
    Pessoa.num_pessoas += 1

  def exibeNome(self):
    print("Meu nome é %s " % (self.nome))

pessoa1 = Pessoa('Rodrigo', 34)
pessoa2 = Pessoa('Maria', 20)
pessoa3 = Pessoa('Carlos', 12)

pessoa1.exibeNome()

"""##Herança

no exemplo, as classes Quadrado e Triangulo vao herdar da classe FormaGeometrica

Essa herança pode ser multipla tambem, podendo herdar de mais de uma classe ao mesmo tempo
"""

class FormaGeometrica:
  def __init__(self, altura, largura):
    self.altura  = altura
    self.largura = largura

  def funcaoHerdada(self):
    print("Sou herdado")

class Quadrado(FormaGeometrica):
  pass

class Triangulo(FormaGeometrica):
  pass

quadrado  = Quadrado(100,50)
triangulo = Triangulo(10,30)

print(quadrado.funcaoHerdada())
print(triangulo.altura)
print(triangulo.largura)

"""##Overrided: Sobreposição de funções

se a função é redeclarada na classe filha ela sobrepõe a função da classe pai
"""

class ClassePai:
  def __init__(self):
    print("Sou a classe pai")

class ClasseFilha1(ClassePai):
  def __init__(self):
    print("Sou a classe filha 1")

class ClasseFilha2(ClassePai):
  def __init__(self):
    print("Sou a classe filha 2")

pai = ClassePai()

filha = ClasseFilha1()

"""Porém, as funcionalidades da classePai ainda continuam disponíveis e podem ser chamadas, a exemplo da chamada na classe Quadrado"""

class FormaGeometrica:
  def __init__(self, altura, largura):
    self.altura  = altura
    self.largura = largura


class Quadrado(FormaGeometrica):
    def __init__(self, altura, largura, atributo_quadrado):
      FormaGeometrica.__init__(self, altura, largura)
      self.atributo_quadrado  = atributo_quadrado

quadrado  = Quadrado(100,50, 'quadrado')

print(quadrado.altura)
print(quadrado.atributo_quadrado)

"""##Modificadores de Acesso
(Private)

*  __ antes do atributo o tornam privado


"""

class Segredo:
  def __init__(self):
    self.__segredo = 'Senha123' #esse atributo não poderá ser acessado fora da classe

  def __printaSegredo(self): #private
    print(self.__segredo)

  def printaSegredo(self):
    self.__printaSegredo() #irá funcionar, pois esta lendo a funcao protegida DENTRO DA CLASSE

seg = Segredo()
seg.printaSegredo()

## EXERCIICIOS

"""1 - Crie uma classe para representar um carro. Ele deve ter um atributo que diga sua potência em cavalos.Outro atributo deve dizer quando de gasolina/km ele consome. Crie um método em que voce fornece quantos km o carro andou e exibe quantos L gastou de gasolina"""

class Carro:
  def __init__(self, potencia, economia):
    self.potencia = potencia
    self.economia = economia

  def consumo(self, km):
    return km / self.economia

carro1 = Carro(100, 12)
consumo1 = carro1.consumo(24)
print("O consumo do carro foi de %f litros" % round(consumo1, 1))

carro2 = Carro(180, 16)
consumo2 =carro2.consumo(100)
print("O consumo do carro foi de %f litros" % round(consumo2, 1))

"""2 - Crie uma classe que represente uma pessoa. Ela deve possuir um CPF e um dependente, onde o dependente é outra pessoa. O dependente não é obrigatório. Crie as instancias pai e filho e depois imprima as saidas dos dados."""

class Pessoa:
  def __init__(self, nome, cpf, dependente = None):
    self.nome = nome
    self.cpf  = cpf
    self.dependente  = dependente

filho = Pessoa('Jõao', '446112364-54')

pai = Pessoa("Rodrigo", "471235841-66", filho)

print("Nome " , filho.nome, " CPF: ", filho.cpf, " Dependente: ", filho.dependente)
print("Nome " , pai.nome, " CPF: ", pai.cpf, " Dependente: ", pai.dependente.nome)

"""3 - Crie uma classe veículo com atributos peso, numero de rodas e potencia. Em seguida crie tres classes que geram de veiculo, onibus, carro e moto. Crie uma instancia de cada tipo e exiba."""

class Veiculo:
    def __init__(self, peso, numRodas, potencia):
      self.peso = peso
      self.numRodas = numRodas
      self.potencia = potencia

    def distanciaPercorrida(self):
      res = (self.peso / self.potencia) * 1000
      return round(res, 2)

class Moto(Veiculo):
  pass

class Carro(Veiculo):
  pass

class Onibus(Veiculo):
  pass





moto = Moto(80, 2, 80)
carro = Carro(400, 4, 140)
onibus = Onibus(1200, 8, 200)

print("Moto - peso: ", moto.peso,  " rodas: ", moto.numRodas, "  potencia:", moto.potencia, " distancia percorrida: ", moto.distanciaPercorrida())
print("Carro - peso: ", carro.peso,  " rodas: ", carro.numRodas, "  potencia:", carro.potencia, " distancia percorrida: ", carro.distanciaPercorrida())
print("Onibus - peso: ", onibus.peso,  " rodas: ", onibus.numRodas, "  potencia:", onibus.potencia, " distancia percorrida: ", onibus.distanciaPercorrida())