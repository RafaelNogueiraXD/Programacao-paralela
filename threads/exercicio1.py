"""
Crie duas threads:

Uma conta de 1 a 5, com sleep(1) entre os números.

A outra conta de 10 a 15, também com sleep(1).

🧪 Objetivo: Ver as duas contagens acontecendo ao mesmo tempo no terminal.
"""
import threading
import time

def contador(inicio: int ,final: int, nome="anonimo"):
    for i in range(inicio, final+1):
        print(i)
        time.sleep(1)

        
if "__main__" == __name__:
    
    t1 = threading.Thread(target=contador, args=(1,5,"contador 1"))
    t2 = threading.Thread(target=contador, args=(10,15,"contador 2"))
    
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()