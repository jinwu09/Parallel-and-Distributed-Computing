from time import perf_counter, sleep
import threading
def task(id, delayInSeconds):
    print(f"{id} is working...")
    sleep(delayInSeconds)
    print(f'{id} is done')

start = perf_counter()
threading.Thread(target=task, args=(1, 1)).run()
threading.Thread(target=task,args=(2,5)).run()

# t1.start()
# t2.start()
# t1.join()
# t2.join()

end = perf_counter()

print(f"takes about {end-start :0.2f}")