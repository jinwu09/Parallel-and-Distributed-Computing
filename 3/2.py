from time import perf_counter
import concurrent.futures
import math
import requests

def GetWRite(link,filename):
        r=requests.get(link,allow_redirects=True)
        print(f"{filename} done")
        open(f"./3/images/{filename}", "wb").write(r.content)
        print("done Writing")



def DownloadConcurrent (linkList):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []
        for link, filename in linkList:
            future = executor.submit(GetWRite, link, filename)
            futures.append(future)
        
            
        
                    


if __name__ == "__main__":
    linkList = [
        ["https://i.natgeofe.com/n/548467d8-c5f1-4551-9f58-6817a8d2c45e/NationalGeographic_2572187_square.jpg", 'cat.jpg'],
        ["https://i.natgeofe.com/n/548467d8-c5f1-4551-9f58-6817a8d2c45e/NationalGeographic_2572187_square.jpg", 'cat1.jpg']
    ]
    startTime = perf_counter()
    endTime = perf_counter()
    DownloadConcurrent(linkList)
    print(f"it took about : {endTime-startTime}")

    print("done")
    