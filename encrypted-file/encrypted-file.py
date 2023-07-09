# import cryptography
# import random
# import hashlib
# from Crypto import Random

from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

# key = get_random_bytes(32)
# print(key)

salt = b'\xc2b\xa1y\xe9 0\x83K4\xbd\xff\x8c&]\x84\xf6L\xc6\xac\x03\xfa\xbdT\xef\xb8\xa6LM\xe8\xb9^'
password = "mypassword"

key = PBKDF2(password, salt, dkLen=32)

message = b"German Shepherd, 120, 3.4"

cipher = AES.new(key, AES.MODE_CBC)
ciphered_data = cipher.encrypt(pad(message, AES.block_size))

with open('settings.txt', 'wb') as f:
    f.write(cipher.iv)
    f.write(ciphered_data)

with open('settings.txt', 'rb') as f:
    iv = f.read(16)
    decrypt_data = f.read()

cipher = AES.new(key, AES.MODE_CBC, iv=iv)
original = unpad(cipher.decrypt(decrypt_data), AES.block_size)
print(original)

# def encode(plaintext):

#     pass

    
#     #print("encoding ", plaintext)

# def decode(ciphertext):
#     pass
#     #print("decoding ", ciphertext)

def menu():
    userInput = 0
    print("You can...\n\t1) Read settings from the settings file.\n\t2) Append to the settings file.\n\t3) Overwrite the settings file.\n\t4) Quit the program")
    while userInput != 1 and userInput != 2 and userInput != 3 and userInput != 4:
        try:
            print("What would you like to do?: ", end="")
            userInput = int(input())
        except ValueError:
            print("Please enter 1-4.")
    return userInput

def main():
    f = open(r"C:\Users\Terry\All Projects\encrypted-file\settings.txt", "r")
    print(f.read())
    ciphertext = encode("File Contents & save to settings") 
    f.close()
    while True:
        match menu():
            case 1:   
                f = open(r"C:\Users\Terry\All Projects\encrypted-file\settings.txt", "r")       
                print("\nDecypting and printing settings.txt")
                print(f.read())
                #decode(ciphertext) # and print plaintext
                f.close()
            case 2:  
                print("Appending settings.txt")
                f = open(r"C:\Users\Terry\All Projects\encrypted-file\settings.txt", "a")
                f.write(input("What would you like to append to settings.txt?: "))
                f.close()
            case 3:    
                print("Rewriting settings.txt")
                f = open(r"C:\Users\Terry\All Projects\encrypted-file\settings.txt", "r+")
                f.write(input("What would you like overwrite settings.txt with?: "))
                f.close()
            case 4:    
                print("Quitting the program...")
                quit()
            case default:
                pass 
            
#main()