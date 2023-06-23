from time import perf_counter, sleep
from threading import Thread


def task(id:int, delayInSeconds:int):
    print(f"{id} is working...")
    sleep(delayInSeconds)
    print(f'{id} is done')


def worker():
    print("Working....")
    sleep(1)
    print("Resting....")


def main():
    numOfTask = 10
    numOfWorker = 10
    # create threads
    threads= []
    for id in range(numOfTask):
        threads.append(Thread(target=task, args=(id, id/2)))

    for work in range(numOfWorker):
        threads.append(Thread(target=worker))


    # start the threads
    for thread in threads:
        thread.start()

    # wait for the threads to complete
    for thread in threads:
        thread.join()

if __name__ =="__main__":
    start = perf_counter()

    main()

    end = perf_counter()