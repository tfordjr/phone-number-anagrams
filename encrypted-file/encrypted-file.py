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
    print("You can...\n\t1) Read settings from a settings file.\n\t2) Modify the settings in the settings file.\nWhat would you like to do?: ", end="")
    while userInput != 1 and userInput != 2 and userInput != 3 and userInput != 4:
        try:
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
    f = open(r"C:\Users\Terry\All Projects\encryptedSettings\settings.txt", "r+")
    print(f.read())
    ciphertext = encode("File Contents & save to settings") 
    while True:
        if menu() == 1:     
            f = open(r"C:\Users\Terry\All Projects\encryptedSettings\settings.txt", "r")       
            print(f.read())
            decode(ciphertext) # and print plaintext
        else:
            #f = open(r"C:\Users\Terry\All Projects\encryptedSettings\settings.txt", "r+")
                        
            #f.flush()
            
            initial_message = b"" # if you want to set up the file somehow

            tf = r"C:\Users\Terry\All Projects\encryptedSettings\settings.txt"
            tf.write(initial_message)
            tf.flush()
            call([EDITOR, tf.name])

            tf.seek(0)
            edited_message = tf.read()
            print (edited_message.decode("utf-8"))
                


            #call(['EDITOR', r"C:\Users\Terry\All Projects\encryptedSettings\settings.txt"])

            decode(ciphertext) # save back to file and let 
            # user edit file and after he's done encode()

main()