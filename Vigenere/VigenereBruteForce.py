def userInput():
  ciphertext = str(input("Enter the ciphertext message: "))  # collect data
  plaintext = str(input("Enter the known plaintext: "))
  texts = [ciphertext, plaintext]

  for index, string in enumerate(texts):    # data cleaning
    string = string.replace(" ", "")
    string = string.upper()
    newString = ""
    for element in string:
      if(element.isalpha()):
        newString += element
    texts[index] = newString
  return texts


def decode(ciphertext, key):
  plaintext = ""                            # decoding
  for element in range(0, len(ciphertext)):
    plaintext += chr((ord(ciphertext[element]) - ord(key[element % len(key)]) - 130) % 26 + 65)
  return plaintext


def main():
  [ciphertext, knownPlaintext] = userInput()                    # data collection and cleaning
  maxKey = int(input("Enter the max size of the key possible: "))
  print("Brute Forcing", ciphertext, "for known plaintxt", knownPlaintext, "up to key length", maxKey)

  from itertools import product         # importing tools
  from string import ascii_uppercase
  import sys

  for keyL in range(1, maxKey + 1):      # iterating through key sizes
    print("iterating through all keys of size", keyL,"...")
    for combo in product(ascii_uppercase, repeat=keyL):   # iterating possible keys
      possibleKey = ''.join(combo)
      possiblePlaintext = decode(ciphertext, possibleKey)
      #print(possiblePlaintext, possibleKey)
      if knownPlaintext in possiblePlaintext:
        print("Possible Plaintext found:", possiblePlaintext, "with key", possibleKey)
        choice = input("Enter to continue, Q to quit: ")
        if (choice == 'q' or choice == 'Q'):
          sys.exit()
    print("All possible keys of size", keyL, "have been evaluated. Would you like to continue brute force?")
    choice = input("Enter to continue, q to quit: ")
    if (choice == 'q' or choice == 'Q'):
      sys.exit()

main()