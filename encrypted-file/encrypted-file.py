# Project 2 CS 4732 SS2023 Terry Ford Jr.
# Sources: https://www.youtube.com/watch?v=gyPuAJfOnGk&t=452s

from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

# key = get_random_bytes(32)
# print(key)

def menu():
    userInput = 0
    print("You can...\n\t1) Read settings from the settings file.\n\t2) Overwrite the settings file.\n\t3) Append the settings file.\n\t4) Quit the program")
    while userInput != 1 and userInput != 2 and userInput != 3 and userInput != 4:
        try:
            print("What would you like to do?: ", end="")
            userInput = int(input())
        except ValueError:
            print("Please enter 1-4.")
    return userInput

def main(): 

    salt = b'\xc2b\xa1y\xe9 0\x83K4\xbd\xff\x8c&]\x84\xf6L\xc6\xac\x03\xfa\xbdT\xef\xb8\xa6LM\xe8\xb9^'
    password = "mypassword"
    key = PBKDF2(password, salt, dkLen=32)  

    while True:
        match menu():
            case 1:                         
                print("\nDecypting and printing settings.txt")       
                with open('settings.txt', 'rb') as f:
                    iv = f.read(16)
                    decrypt_data = f.read()

                cipher = AES.new(key, AES.MODE_CBC, iv=iv)
                original = unpad(cipher.decrypt(decrypt_data), AES.block_size)
                print(original)                
            case 2:               
                message = bytes(input("Overwrite settings.txt: "), 'utf-8')
                cipher = AES.new(key, AES.MODE_CBC)
                ciphered_data = cipher.encrypt(pad(message, AES.block_size))

                with open('settings.txt', 'wb') as f:
                    f.write(cipher.iv)
                    f.write(ciphered_data)                
            case 3:    
                message = bytes(input("Append settings.txt: "), 'utf-8')
                cipher = AES.new(key, AES.MODE_CBC)
                ciphered_data = cipher.encrypt(pad(message, AES.block_size))

                with open('settings.txt', 'a') as f:
                    f.write(cipher.iv)
                    f.write(ciphered_data)  
            case 4:    
                print("Quitting the program...")
                quit()
            case default:
                pass 
            
main()