import csv
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt

def registrar_em_csv(valor: float, metodo: str, nome_arquivo: str = "dados.csv"):
    with open(nome_arquivo, mode="a", newline='', encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow([datetime.now().isoformat(), valor, metodo])

def gerar_grafico(nome_arquivo: str = "dados.csv"):
    # Lê o CSV
    df = pd.read_csv(nome_arquivo, header=None, names=["data", "tempo", "metodo"])
    
    # Agrupa por método e calcula a média
    medias = df.groupby("metodo")["tempo"].mean().sort_values()
    
    # Cria o gráfico
    plt.figure(figsize=(8, 5))
    medias.plot(kind="bar", color="skyblue", edgecolor="black")
    plt.ylabel("Tempo Médio")
    plt.title("Comparação de Tempo por Método")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    
    # Exibe o gráfico
    plt.show()
