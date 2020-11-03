from pessoa import Pessoa

class Jogador(Pessoa):
    def __init__(self, nome: str, jogada: str):
        if isinstance(nome, str):
            self.__nome = nome
        if isinstance(jogada, str):
            self.__jogada = jogada

    contador = 0

    def jogarPedra(self):
        if self.__jogada == 'PEDRA':
            if self.__computador == 'PEDRA':
                contador += 0
            elif self.__computador == 'PAPEL':
                contador -= 1
            elif self.__computador == 'TESOURA':
                contador += 1
        return contador

    def jogarPapel(self):
        if self.__jogada == 'PAPEL':
            if self.__computador == 'PEDRA':
                contador += 1
            elif self.__computador == 'PAPEL':
                contador += 0
            elif self.__computador == 'TESOURA':
                contador -= 1
        return contador

    def jogarTesoura(self):
        if self.__jogada == 'TESOURA':
            if self.__computador == 'PEDRA':
                contador -= 1
            elif self.__computador == 'PAPEL':
                contador += 1
            elif self.__computador == 'TESOURA':
                contador += 0
        return contador