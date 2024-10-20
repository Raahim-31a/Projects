from random import randint
hangwords = ["hello", "this", "is", "hangman"]
sel = randint(0, len(hangwords) -1)
word = hangwords[sel]
lives = 6
handword = []
printguess = []
foundword = []
for i in range(len(word)):
    handword.append(word[i])
    printguess.append("_")
while lives > 0:
    printguessword = ""
    print(f"You have {lives} lives")
    for _ in range(len(word)):
        printguessword = printguessword + printguess[_]
    print(printguessword)
    if printguessword == word.strip():
        print("You won")
        exit()
    found = False
    guess = input(f"Enter your guess character: ").lower()
    for j in range(len(word)):
        if guess == word[j]:
            printguess[j] = guess
            found = True

    if found == False:
        lives = lives - 1

if lives == 0:
    print("You lost")
