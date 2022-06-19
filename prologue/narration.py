from misc.defs import convo, convoTitle, clrscr
from misc import color
from time import sleep


def entry():
    convoTitle(
        "NARRATOR",
        "\n\t The reign of terror had become a reality as \n\t the evil king Xerxes had begun expanding his \n\t kingdom of utter evil."
    )

    sleep(0.5)

    convo(
        "\n\n\t It was the era of wars, a time period in the \n\t Universe where WAR was the answer to everything.\n\t Several kingdoms had begun declaring wars on \n\t each other and conquering territories of each other."
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