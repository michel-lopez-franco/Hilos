from multiprocessing import Process

# Cada proceso tiene su propia copia de counter
def increment(counter):
    counter.value += 1

# Se necesita un tipo especial para compartir datos
from multiprocessing import Value
counter = Value('i', 0)

processes = [Process(target=increment, args=(counter,)) for _ in range(10)]
for p in processes:
    p.start()
    p.join()
    
print(counter.value)