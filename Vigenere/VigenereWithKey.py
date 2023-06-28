def encode(msg, key):
  print("Encoding message", msg, "with key", key)
  ciphertext = ""                          # encoding
  for element in range(0, len(msg)):
    ciphertext += chr((ord(msg[element]) + ord(key[element % len(key)]) - 130) % 26 + 65)
  print(ciphertext)
  return ciphertext


def decode(ciphertext, key):
  print("Decrypting message", ciphertext, "with key", key)
  plaintext = ""                            # decoding
  for element in range(0, len(ciphertext)):
    plaintext += chr((ord(ciphertext[element]) - ord(key[element % len(key)]) - 130) % 26 + 65)
  print(plaintext)
    

def userInput():
  msg = str(input("Please enter a plaintext message: "))  # collect data
  key = str(input("Enter a key: "))  
  texts = [msg, key]

  for index, string in enumerate(texts):    # data cleaning
    string = string.replace(" ", "")
    string = string.upper()
    newString = ""
    for element in string:
      if(element.isalpha()):
        newString += element
    texts[index] = newString        
  return texts

def main():
  texts = userInput() 
  [msg, key] = texts

  ciphertext = encode(msg, key)
  decode(ciphertext, key)

main()