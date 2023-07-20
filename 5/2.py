import random
from multiprocessing import Pipe, Process


def player1(send_pipe, recv_pipe):
    firstStart = True
    while True:
        if firstStart:
            value = random.random()
            send_pipe.send(value)
            firstStart = False
            print(f"Player 1 sent: {value}")
            continue

        received_value = recv_pipe.recv()
        value = received_value + random.random()
        send_pipe.send(value)

        print(f"Player 1 received: {received_value}")
        print(f"Player 1 sent: {value}")

        if value > 10:
            print("player 1 ending")
            break


def player2(send_pipe, recv_pipe):
    while True:
        received_value = recv_pipe.recv()
        print(f"Player 2 received: {received_value}")

        if received_value > 10:
            print("player 2 ending")
            break

        value = received_value + random.random()
        send_pipe.send(value)
        print(f"Player 2 sent: {value}")


if __name__ == '__main__':

    player1_send_pipe, player2_recv_pipe = Pipe()

    player2_send_pipe, player1_recv_pipe = Pipe()

    player1_process = Process(target=player1, args=(
        player1_send_pipe, player1_recv_pipe))
    player2_process = Process(target=player2, args=(
        player2_send_pipe, player2_recv_pipe))

    player1_process.start()
    player2_process.start()

    player1_process.join()
    player2_process.join()
