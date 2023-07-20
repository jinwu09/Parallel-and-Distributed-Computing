import random
from multiprocessing import Process, Pipe


def sender(sendpipe):
    for _ in range(5):
        number = random.randint(1, 100)
        sendpipe.send(number)
        print(f"Sent: {number}")
    sendpipe.send(False)
    sendpipe.close()


def receiver(recv_pipe):
    while True:
        number = recv_pipe.recv()
        if number == False:
            break
        print(f"Received: {number}")
    recv_pipe.close()


if __name__ == '__main__':
    sender_pipe, receiver_pipe = Pipe()

    sender_proc = Process(target=sender, args=(sender_pipe,))
    receiver_proc = Process(target=receiver, args=(receiver_pipe,))

    sender_proc.start()
    receiver_proc.start()

    sender_proc.join()
    receiver_proc.join()
