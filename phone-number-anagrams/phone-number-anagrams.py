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


def initialize(numbers):         # converts phone number into letter string
  letters = ""
  for num in str(numbers):         
    if num == "8" or num == "9":          # This exists to skip Q and it never reaches z
      letters += chr(int(num)*3 + 60)     # we have 8 nums representing 3 letters each
    else:
      letters += chr(int(num)*3 + 59)
  return letters


def cleanWords():
  words = []
  with open('words.txt', 'r') as f:     # only filereading in whole program
    for line in f:
      words.append(line.rstrip().upper())  # transfers as uppercase and as string 
  return words                             # to prep for string comparison later


def numberize(letters, i, j):
  substrings = [letters[:i], letters[j:]]       # left and right substrings
  for index, string in enumerate(substrings):
    numbers = ""
    for letter in string:
      numbers += str((ord(letter) - 59) // 3)   # substrings become phone numbers again
    substrings[index] = numbers

  print(substrings[0], "-", letters[i: j], "-", substrings[1])

# Uses recursion to find all 2,187 unique combinations possible
def createStrings(letters, index, combos, found, words):   
  for x in range(3):            # each call creates 3 more recursive calls passing
    if letters not in combos:   # unique strings onward until word length is reached
      combos.append(letters)                            
                                                        
      for i in range(len(letters)):        # Linear search surprisingly powerful enough
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
  phoneNumber = userInput()                         # Collect phone number
  letters = initialize(phoneNumber)                 # Init phone letter string 
  combos, found, words = [], [], cleanWords()       
  createStrings(letters, 0, combos, found, words)   # Recursive call
    
  found.sort()
  print("\n", len(found), "words found!")
  print(found)

main()