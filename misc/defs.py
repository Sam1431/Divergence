from misc import color
import os, platform, time, sys


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
        time.sleep(0.08)


def convo(speech):
    typingPrint(speech)


def convoTitle(speaker, speech):
    print(color.black, "-------------------------")
    print(color.blue, "[", speaker, "]", color.white)
    typingPrint(speech)


def progressBar():
    toolbar_width = 40
    sys.stdout.write("[%s]" % (" " * toolbar_width))
    sys.stdout.flush()
    sys.stdout.write("\b" * (toolbar_width + 1))
    for i in range(toolbar_width):
        time.sleep(0.05)
        sys.stdout.write("-")
        sys.stdout.flush()
    sys.stdout.write("]\n")
