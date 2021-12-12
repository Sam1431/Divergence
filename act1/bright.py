from time import sleep
from misc import color

purity = "impure"

def walk():
  print(">> You slowly walk towards the brightly lit pathway")
def teleport():
  print(color.red,"[ you are teleported to what looks like the hall of fame for the gods ]")
def intro():
  print(color.blue,"[KNITTER]>>",color.white,"  I am the knitter. I've chose a few candidates and placed in similar dungeons to check if they are worthy. The same applies for you")
def flashback():
  print(color.blue,"[KNITTER]>>",color.white," Oh, I forgot to tell bout gods.")
  sleep(3)
  print(color.blue,"[KNITTER]>>",color.white,"At the start of the Universe, \nthere were a total of 5 gods in existence,\nbeings with power to  obliterate universes with a single snap.\nThey were :-\nBeing of Light - Refracta\nBeing of Darkness - Gluttony \nBeing of Control - Nikola \nBeing of Emptyness - Eerie \nThe Great Schemer - Knitter")
  sleep(4)
  
  print(color.blue,"[KNITTER]>>", color.white," As for the worthy part, one of the gods betrayed us and committed taboo by incarnating as a mortal, we need a successor to go against her ")
  sleep(5)
  print(color.blue,'[Player]>>', color.white,'But what about me? I just want to go back to my home')
  sleep(4)             
  print(color.blue,'[KNITTER]>>',color.white,'You shall not, you have been chosen to compete here as a candidate to defeat the mortal god that went and betayed us once upon a time, she lives in the dimension of mortals and only another mortal can possesses the power to beat him!')
  sleep(4)
  print(color.blue,'[Player]>>', color.white,'What do I even get in return? If I get chosen as the candidate and defeat this so called traitor will i get home again?')
  sleep(5)
  print(color.blue,'[KNITTER]>>', color.white, 'Yes you can, and you will be handsomely rewarded as well.')
  sleep(2)
  print(color.blue,'[PLAYER]>>', color.white,'Oh well then, looks like I have no other option..')
  print(color.blue, '[You start blacking out and wake up in a place you dont really know..]')
  print(color.blue, color.blackbg,"-----------------------\n[YOU HAVE COMPLETED ACT 1]\n  -----------------------")

