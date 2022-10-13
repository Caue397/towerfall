'''
A idéia desse arquivo é implementar o controle de jogadores
de um jogo simples chamado towerfall

O jogo tem 4 jogadores, no máximo.

Assim, vamos representar ele por uma classe, que tenha a capacidade de
guardar um nome de jogador (uma string) em uma posicao (1,2,3 ou 4)

Primeiramente, vamos implementar os métodos de adicionar e consultar jogador

Depois, vamos implementar um método para trocar dois jogadores 

O que acontece se vc tentar criar um jogador adicionando a uma
posicao que já existe?

Poderiamos retornar uma string, como "posicao ocupada". Mas o jeito
mais profissional de fazer é lançar uma excessão.

Uma excessão é um erro que facilita a vida
de quem recebe o erro.

A gente pode até dar mais mensagem de erro pro(a) usuário(a)

raise PosicaoOcupadaException(string) mostra essa string pro usuario

Vamos fazer uma função remover, que tira um jogador

'''
'''
O erro que estamos usando, PosicaoOcupadaException, foi a gente mesmo que criou.

Veja como:
class PosicaoOcupadaException(Exception):
    pass 

Seguindo essa receita de bolo vamos criar uma excessão nova, chamada PosicaoDesocupadaException
'''
class PosicaoOcupadaException(Exception):
    pass 

class PosicaoDesocupadaException(Exception):
    pass

class PosicaoInexistenteException(Exception):
    pass

'''
Se vc tentar deletar um usuário que não existe, lance a PosicaoDesocupadaException
'''

'''
Agora use a excessão nova
Se vc tentar trocar dois usuários, e um deles (ou os dois!) nao existe, lance a PosicaoDesocupadaException
'''

'''
Criar e usar uma terceira excessão
Se o usuário passar um numero invalido ao adicionar, remover ou trocar, lance a excessão PosicaoInexistenteException.

Lembre que as posições válidas são 1 2 3 e 4
'''

class Towerfall:
    def __init__(self):
        self.jogadores={}

    def adicionar(self, jogador, posicao):
        if posicao > 4 or posicao < 1:
            raise PosicaoInexistenteException()
        if posicao in self.jogadores.keys():
            raise PosicaoOcupadaException(f'posicao {posicao} ocupada')
        self.jogadores[posicao]=jogador
      
    def jogador(self, posicao_jogador):
        return f'{self.jogadores[posicao_jogador]} (player {posicao_jogador})'
    
    def trocar(self, posicao1, posicao2):
        if posicao1 > 4 or posicao1 < 1:
            raise PosicaoInexistenteException()
        if posicao2 > 4 or posicao2 < 1:
            raise PosicaoInexistenteException()
        if posicao1 not in self.jogadores.keys():
            raise PosicaoDesocupadaException()
        if posicao2 not in self.jogadores.keys():
            raise PosicaoDesocupadaException()
        posicao1_troca=self.jogadores[posicao1]
        posicao2_troca=self.jogadores[posicao2]
        self.jogadores[posicao1]=posicao2_troca
        self.jogadores[posicao2]=posicao1_troca

    def remover(self, posicao):
        if posicao > 4 or posicao <1:
            raise PosicaoInexistenteException()
        if posicao not in self.jogadores.keys():
            raise PosicaoDesocupadaException()
        self.jogadores.pop(posicao)

import unittest

