#Criando a classe Casa()
class Casa():
    imobiliaria = "CTRL imoveis"
    def __init__(self, rua, bairro, CEP):
        self.rua = rua
        self.bairro = bairro
        self.CEP = CEP

    def getImobiliaria(self):
        return self.imobiliaria
    
    def getRua(self):
        return self.rua

    def getBairro(self):
        return self.bairro

    def getCEP(self):
        return self.CEP

    def setImobiliaria(self, i):
        self.imobiliaria = i

    def setRua(self, i):
        self.rua = r

    def setBairro(self, b):
        self.bairro = b

    def setCEP(self, c):
        self.CEP = c
    
    def endereçoCompleto(self):
        return 'endereço Completo: ' + self.rua + ', ' + self.bairro + ' - CEP: ' + self.CEP


#Criando o objeto Casa()
casa1 = Casa()

#Acessando atrbuto de um objeto:
print(casa1.CEP)

print(casa1.endereçoCompleto())

#Criando a classe cachorro:

class Cachorro:
    def __init__(self, nome, raca):
        self.nome = nome
        self.raca = raca
    def Latir(self):
        print(F'{self.nome} esta Latindo!')

#Criando o objeto Cachorro
meuCachorro = Cachorro('Bartô', 'Salsicha')
meuCachorro.Latir()


#Minha Classe

class cão:
    def __init__(self, nome, raca):
        self.nome = nome
        self.raca = raca
    def latir(self):
        print(F'{self.nome} esta latindo!! ')

#Meu objeto cão
meuCão = cão('Bob', 'Golden')
meuCão.latir()
