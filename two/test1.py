from time import perf_counter, sleep
import threading

done = False
def worker():
    counter = 0 
    while True:
        counter = counter +1
        print(f"{counter}")
        sleep(1)

threading.Thread(target=worker, daemon=True).start()

input("pres any key to end the program")
done = True