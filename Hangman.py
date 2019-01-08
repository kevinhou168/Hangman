import random

win = False
player_name = input('Welcome to Hangman Python Edition, what is your name?\n')
people = ['boy', 'cat', 'bird', 'girl', 'dog', 'Northwestern student', 'blue footed booby', 'SpaceX CEO']
verbs = ['leapt over', 'attacked', 'climbed on', 'created', 'destroyed', 'flipped over', 'hugged', 'kissed']
objects = ['mountain', 'hill', 'building', 'desk', 'satellite', 'computer', 'tree', 'lecture hall']

def random_word():
    word_list = people + objects
    num = random.randrange(0, len(word_list))
    return word_list[num]

def random_sentence():
    num_people = random.randrange(0, len(people))
    num_verbs = random.randrange(0, len(verbs))
    num_objects = random.randrange(0, len(objects))
    return "The " +people[num_people]+ " " +verbs[num_verbs]+ " the " +objects[num_objects]

def result(win):
    if win == True:
        print("Congratulations, you saved the hangman! But from what did you save him from...?")
    else:
        print("Oh no! You failed to save the hangman. There seems to be another one though, for some reason.")

    if input("Would you like to play again? (Y/N)") == 'Y':
        game()
    elif input("Would you like to play again? (Y/N)") == 'N':
        print("Thank you for playing!")
        exit()

def game():
    difficulty = input(player_name + ', would you like a word or a sentence?\n')
    if difficulty == 'word':
        hangman = random_word()
    elif difficulty == 'sentence':
        hangman = random_sentence()
    else:
        'Please enter either "word" or "sentence."'
        game()

    guessed_letters = []
    fill_blanks = []
    for i in range(0, len(hangman)):
        if hangman[i] == ' ':
            fill_blanks.append(' ')
        else:
            fill_blanks.append('_ ')

    num_guesses = len(hangman)
    print('You have ' + str(num_guesses) + ' guesses to save the hangman. It is up to you, ' + player_name + '.')

    for i in range(0, num_guesses):
        guess = input('Enter an upper-case letter: \n')
        for j in range(0, len(hangman)):
            if hangman[j] == guess:
                fill_blanks[j] = hangman[j]

        num_guesses -= 1
        guessed_letters.append(guess)
        print(fill_blanks)
        print("So far, you have guessed: \n" + str(guessed_letters))

        if num_guesses == 1:
            print("You have 1 remaining guess.")
        elif num_guesses == 0:
            if hangman == fill_blanks:
                result(True)
            else:
                result(False)
        else:
            print("You have " + num_guesses + " remaining guesses.")

        if hangman == fill_blanks:
            result(True)

game()
