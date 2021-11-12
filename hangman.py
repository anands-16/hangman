import random

name = input("enter the user name: ")
print("welcome",name)
print("try to guess the word in less than 10 attempt")


def getrandomword():
    words = ["apple","orange","grape","pappaya","kiwi","pinapple","watermelon","cherry","strawberry","greenapple","india","laptop","samsung","australia"]
    word = random.choice(words)
    #main_word = ""
    counts = 10
    valid_word = set("abcdefghijklmnopqrstuvwxyz")
    get_word = ""
    while len(word)>0:
        main_word = ""
        for letter in word:
            if letter in get_word:
                main_word = main_word+letter
            else:
                main_word = main_word+"_ "
        if main_word == word:
            print("you Won!",main_word)
            break

        print("Guess the word with in " + str(counts) + " Counts ", main_word)
        guess = input()
        counts = counts - 1
        print("you have only " + str(counts) + " chances left")

        if counts == 0:
            print("your chance is over! try again")
            break

        if guess in valid_word:
            get_word = get_word + guess
        else:
            print("enter the correct word")
            guess = input()

        if counts == 9:
            print("-------------")
            print("      o      ")
        if counts == 8:
            print("      o      ")
            print("      |      ")
        if counts == 7:
            print("      o      ")
            print("      |      ")
            print("     / \     ")
        if counts == 6:
            print("     \o      ")
            print("      |      ")
            print("     / \     ")
        if counts == 5:
            print("     \o/     ")
            print("      |      ")
            print("     / \     ")

        if counts == 4:
            print("     \o/ -   ")
            print("      |      ")
            print("     / \     ")

        if counts == 3:
            print("     \o/ --  ")
            print("      |      ")
            print("     / \     ")

        if counts == 2:
            print("     \o/ --- ")
            print("      |      ")
            print("     / \     ")

        if counts == 1:
            print("     \o/ ---|")
            print("      |      ")
            print("     / \     ")


getrandomword()
