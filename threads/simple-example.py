import threading
import time
# objetivo é executar N funções ao mesmo tempo 
def tarefa(nome):
    print(f"[{nome}] Começou")
    time.sleep(2)
    print(f"[{nome}] Terminou")

# Criando duas threads
t1 = threading.Thread(target=tarefa, args=("Thread 1",))
t2 = threading.Thread(target=tarefa, args=("Thread 2",))
t3 = threading.Thread(target=tarefa, args=("Thread 3",))
t4 = threading.Thread(target=tarefa, args=("Thread 4",))

# Iniciando as threads
t1.start()
t2.start()
t3.start()
t4.start()

# Espera ambas terminarem
t1.join()
t2.join()
t3.join()
t4.join()

print("Todas as tarefas terminaram!")
