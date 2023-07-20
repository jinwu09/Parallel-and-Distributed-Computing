# jlos problems in the world af
# in 1 string how many syllable in it
import concurrent.futures

def CountSyllable(word:str):
    vowels = 'aeiouy'
    count = 0
    word =word.replace('eau','u')
    for i,char in enumerate(word,1):
        if char == ' ':
            continue
        for vowel in vowels:
            if len(word) == i and char == 'e':
                continue
            if vowel == char:
                count += 1
                break

    return [word,count]

if __name__ =="__main__":
    sentence = "hello there beautiful misogynistic"
    sentence = sentence.split(" ")
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = executor.map(CountSyllable,sentence)
        for result in results:
            print(f"the word {result[0]} the syllables has {result[1]}")