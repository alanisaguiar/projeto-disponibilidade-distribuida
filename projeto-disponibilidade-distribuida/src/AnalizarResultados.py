import math
import os
import pandas as pd
import matplotlib.pyplot as plt

class AnalizarResultados:
    def __init__(self, calculadora, simulador):
        self.calculadora = calculadora
        self.simulador = simulador

    def gerar_resultados(self, valores_n, valores_p, rodadas=50000):
        resultados = []

        for n in valores_n:
            ks = [1, math.ceil(n / 2), n]

            for k in ks:
                for p in valores_p:
                    analitico = self.calculadora.calcular_disponibilidade_analitica(n, k, p)
                    experimental = self.simulador.simular_disponibilidade(n, k, p, rodadas)
                    erro = abs(analitico - experimental)

                    resultados.append({
                        "n": n,
                        "k": k,
                        "p": p,
                        "analitico": analitico,
                        "experimental": experimental,
                        "erro_absoluto": erro
                    })

        return pd.DataFrame(resultados)

    def salvar_csv(self, dataframe, caminho_arquivo):
        os.makedirs(os.path.dirname(caminho_arquivo), exist_ok=True)
        dataframe.to_csv(caminho_arquivo, index=False)

    def gerar_graficos_analiticos(self, valores_n, valores_p, pasta_saida="graficos"):
        os.makedirs(pasta_saida, exist_ok=True)

        for n in valores_n:
            ks = [1, math.ceil(n / 2), n]

            plt.figure(figsize=(8, 5))

            for k in ks:
                ys = [
                    self.calculadora.calcular_disponibilidade_analitica(n, k, p)
                    for p in valores_p
                ]
                plt.plot(valores_p, ys, marker="o", label=f"k={k}")

            plt.title(f"Disponibilidade Analítica - n={n}")
            plt.xlabel("p")
            plt.ylabel("Disponibilidade")
            plt.ylim(0, 1.05)
            plt.grid(True)
            plt.legend()
            plt.savefig(f"{pasta_saida}/grafico_analitico_n{n}.png")
            plt.close()

    def gerar_grafico_comparacao(self, n, k, valores_p, rodadas=50000, pasta_saida="graficos"):
        os.makedirs(pasta_saida, exist_ok=True)

        ys_analitico = [
            self.calculadora.calcular_disponibilidade_analitica(n, k, p)
            for p in valores_p
        ]

        ys_experimental = [
            self.simulador.simular_disponibilidade(n, k, p, rodadas)
            for p in valores_p
        ]

        plt.figure(figsize=(8, 5))
        plt.plot(valores_p, ys_analitico, marker="o", label="Analítico")
        plt.plot(valores_p, ys_experimental, marker="x", label="Experimental")
        plt.title(f"Comparação Analítico x Experimental - n={n}, k={k}")
        plt.xlabel("p")
        plt.ylabel("Disponibilidade")
        plt.ylim(0, 1.05)
        plt.grid(True)
        plt.legend()
        plt.savefig(f"{pasta_saida}/comparacao_n{n}_k{k}.png")
        plt.close()