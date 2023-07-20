import multiprocessing
import time

def shared(conn):
    time.sleep(5)
    conn.send(['Albert',99])

if __name__=="__main__":
    receiver, sender = multiprocessing.Pipe()
    jymclai = multiprocessing.Process(target=shared,args=(sender,))
    jymclai.start()
    print(receiver.recv())
    print("testing 101")
    jymclai.join()
