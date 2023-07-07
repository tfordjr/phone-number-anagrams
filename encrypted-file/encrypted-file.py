import cryptography
import random
# from Crypto.Cipher import AES
# from Crypto.Random import get_random_bytes

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
            
main()