class TestStringMethods(unittest.TestCase):

    def test_01_adicionar(self):
        t = Towerfall()
        t.adicionar("mel",1)
        self.assertEqual(t.jogador(1),"mel (player 1)")
        t.adicionar("athena",3)
        self.assertEqual(t.jogador(1),"mel (player 1)")
        self.assertEqual(t.jogador(3),"athena (player 3)")

    def test_02_trocar(self):
        t = Towerfall()
        t.adicionar("mel",1)
        t.adicionar("athena",3)
        t.trocar(1,3)
        self.assertEqual(t.jogador(3),"mel (player 3)")
        self.assertEqual(t.jogador(1),"athena (player 1)")

    def test_04_posicao_ocupada(self):
        t = Towerfall()
        t.adicionar("mel",1)
        t.adicionar("athena",3)
        #esse try e except eu vou te explicar na outra aula
        try:
            t.adicionar("zeus",3)
            self.fail("seu código não deu o erro esperado")
        except PosicaoOcupadaException:
            "legal, seu código deu o erro esperado. Essa linha nao faz nada"
        
    def test_05_erro_com_string(self):
        t = Towerfall()
        t.adicionar("mel",1)
        t.adicionar("athena",3)
        #esse try e except eu vou te explicar na outra aula
        try:
            t.adicionar("zeus",1)
            self.fail("seu código não deu o erro esperado")
        except PosicaoOcupadaException as e:
            if "posicao 1 ocupada" not in str(e): 
                self.fail("você esqueceu de colocar o texto de erro")
        t.adicionar("zeus",2)
        try:
            t.adicionar("thor",2)
            self.fail("seu código não deu o erro esperado")
        except PosicaoOcupadaException as e:
            if "posicao 2 ocupada" not in str(e): 
                self.fail("você esqueceu de colocar o texto de erro")

    def test_06_remover(self):
        t = Towerfall()
        t.adicionar("mel",1)
        #esse try e except eu vou te explicar na outra aula
        try: 
            t.adicionar('zeus',1)
        except PosicaoOcupadaException:
            "tudo ok, tinha que dar erro mesmo"
        t.remover(1)
        try:
            t.adicionar('zeus',1)
            self.assertEqual(t.jogador(1),"zeus (player 1)")
        except PosicaoOcupadaException:
            self.fail("tinha deletado a posicao 1, mas ainda está aparecendo ocupada")

    def test_07_nova_excessao(self):
        try:
            a = PosicaoDesocupadaException
        except NameError: #erro de variavel nao existe
            self.fail("voce nao criou a excessão que eu pedi")

    def test_08_usar_nova_excessao_ao_remover(self):
        t = Towerfall()
        t.adicionar("zeus",4)
        t.remover(4)
        try:
            t.remover(4)
            self.fail("tinha que der dado erro, mas nao deu")
        except PosicaoDesocupadaException:
            "beleza, deu o erro certo"
        except:
            self.fail("era pra ter dado PosicaoDesocupadaException, mas nao deu")
    

    def test_09_usar_nova_excessao_ao_trocar(self):
        t = Towerfall()
        t.adicionar("zeus",4)
        try:
            t.trocar(1,4)
            self.fail("tinha que der dado erro, mas nao deu")
        except PosicaoDesocupadaException:
            "beleza, deu o erro certo"
        except:
            self.fail("era pra ter dado PosicaoDesocupadaException, mas nao deu")
        t.adicionar("mel",1)
        t.trocar(1,4) #nao devia dar erro

    def test_10_usar_terceira_excessao(self):
        t = Towerfall()
        try:
            t.adicionar("zeus",10)
            self.fail("tinha que dar erro ao usar a posicao 10")
        except PosicaoInexistenteException:
            "beleza, fez a excessão certa"
        try:
            t.remover(5)
            self.fail("tinha que dar erro ao usar a posicao 5")
        except PosicaoInexistenteException:
            "beleza, fez a excessão certa"
        try:
            t.trocar(1,6)
            self.fail("tinha que dar erro ao usar a posicao 6")
        except PosicaoInexistenteException:
            "beleza, fez a excessão certa"
        try:
            t.trocar(7,2)
            self.fail("tinha que dar erro ao usar a posicao 7")
        except PosicaoInexistenteException:
            "beleza, fez a excessão certa"
        try:
            t.trocar(0,2)
            self.fail("tinha que dar erro ao usar a posicao 0")
        except PosicaoInexistenteException:
            "beleza, fez a excessão certa"
#pode deletar esse código, se quiser.
#mas qq vc acha que ele faz??
try:
    from towerfall_gabarito import *
except:
    pass


def runTests():
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestStringMethods)
        unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)

runTests()