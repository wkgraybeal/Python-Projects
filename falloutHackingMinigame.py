import random

def startHacking(nLetters, nWords):
    f = open('enable1.txt', 'r')
    words = []
    while(True):
        line = f.readline().strip()
        if len(line) == nLetters:
            words.append(line)
        if len(line) == 0:
            break
    random.shuffle(words)
    gameWords = []
    for idx, w in enumerate(words):
        if idx >= nWords:
            break
        gameWords.append(words[idx])

    answer = gameWords[random.randint(0,nWords-1)]
    for w in gameWords:
        print(w.upper())

    nTries = 4
    while (nTries > 0):
        nCorrect = 0
        print("Guess ({} left)? ".format(nTries), end="")
        guess = input("")
        if guess not in gameWords:
            print("Guess not in list")
            nTries -= 1
            continue
        for idx,c in enumerate(guess):
            if c == answer[idx].lower():
                nCorrect += 1
        nTries -= 1
        print("{}/{} correct".format(nCorrect,nLetters))
        if nCorrect == nLetters:
            print("You win!")
            return

    print("You lose!")
    print("The correct answer was {}".format(answer))



def main():
    inp = int(input("Difficulty? (1-5) "))
    if inp >= 1 and inp <= 5:
        if inp == 1:
            nLetters = 4
            nWords = 5
        elif inp == 2:
            nLetters = 6
            nWords = 8
        elif inp == 3:
            nLetters = 8
            nWords = 10
        elif inp == 4:
            nLetters = 12
            nWords = 12
        elif inp == 5:
            nLetters = 15
            nWords = 15
        startHacking(nLetters, nWords)
    else:
        print("That's not a diffculty")

main()
