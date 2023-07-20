from time import perf_counter
import concurrent.futures
import requests
from PIL import Image, ImageOps

def GetWRite(link, filename):
    r = requests.get(link, allow_redirects=True).content
    print(f"{filename} done downloading")
    open(f"{filename}", "wb").write(r)
    with Image.open(r"./4/images/"+filename) as im:
        im = ImageOps.grayscale(im)
        im.save(f'./4/images/greyscale_'+filename)

    print("done Writing")


def DownloadConcurrent(linkList):
    with concurrent.futures.ProcessPoolExecutor() as executor:
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
