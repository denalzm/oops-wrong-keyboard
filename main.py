# Low Quality Phonetic Transliteration Service
# Version 1.0
# @denalz#9606
# 2022/01/25 - 2022/01/27

import math, random, io, time
from english import latinContent
from russian import *

VNUM = 1.0

def main():
    print("\n\nDefinitely A Translation Service")
    print("Version number: " + str(VNUM))
    print("Type \"quit\" to exit at any time.")
    choice = "poopy"
    while choice.lower() != "quit":
        choice = input("Enter your input string: ")
        if choice == "quit":
            print("In Russian that would be \"квуит\"\n\n")
            exit(0)
        elif choice == "":
            print("Please enter something!")
        elif latinContent(choice) > 0.5:
            print("Latin alphabet detected. Assuming English pronunciations...")
            print("In Russian that would be: ")
            print(cyrillicizeEnglish(choice))
            print()
        else:
            print("Could not recognize input language. Please try again.\n")
    print("This should never print")

main()
