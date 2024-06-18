import random

answers = ['Oylook is looking gooood girl', 'Mmmm no', 'OH yes!', 'Yahhhh try again lol', 'Is that even a question...?',
           'Uh its not looking good', 'Erm, maybe???', 'Uh, Ill let you figure that out yourself.']

input("Ask the Magic 8 Ball any question: ")

randomAnswer = random.randint(0,7)

print('The Magic 8 Ball says: ' + answers[randomAnswer])