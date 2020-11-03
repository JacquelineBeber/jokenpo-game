
class Jogador:
    def __init__(self, nome: str, pontos: int):
        if isinstance(nome, str):
            self.__nome = nome
        if isinstance(pontos, str):
            self.__pontos = pontos

    pontos = 0
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