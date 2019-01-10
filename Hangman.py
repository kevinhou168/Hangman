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
        print("Congratulations, you saved the hangman! He goes on to live another day!")
    else:
        print("You failed to save the hangman from the doom that was " + hangman)

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

    while num_guesses > 0:
        guess = input('Enter an upper-case letter: \n')
        check = False
        for j in range(0, len(hangman)):
            if hangman[j].lower() == guess.lower():
                fill_blanks[j] = hangman[j]
                check = True

        if check == False:
            num_guesses -= 1



        if num_guesses == 1:
            print("You have 1 remaining guess.")
        elif num_guesses == 0:
            if hangman == (''.join(fill_blanks)):
                result(True)
            else:
                result(False)
        else:
            print("You have " + str(num_guesses) + " remaining guesses.")

        if hangman == (''.join(fill_blanks)):
            print(''.join(fill_blanks))
            result(True)
        else:
            guessed_letters.append(guess)
            print(''.join(fill_blanks))
            print("So far, you have guessed: \n" + (', '.join(guessed_letters)))


game()
