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