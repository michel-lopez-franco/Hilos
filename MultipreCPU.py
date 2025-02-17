from multiprocessing import Pool

def compute_intensive(data):
    # Cálculos complejos que benefician del uso de múltiples CPUs
    return sum(x * x for x in range(data))

with Pool(4) as pool:  # 4 procesos
    results = pool.map(compute_intensive, range(1000))
    
    
print(results)