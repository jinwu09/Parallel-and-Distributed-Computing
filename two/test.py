from time import perf_counter, sleep
import threading

def  worker ():
    print("Working....")
    sleep(1)
    print("Resting....")


if __name__=="__main__":
    start = perf_counter()


    t1 = threading.Thread(target=worker)
    t2 = threading.Thread(target=worker)
    t3 = threading.Thread(target=worker)

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()


    end = perf_counter()

    print(f"it took {end- start:0.2f}seconds to finish the task ")
