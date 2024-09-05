import sys, time, threading

a = []
b = a
sys.getrefcount([a])

def thread_function(name):
    print(f"Thread {name}: starting at {time.time()}")
    time.sleep(2)
    print(f"Thread {name}: finishing at {time.time()}")
threads = []

print("Thread about to start")
for i in range(1, 4):
    x = threading.Thread(target=thread_function, args=(i, ))
    threads.append(x)
    x.start()
print("Thread started")

for i in threads:
    i.join()
print("Thread finished")


def funzione(id:int):
    import time
    import random

    sleep_time:int = random.randint(1, 10)
    print(f"{id=} time {time.time()}")
    time.sleep(sleep_time)
    print(f"{id=} time {time.time()}")

if __name__ == "__main__":
    import threading
    from concurrent.futures import ThreadPoolExecutor

    with ThreadPoolExecutor(max_workers=10) as executor:
        executor.map(funzione, range(100))