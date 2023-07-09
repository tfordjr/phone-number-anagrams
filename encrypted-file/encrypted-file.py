# Project 2 CS 4732 SS2023 Terry Ford Jr.
# Sources: https://www.youtube.com/watch?v=gyPuAJfOnGk&t=452s

from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

def menu():
    userInput = 0
    print("You can...\n\t1) Read settings from the settings file.")
    print("\t2) Overwrite settings file.\n\t3) Quit program")
    while userInput != 1 and userInput != 2 and userInput != 3:
        try:
            print("What would you like to do?: ", end="")
            userInput = int(input())
        except ValueError:
            print("Please enter 1-3.")
    return userInput

def main(): 
    # key = get_random_bytes(32)
    # print(key)    # Copied and pasted this from terminal into salt byte string variable
    salt = b'\xc2b\xa1y\xe9 0\x83K4\xbd\xff\x8c&]\x84\xf6L\xc6\xac\x03\xfa\xbdT\xef\xb8\xa6LM\xe8\xb9^'
    password = "waterworld"
    key = PBKDF2(password, salt, dkLen=32)  

    while True:
        match menu():
            case 1:                         
                print("\nDecypting and printing settings.txt")       
                with open('settings.txt', 'rb') as f:
                    iv = f.read(16)
                    ciphertext = f.read()

                cipher = AES.new(key, AES.MODE_CBC, iv=iv)
                plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
                print(plaintext)                
            case 2:               
                plaintext = bytes(input("Overwrite settings.txt: "), 'utf-8')
                cipher = AES.new(key, AES.MODE_CBC)
                ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))

                with open('settings.txt', 'wb') as f:
                    f.write(cipher.iv)
                    f.write(ciphertext)    
            case default:
                quit("Quitting the program...")            

main()