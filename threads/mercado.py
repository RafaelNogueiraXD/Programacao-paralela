"""
Simule uma fila de clientes sendo atendidos. Cada cliente demora entre 1 e 3 segundos pra ser atendido.
Use threads pra atender vários clientes simultaneamente (como se fossem vários guichês de atendimento).
Limite de guiches: 5
🧪 Objetivo: Praticar a criação de várias threads a partir de uma fila/lista.

se chegar 7 clientes, divido por 5, resultado é 1 por caixa, como numero é menor que 10,
é necessário fazer fazer 7 - 5 , para descobrir quantos faltam para redestribuir em igual

se for 37 clientes, por 5, da 7 clientes por caixa, fazendo 37-(5*7), sabemos que sobra 2 clientes
para dividir entre os caixas

"""

import random
import time
import threading

numero_caixas = 5
caixas = [0] * numero_caixas

chegada_clientes = random.randint(1, 100)

lock = threading.Lock()

def redistribuicao(clientes):
    while clientes > 0:
        menor = min(caixas)
        for i in range(len(caixas)):
            if caixas[i] == menor and clientes > 0:
                caixas[i] += 1
                clientes -= 1

def calcula_clientes_por_caixa(chegada):
    if chegada == 0:
        return
    
    if chegada > 9:
        divisao = chegada // numero_caixas
        sobra = chegada - (divisao * numero_caixas)

        for i in range(len(caixas)):
            caixas[i] += divisao

        redistribuicao(sobra)
    else:
        redistribuicao(chegada)

def atender_clientes(caixa_id, total_clientes):
    for i in range(total_clientes):
        tempo = random.randint(1, 3)
        print(f"Caixa {caixa_id+1} atendendo cliente {i+1} (vai demorar {tempo}s)...")
        time.sleep(tempo)
        print(f"Caixa {caixa_id+1} finalizou atendimento do cliente {i+1}")

def mostra_caixas():
    print("\nClientes por caixa:")
    for i, caixa in enumerate(caixas):
        print(f"Caixa {i+1}: {caixa} clientes")

if __name__ == "__main__":
    print(f"Chegaram {chegada_clientes} clientes.\n")
    calcula_clientes_por_caixa(chegada_clientes)
    mostra_caixas()

    
    threads = []
    for i in range(numero_caixas):
        t = threading.Thread(target=atender_clientes, args=(i, caixas[i]))
        threads.append(t)
        t.start()

    
    for t in threads:
        t
