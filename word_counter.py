
with open('t.txt', 'r') as file:
    lines = file.readlines()
    wordList= [i[:-1].split(' ') for i in lines ]

    words = [i for x in wordList for i in x]
    chars = [i for x in words for i in x]
    lenChars = len(chars)
    lenWords = len(words)
    lenLines = len(lines)

    print(lenWords)
    print(lenChars)
    print(lenLines)
 
  