from time import perf_counter,sleep
import threading

def task(id,delayInSeconds):
    print(f'{id} is working')
    sleep(delayInSeconds)
    print(f"{id} is done.")

start = perf_counter()
numOfHreads = 1000000
threads=[]
for i in range(numOfHreads):
    t = threading.Thread(target=task,args=(i,1))
    threads.append(t)
    t.start()

for thread in threads:
    thread.join()

end = perf_counter()

print(f"take about {end - start :0.2f}")