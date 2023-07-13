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



def main():
  print("This program will find words that can be created from a phone number!")
  phoneNumber = userInput()                # Collect phone number
  letters = initialize(phoneNumber)    # Init phone letter string 
  createStrings.counter = 0
  createStrings(letters, 0)    # Recursive permute strings method call

  print(createStrings.counter)


def createStrings(letters, index):       # Recursive method to create all possible combos
  createStrings.counter += 1

  for x in range(2):
    print(letters)          #Print statement equivalent to test for words statements
    if index < 7:
      createStrings(letters, index + 1)

    if index == 1:
      if chr(ord(letters[-index]) + 1) == "Q":
        letters = letters[:-index] + chr(ord(letters[-index]) + 2)
      else:
        letters = letters[:-index] + chr(ord(letters[-index]) + 1)
    else:
      if chr(ord(letters[-index]) + 1) == "Q":
        letters = letters[:-index] + chr(ord(letters[-index]) + 2) + letters[-(index-1):]
      else:
        letters = letters[:-index] + chr(ord(letters[-index]) + 1) + letters[-(index-1):]

  print(letters)       #Print statement equivalent to test for words statements
  if index < 7:
      createStrings(letters, index + 1)

# test all substrings for words and test full 7 letters for word

main()