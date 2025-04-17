from multiprocessing import Pool, cpu_count
import time
import threading
from numeroPrimo import Numero_Primo
from functions import *

# Intervalos definidos
intervalos = [
    (10_000, 50_000),
    (50_000, 90_000),
    (90_000, 130_000),
    (130_000, 170_000),
    (230_000, 270_000),
    (330_000, 370_000),
    (430_000, 470_000),
    (530_000, 570_000),
    (630_000, 670_000)
]

calculadora = Numero_Primo()

# Função wrapper para multiprocessing
def contar_primos_wrapper(intervalo):
    return calculadora.contar_primos(intervalo)

def multi_threads():
    resultados = [0] * len(intervalos)
    threads = []
    inicio = time.time()

    for i, intervalo in enumerate(intervalos):
        thread = threading.Thread(target=calculadora.contar_primos_thread, args=(intervalo, resultados, i))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
    
    fim = time.time()
    output(resultados, inicio, fim)
    return [fim - inicio , "threads"]

def normal():
    inicio = time.time()
    resultados = []
    for intervalo in intervalos:
        resultado = calculadora.contar_primos(intervalo)
        resultados.append(resultado)
    fim = time.time()
    output(resultados, inicio, fim)
    return [fim - inicio , "normal"]

def multi_processing():
    print(f"Usando {cpu_count()} núcleos disponíveis")
    inicio = time.time()
    with Pool(cpu_count()) as pool:
        resultados = pool.map(contar_primos_wrapper, intervalos)
    fim = time.time()
    output(resultados, inicio, fim)
    return [fim - inicio , "multiprocessing"]

def output(resultados,inicio, fim):
    total_primos = sum(resultados)
    print(f"\nTotal de primos encontrados: {total_primos}")
    print(f"Tempo total: {fim - inicio:.2f} segundos")       

if __name__ == "__main__":
    for _ in range(0, 10):
        resultado = multi_processing()
        resultado1 = multi_threads()
        resultado2 = normal()
        registrar_em_csv(resultado[0], resultado[1])
        registrar_em_csv(resultado1[0], resultado1[1])
        registrar_em_csv(resultado2[0], resultado2[1])
    
    gerar_grafico()
