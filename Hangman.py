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
