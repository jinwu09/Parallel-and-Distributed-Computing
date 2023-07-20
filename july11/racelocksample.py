from multiprocessing import Process, Value, Lock
from time import sleep

def deposit(balance,s_lock):

    for i in range(100):
        sleep(.1)
        s_lock.acquire()
        balance.value = balance.value + 1
        s_lock.release()

def withdraw(balance,s_lock):
    for i in range(100):
        sleep(.1)
        s_lock.acquire()
        balance.value = balance.value - 1
        s_lock.release()

if __name__=="__main__":
    shared_balance = Value('i',200)
    lock = Lock()
    deposit_process = Process(target=deposit,args=(shared_balance,lock,))
    withdraw_process = Process(target=withdraw,args=(shared_balance,lock,))

    deposit_process.start()
    withdraw_process.start()
    
    deposit_process.join()
    withdraw_process.join()
    print("Remaining balance is : ", shared_balance.value)