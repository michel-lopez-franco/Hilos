import time
import threading
import multiprocessing

N= 32

def io_bound_task():
    time.sleep(1)  # Simula I/O

def cpu_bound_task():
    sum(i * i for i in range(10**7))  # Operación CPU intensiva

# Test con threading
def test_threading():
    threads = [threading.Thread(target=io_bound_task) for _ in range(N)]
    start = time.time()
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    return time.time() - start

# Test con multiprocessing
def test_multiprocessing():
    processes = [multiprocessing.Process(target=cpu_bound_task) for _ in range(N)]
    start = time.time()
    for p in processes:
        p.start()
    for p in processes:
        p.join()
    return time.time() - start

# Para tareas I/O bound, threading es más eficiente
print(f"Threading (I/O): {test_threading():.2f} segundos")

# Para tareas CPU bound, multiprocessing es más eficiente
print(f"Multiprocessing (CPU): {test_multiprocessing():.2f} segundos")