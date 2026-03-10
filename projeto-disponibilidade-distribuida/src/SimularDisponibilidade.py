import random

class SimularDisponibilidade:
    def simular_disponibilidade(self, n, k, p, rodadas=50000):
        sucessos = 0

        for _ in range(rodadas):
            disponiveis = 0

            for _ in range(n):
                if random.random() <= p:
                    disponiveis += 1

            if disponiveis >= k:
                sucessos += 1

        return sucessos / rodadas