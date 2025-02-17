import threading

# La variable shared_counter es accesible por todos los threads
shared_counter = 0

def increment():
    global shared_counter
    shared_counter += 1

threads = [threading.Thread(target=increment) for _ in range(10)]
for t in threads:
    t.start()
    t.join()
    
print(shared_counter)

    
    
