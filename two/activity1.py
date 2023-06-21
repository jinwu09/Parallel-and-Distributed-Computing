from threading import Thread
from time import perf_counter

def replace(filename, substr, new_substr):
    print(f"Processing the file {filename}")
    # # get the content of the file
    with open(filename, 'r') as f:
        content = f.read()
    
    # replace the substr by new_substr
    content = content.replace(substr, new_substr)

    # write data into the file
    with open(filename, 'w') as f:
        f.write(content)
        

filenames = [
    "./two/testfolder/text1.txt",
    "./two/testfolder/text2.txt",
    "./two/testfolder/text3.txt",
    "./two/testfolder/text4.txt",
    "./two/testfolder/text5.txt",
    "./two/testfolder/text6.txt",
    "./two/testfolder/text7.txt",
    "./two/testfolder/text8.txt",
    "./two/testfolder/text9.txt",
    "./two/testfolder/text10.txt",
    "./two/testfolder/text11.txt",
    "./two/testfolder/text12.txt",
    "./two/testfolder/text13.txt",
    "./two/testfolder/text14.txt",
    "./two/testfolder/text15.txt",
    "./two/testfolder/text16.txt",
    "./two/testfolder/text17.txt",
    "./two/testfolder/text18.txt",
    "./two/testfolder/text19.txt",
    "./two/testfolder/text20.txt",
    "./two/testfolder/1text1.txt",
    "./two/testfolder/1text2.txt",
    "./two/testfolder/1text3.txt",
    "./two/testfolder/1text4.txt",
    "./two/testfolder/1text5.txt",
    "./two/testfolder/1text6.txt",
    "./two/testfolder/1text7.txt",
    "./two/testfolder/1text8.txt",
    "./two/testfolder/1text9.txt",
    "./two/testfolder/1text10.txt",
    "./two/testfolder/1text11.txt",
    "./two/testfolder/1text12.txt",
    "./two/testfolder/1text13.txt",
    "./two/testfolder/1text14.txt",
    "./two/testfolder/1text15.txt",
    "./two/testfolder/1text16.txt",
    "./two/testfolder/1text17.txt",
    "./two/testfolder/1text18.txt",
    "./two/testfolder/1text19.txt",
    "./two/testfolder/1text20.txt",

]

def main():
    

    # create threads
    threads = [Thread(target=replace, args=(filename, 'a', "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."))
               for filename in filenames]
    
    
    # start the threads
    for thread in threads:
        thread.start()

    # wait for the threads to complete
    for thread in threads:
        thread.join()

def reset(filename, content):
    with open(filename, 'w') as f:
        f.write(content)

if __name__ =="__main__":
    for filedir in filenames:
        reset(filedir, "a\na\na\na\na\na\na\na\na\na")
    startTime = perf_counter()

    startTime = perf_counter()

    main()

    endTime = perf_counter()

    print(f"It took {endTime - startTime  } second(s) to complete")
