from misc.defs import convo, convoTitle, clrscr
from misc import color
from time import sleep


def entry():
    convoTitle(
        "Commander",
        "\n\t General Sean , Lord Xerxes has issued order to attack Qeltar "
    )

    sleep(0.5)

    convo(
        "\n\n\t I know you're against this entire conquering and \n\t stuff but this is the only way stop a massacre from Happening. \n\t You don't want our lord to kill everyone on the planet now, \n\t do you ?"
    )

    input("\n\n[Any Key to Continue] ")

    clrscr()
    convoTitle(
        "PROLOGUE",
        "\n\t Planet Qeltar, \n\t Home to the well known magic wielding tribe, the Larrs. \n\t A planet located in the altar stellar system"
    )
    convo(
        "\n\n\t Qeltar was a rather peaceful planet who decided \n\t to be neutral in the war."
    )

    sleep(0.5)
    print(color.red, "")
    convo(
        """\n\n\t█▄▄ █░█ ▀█▀   █▄░█ █▀█ ▀█▀   █▀▀ █░█ █▀▀ █▀█ █▄█ █▀█ █▄░█ █▀▀   █░█░█ ▄▀█ █▄░█ ▀█▀ █▀   █▀█ █▀▀ ▄▀█ █▀▀ █▀▀
    █▄█ █▄█ ░█░   █░▀█ █▄█ ░█░   ██▄ ▀▄▀ ██▄ █▀▄ ░█░ █▄█ █░▀█ ██▄   ▀▄▀▄▀ █▀█ █░▀█ ░█░ ▄█   █▀▀ ██▄ █▀█ █▄▄ ██▄"""
    )

    input("\n\n[Any Key to continue] ")

    clrscr()
    convoTitle(
        "XERXES",
        "\t Finally !!, My quest to conqueror magic is close to complete than ever \n")
    convo(
        "\t Commander. How much more time till announcement ?\n")
    sleep(2)
    convoTitle(
        "Commander",
        "\t 2 min sire\n")
    sleep(2)
    convoTitle(
        "XERXES",
        "\t AHHH, I can't wait for my conquest")
    
    buffer()