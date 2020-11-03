from random import radint

class Computador:
    def __init__(self, computador):
        self._computador = None
        pass

    def jogar(self):
        opcao = randint(1,3)
        if opcao == 1:
            self._computador = 'PEDRA'
        elif opcao == 2:
            self._computador = 'PAPEL'
        elif opcao == 3:
            self._computador = 'TESOURA'
