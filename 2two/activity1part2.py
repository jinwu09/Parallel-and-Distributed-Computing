from threading import Thread
from time import perf_counter


def replace(filename, substr, new_substr):
    print(f"Processing the file {filename}")
    # get the content of the file
    with open(filename, 'r') as f:
        content = f.read()

    # replace the substr by new_substr
    content = content.replace(substr, new_substr)
    # content = new_substr

    # write data into the file
    with open(filename, 'w') as f:
        f.write(content)


filenames = [
    "./2two/testfolder/text1.txt",
    "./2two/testfolder/text2.txt",
    "./2two/testfolder/text3.txt",
    "./2two/testfolder/text4.txt",
    "./2two/testfolder/text5.txt",
    "./2two/testfolder/text6.txt",
    "./2two/testfolder/text7.txt",
    "./2two/testfolder/text8.txt",
    "./2two/testfolder/text9.txt",
    "./2two/testfolder/text10.txt",
    "./2two/testfolder/text11.txt",
    "./2two/testfolder/text12.txt",
    "./2two/testfolder/text13.txt",
    "./2two/testfolder/text14.txt",
    "./2two/testfolder/text15.txt",
    "./2two/testfolder/text16.txt",
    "./2two/testfolder/text17.txt",
    "./2two/testfolder/text18.txt",
    "./2two/testfolder/text19.txt",
    "./2two/testfolder/text20.txt",
    "./2two/testfolder/1text1.txt",
    "./2two/testfolder/1text2.txt",
    "./2two/testfolder/1text3.txt",
    "./2two/testfolder/1text4.txt",
    "./2two/testfolder/1text5.txt",
    "./2two/testfolder/1text6.txt",
    "./2two/testfolder/1text7.txt",
    "./2two/testfolder/1text8.txt",
    "./2two/testfolder/1text9.txt",
    "./2two/testfolder/1text10.txt",
    "./2two/testfolder/1text11.txt",
    "./2two/testfolder/1text12.txt",
    "./2two/testfolder/1text13.txt",
    "./2two/testfolder/1text14.txt",
    "./2two/testfolder/1text15.txt",
    "./2two/testfolder/1text16.txt",
    "./2two/testfolder/1text17.txt",
    "./2two/testfolder/1text18.txt",
    "./2two/testfolder/1text19.txt",
    "./2two/testfolder/1text20.txt",

]

def reset(filename,content):
    with open(filename, 'w') as f:
        f.write(content)

def main():
    

    for filename in filenames:
        replace(filename, "a", "It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like).")




if __name__ == "__main__":
    for filedir in filenames:
        reset(filedir, "a\na\na\na\na\na\na\na\na\na")
    startTime = perf_counter()

    main()

    endTime = perf_counter()

    print(f"It took {endTime - startTime } second(s) to complete")
