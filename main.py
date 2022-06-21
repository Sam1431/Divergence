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
print("\n\n\n\n\n\n")
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
#print (color.purple,centered ("Press Any key to Begin"))
#input()


ans=True
while ans:
       print(color.green,centered("1      Start Game         1"))
       print(color.blue,centered("2    Load from Saved    2"))
       print(color.red,centered("3       Quit Game         3"))
       ans=input("Choose : ") 
       if ans=="1":
         defs.clrscr()
         print(color.cyan,"Loading Game")
         defs.progressBar()
         defs.clrscr()
         narration.entry()
       elif ans=="2":
         print("feature soon to be added")
       elif ans=="3":
         print("quitting")
         quit()
       elif ans !="":
         print("\n Not Valid Choice Try again")

