import concurrent.futures
from time import perf_counter

def checkEven(start, end):
    for number in range(start, end+1):
        if (number % 2) == 0:
            print(f"{number} is Even")
        else:
            print(f"{number} is Odd")

if __name__=="__main__":
    threads = 2
    start = 30
    end = 50
    startTime = perf_counter()
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []
        for thread in range(threads):
            task = executor.submit(checkEven , start,end)
            futures.append(task)
    endTime = perf_counter()
    print(f"it took about : {endTime-startTime}")

        
