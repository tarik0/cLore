# AUTHOR:Tarık Kızıltan 2017 / Turkey
# QUOTATION:http://stackoverflow.com/questions/287871/print-in-terminal-with-colors-using-python
import time

class colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    STOP = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def slowPrint(slowString,slowInt):
    slowString = str(slowString)
    slowInt = float(slowInt)
    slowForEOF = len(slowString)
    slowForEOFInt = 0
    for slowString2 in slowString:
        if (slowForEOF-slowForEOFInt==1):
            print(slowString2)
        else:
            slowForEOFInt = slowForEOFInt + 1
            print(slowString2,end='',flush=True)
            time.sleep(slowInt)

def color(colorString):
    colorString = str(colorString)
    if (colorString == "RED"):
        print(colors.RED,end = '' ,flush=True)
    if (colorString == "GREEN"):
        print(colors.GREEN, end = '', flush=True)
    if (colorString == "BOLD"):
        print(colors.BOLD, end = '', flush=True)
    if (colorString == "UNDERLINE"):
        print(colors.UNDERLINE, end = '', flush=True)
    if (colorString == "HEADER"):
        print(colors.HEADER, end = '', flush=True)
    if (colorString == "BLUE"):
        print(colors.BLUE, end = '', flush=True)
    if (colorString == "STOP"):
        print(colors.STOP, end = '', flush=True)

def asciiArtFile(asciiArtStringFile, asciiArtSeconds):
    asciiArtStringFile = str(asciiArtStringFile)
    asciiArtSeconds = float(asciiArtSeconds)
    asciiArtFile = open(asciiArtStringFile, "r")
    for asciiFileString in asciiArtFile.readlines():
        print(asciiFileString,end='',flush=True)
        time.sleep(asciiArtSeconds)


color("RED");print(r"Author:Tarık Kızıltan / 2017 / Turkey / cLore.py More Visual Terminal v1");color("STOP")
print("\n")
print(colors.YELLOW+"How to use:"+colors.STOP)
print("""\nfirst add "from cLore import *" to your project""")
print("""\nasciiArtFile("path/to/your/ascii/art",<seconds to delay>) : Writes ascii art in your file.""")
print("""\ncolor(<color>):Printes colors options:RED,UNDERLINE,BOLD,BLUE,STOP,GREEN,HEADER USAGE: color("RED");print("hi");color("STOP")\nor print(colors.RED+"Hi"+colors.STOP)""")
print("""\nslowPrint("string",<seconds to delay>)\n""")

menu = input(colors.GREEN+"cLore"+colors.STOP+">")
exec(menu)
