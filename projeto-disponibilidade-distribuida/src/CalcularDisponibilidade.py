import math

class CalcularDisponibilidade:
    def calcular_disponibilidade_analitica(self, n, k, p):
        soma = 0.0
        for i in range(k, n + 1):
            soma += math.comb(n, i) * (p ** i) * ((1 - p) ** (n - i))
        return soma

    def calcular_caso_k1(self, n, p):
        return 1 - (1 - p) ** n

    def calcular_caso_kn(self, n, p):
        return p ** n