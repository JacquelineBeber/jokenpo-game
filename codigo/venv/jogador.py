
class Jogador:
    def __init__(self, nome: str, pontos: int):
        if isinstance(nome, str):
            self.__nome = nome
        if isinstance(pontos, str):
            self.__pontos = pontos

    contador = 0

    def jogarPedra(self):
        if self.__jogada == 'PEDRA':
            if self._computador == 'PEDRA':
                contador += 0
            elif self._computador == 'PAPEL':
                contador -= 1
            elif self._computador == 'TESOURA':
                contador += 1
        return contador

    def jogarPapel(self):
        if self.__jogada == 'PAPEL':
            if self._computador == 'PEDRA':
                contador += 1
            elif self._computador == 'PAPEL':
                contador += 0
            elif self._computador == 'TESOURA':
                contador -= 1
        return contador

    def jogarTesoura(self):
        if self._jogada == 'TESOURA':
            if self._computador == 'PEDRA':
                contador -= 1
            elif self._computador == 'PAPEL':
                contador += 1
            elif self._computador == 'TESOURA':
                contador += 0
        return contador