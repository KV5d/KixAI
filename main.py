#Raine Berrigan
#14/11/2020
#DESCRIPTION = KixAI chatbot made with chatterbot + nltk
#Python 3.8.6 32-bit




import datetime
from art.art import tprint
from tqdm import trange
from time import sleep
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

now = datetime.datetime.now()

tprint("Kix")

print()

print(now)

print()

for i in trange(10, desc ="Initiating "):
    sleep(0.2)

sleep(0.5)

print()

print(now)

print("\nHello and welcome to Kix! ")

sleep(1)

name = input("\nMay I ask your name?: ")

name_log = open("name-logs.txt", 'a+')
name_log.write(name + "\n\n")
name_log.close()

sleep(1)

print("\nHello, " + name + "! ")

shit = ChatBot('Kix', logic_adapters=['chatterbot.logic.MathematicalEvaluation', 'chatterbot.logic.BestMatch'])

small_talk = ['hi there!',
              'hi!',
              'how do you do?',
              'how are you?',
              'i\'m cool.',
              'fine, you?',
              'always cool.',
              'i\'m ok.',
              'glad to hear that.',
              'i\'m fine.',
              'glad to hear that!',
              'i feel awesome!',
              'excellent, glad to hear that!',
              'not so good.',
              'sorry to hear that.',
              'what\'s your name?',
              'i\'m Kix. ask me a question.']

math_talk1 = ['pythagorean theorem.',
              'a squared plus b squared equals c squared!']

math_talk2 = ['law of cosines',
              'c**2 = a**2 + b**2 - 2 * a * b * cos(gamma)']

list_trainer = ListTrainer(shit)

for item in (small_talk, math_talk1, math_talk2):
    list_trainer.train(item)

corpus_trainer = ChatterBotCorpusTrainer(shit)
corpus_trainer.train('chatterbot.corpus.english')

#_input = input("Say something!: ")


while True:
    try:
        _input = shit.get_response(input())
        print(_input)

    except(KeyboardInterrupt, EOFError, SystemExit):
        break



