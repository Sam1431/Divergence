import os
import operator
from time import sleep
from misc import color
from misc import defs

from prologue import narration

#print(color.purple,"WELCOME USER", color.blue)
#sleep(0.05)
#print(' ----------------------------------------------',color.yellow)
#sleep(0.05)
#print(""" You will be given choices for each scene\n and only choosing the correct option\n will lead to the next scene""",color.blue)
#sleep(0.05)
#print(' ----------------------------------------------',color.green)
#sleep(0.05)
#username = input(' Choose a character name for yourself \n > ')

defs.clrscr()

SCREEN_WIDTH = 100
centered = operator.methodcaller('center', SCREEN_WIDTH)
print("")
print(color.blue,centered("██████╗░██╗██╗░░░██╗███████╗██████╗░░██████╗░███████╗███╗░░██╗░█████╗░███████╗"))
sleep(0.05)
print(centered("  ██╔══██╗██║██║░░░██║██╔════╝██╔══██╗██╔════╝░██╔════╝████╗░██║██╔══██╗██╔════╝"))
sleep(0.05)
print(centered("  ██║░░██║██║╚██╗░██╔╝█████╗░░██████╔╝██║░░██╗░█████╗░░██╔██╗██║██║░░╚═╝█████╗░░"))
sleep(0.05)
print(centered("  ██║░░██║██║░╚████╔╝░██╔══╝░░██╔══██╗██║░░╚██╗██╔══╝░░██║╚████║██║░░██╗██╔══╝░░"))
sleep(0.05)
print(centered("  ██████╔╝██║░░╚██╔╝░░███████╗██║░░██║╚██████╔╝███████╗██║░╚███║╚█████╔╝███████╗"))
sleep(0.05)
print(centered("  ╚═════╝░╚═╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝░╚═════╝░╚══════╝╚═╝░░╚══╝░╚════╝░╚══════╝"))

print("")
print (color.purple,centered ("Press Any key to Begin"))
input()

defs.clrscr()
narration.entry()
