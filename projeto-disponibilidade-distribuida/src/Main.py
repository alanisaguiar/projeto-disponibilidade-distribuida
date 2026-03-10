import math
from CalcularDisponibilidade import CalcularDisponibilidade
from SimularDisponibilidade import SimularDisponibilidade
from AnalizarResultados import AnalizarResultados

def main():
    valores_n = [2, 4, 8, 16]
    valores_p = [i / 10 for i in range(11)]
    rodadas = 50000

    calculadora = CalcularDisponibilidade()
    simulador = SimularDisponibilidade()
    analisador = AnalizarResultados(calculadora, simulador)

    df_resultados = analisador.gerar_resultados(valores_n, valores_p, rodadas)
    analisador.salvar_csv(df_resultados, "dados/resultados.csv")
    analisador.gerar_graficos_analiticos(valores_n, valores_p, "graficos")

    for n in valores_n:
        for k in [1, math.ceil(n / 2), n]:
            analisador.gerar_grafico_comparacao(n, k, valores_p, rodadas, "graficos")

    print("Execução finalizada com sucesso.")
    print("Arquivo CSV salvo em: dados/resultados.csv")
    print("Gráficos salvos na pasta: graficos/")


if __name__ == "__main__":
    main()