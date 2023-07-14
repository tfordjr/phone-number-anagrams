# Terry Ford Project 1 CS 4200SS 07/13/2023

def userInput():           #User Input to collect phone number
  numbers = 2
  while len(str(numbers)) != 7:
    try:
      numbers = int(input("Enter a seven digit phone number without 0 or 1: "))
    except ValueError:
      print("No punctuation!")
    if "0" in str(numbers) or "1" in str(numbers):
      print("No 0's or 1's!")
      numbers = 2
  return numbers


def initialize(numbers):  
  letters = ""
  for num in str(numbers):  # convert phone number into starting letter string
    if num == "8" or num == "9":
      letters += chr(int(num)*3 + 60)
    else:
      letters += chr(int(num)*3 + 59)
  return letters


def cleanWords():
  words = []
  with open('words.txt', 'r') as f: 
    for line in f:
      words.append(line.rstrip().upper())
  return words


def numberize(letters, i, j):
  left = letters[:i]
  right = letters[j:]
  numbers = ""
  for letter in left: # convert left and right substring back to phone numbers
    numbers += str((ord(letter) - 59) // 3)
  left = numbers
  numbers = ""
  for letter in right: # convert left and right substring back to phone numbers
    numbers += str((ord(letter) - 59) // 3)
  right = numbers
  print(left, "-", letters[i: j], "-", right)

# Uses recursion to find all 2,187 unique combinations possible
def createStrings(letters, index, combos, found, words):   
  for x in range(3):                                     
    if letters not in combos:                          
      combos.append(letters)                            
                                                        
      for i in range(len(letters)):     # Linear search surprisingly powerful enough
        for j in range(i + 1, len(letters) + 1): 
          if letters[i:j] not in found and letters[i:j] in words:
            found.append(letters[i:j])
            numberize(letters, i, j)           
    
    if index < 6:     
        createStrings(letters, index + 1, combos, found, words)

    # this iterates only twice to prevent bad combos from being generated
    if x != 3:
      if chr(ord(letters[index]) + 1) != "Q":
        letters = letters[:index] + chr(ord(letters[index]) + 1) + letters[(index + 1):]
      else:
        letters = letters[:index] + chr(ord(letters[index]) + 2) + letters[(index + 1):]

def main():
  print("This program will find words that can be created from a phone number!")
  phoneNumber = userInput()                # Collect phone number
  letters = initialize(phoneNumber)    # Init phone letter string 
  combos, found, words = [], [], cleanWords()    
  
  createStrings.counter = 0
  createStrings(letters, 0, combos, found, words)    # Recursive method call
  
  found.sort()
  print("\n", len(found), "words found!")
  print(found)



main()