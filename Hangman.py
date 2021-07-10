import random

words = ['table', 'chair', 'mouse', 'laptop','office', 'gamer', 'torche', 'python']

word = random.choice(words)
print("_"*len(word))
lives = 6
wrong_input = []
correct_input = []
temp = ""
while lives !=0 and temp != word:
    letter = input("Guess a letter, you still have: " + str(lives) + " lives ")
    if(len(letter)!= 1):
        print("Please enter a single letter")
        continue
    if(letter in correct_input or letter in wrong_input):
        print("You already used this letter please choose a new one")
        continue
    elif(letter in word):
        correct_input.append(letter)
        temp = ""
        for i in word:
            if i in correct_input:
                temp = temp + i
            else:
                temp = temp + "_"
        print(temp)
    else:
        if(temp == ""):
            print("_"*len(word))
        else:
            print(temp)
        wrong_input.append(letter)
        lives = lives - 1
    if(lives == 0):
        print("You lost and the solution is: " + word)

if(lives>0):
    print("You found the word and you still have " + str(lives) + " lives")
    

