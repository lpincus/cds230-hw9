

def Read(filename="romeo-and-juliet.txt"):
    return open(filename).read()

def Parse(text):
    return text.lower().split()

def Count(wordlist):
    answer = {}
    distinctwords = set(wordlist)
    for word in distinctwords:
        answer[word] = wordlist.count(word)
    return answer

