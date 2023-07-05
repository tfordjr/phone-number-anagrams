import cryptography
import csv
import sys, tempfile, os
import editor
import subprocess
import random, string
from subprocess import call

EDITOR = os.environ.get('EDITOR', 'vim')

def menu():
    userInput = 0
    print("You can...\n\t1) Read settings from the settings file.\n\t2) Append to the settings file.\n\t3) Delete and rewrite the settings file.\n\t4) Quit the program")
    while userInput != 1 and userInput != 2 and userInput != 3 and userInput != 4:
        try:
            print("What would you like to do?: ", end="")
            userInput = int(input())
        except ValueError:
            print("Please enter 1 or 2.")
    return userInput

def encode(plaintext):
    pass
    #print("encoding ", plaintext)

def decode(ciphertext):
    pass
    #print("decoding ", ciphertext)

def main():
    f = open(r"C:\Users\Terry\All Projects\encrypted-file\settings.txt", "r")
    print(f.read())
    ciphertext = encode("File Contents & save to settings") 
    while True:
        match menu():
            case 1:    # read   
                f = open(r"C:\Users\Terry\All Projects\encrypted-file\settings.txt", "r")       
                print("\nDecypting and printing settings.txt")
                print(f.read())
                #decode(ciphertext) # and print plaintext
            case 2:    # append
                print("Appending settings.txt")
                #f = open(r"C:\Users\Terry\All Projects\encrypted-file\settings.txt", "r+")
            case 3:    # rewrite
                print("Rewriting settings.txt")
                #f = open(r"C:\Users\Terry\All Projects\encrypted-file\settings.txt", "r+")
            case 4:    # quit
                print("Quitting the program...")
                quit()
            case default:
                pass            
                        
                        
            
                            


            

main()