import time, sys
from misc import color
from tqdm import tqdm
import os, platform



def died():
    print(color.black, "----------------------------------\n ------------",
          color.red, "YOU DIED", color.black,
          "----------\n ----------------------------------")


def clrscr():
   if platform.system() == 'Windows':
      os.system('cls')
   else:
      os.system('clear')

def typingPrint(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.05)

def convo(speech):
   typingPrint(speech)

def convoTitle(speaker,speech):
   print(color.black,"-------------------------")
   print(color.blue,"[",speaker,"]",color.white)
   typingPrint(speech)