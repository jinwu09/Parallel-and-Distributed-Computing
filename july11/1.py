import multiprocessing
from time import sleep

def squares(number_list, results, s_value ,s_queue:multiprocessing.Queue):
    s_value.value = 123.53342
    for i,number in enumerate(number_list):
        result = number * number
        results[i] = result
        s_queue.put(result)
    print(f"within the albert process",list(results))


if __name__=="__main__":
    number_list = [1,2,3,4,5,6,7]
    shared_memory = multiprocessing.Array("i",len(number_list))
    shared_value = multiprocessing.Value("d",0.0)
    shared_queue = multiprocessing.Queue()
    albert = multiprocessing.Process(
        target=squares, args=(number_list, shared_memory,shared_value,shared_queue))
    albert.start()

    albert.join()
    print("outside the alber process", list(shared_memory))
    print("shared value is:", shared_value.value)
    print("shared queue is:")
    while not shared_queue.empty():
        print(shared_queue.get())
