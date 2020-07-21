import random

    
def game():
    
    word_list = ['python', 'java', 'kotlin', 'javascript']
    choice = random.choice(word_list)
    dashes = list(len(choice) * '-')  # initial value
    marker = set()
    total = set()
    fail = 0
    print(len(choice) * '-')
    letter = input('Input a letter: ')
    while fail != 8 and marker != set(choice):
        if letter in set(choice):
            if letter in marker:
                print('You already typed this letter')
            else:
                marker.add(letter)
                dashes = list(choice)  # recover dashes
                for a in range(len(choice)):  # checks every character in word
                    if choice[a] != letter and choice[a] not in marker:
                        dashes[a] = '-'
        elif len(letter) != 1:
            print("You should input a single letter")
        elif not letter.islower():
            print("It is not an ASCII lowercase letter")
        elif letter in total:
            print('You already typed this letter')
        else:
            if letter not in set(choice):
                print('No such letter in the word')
                fail += 1
        if fail == 8:
            print('You are hanged!')
        elif marker == set(choice):
            print()
            print(''.join(dashes))
            print('You guessed the word!')
            print('You survived!')
        else:
            print()
            print(''.join(dashes))
            total.add(letter)
            letter = input('Input a letter: ')
    replay()    
def replay():
    action2 = input('Type "play" to play the game, "exit" to quit: ')
    if action2 == "play":
        game()
    else:
        exit()
print('H A N G M A N\n')
action = input('Type "play" to play the game, "exit" to quit: ')
if action == "play":
    game()
else:
    exit()
