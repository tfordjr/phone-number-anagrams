

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
    # print("This program will find words that can be created from a phone number!")
    # phoneNumber = userInput()                # Collect phone number
    letters = initialize("6862377")    # Init phone letter string 

    combos, words = [], []
    createStrings.counter = 0
    createStrings(letters, 0, combos, words)    # Recursive permute strings method call

    combos.sort()
    print(len(combos))

    words.sort()
    print(words)
    print(len(words))
    
  






def createStrings(letters, index, combos, words):  
    for x in range(3):
        if letters not in combos:    
            combos.append(letters)

            # with open('words.txt', 'rb', 0) as f:
            #     if binary_search(letters, 0, 10000) != -1:
            #        words.append(letters)

            
        
        if index < 6:     
            createStrings(letters, index + 1, combos, words)

        # iterate only twice
        if x != 3:
            if chr(ord(letters[index]) + 1) != "Q":
                letters = letters[:index] + chr(ord(letters[index]) + 1) + letters[(index + 1):]
            else:
                letters = letters[:index] + chr(ord(letters[index]) + 2) + letters[(index + 1):]





#   if index >= 0:
#       createStrings(letters, index - 1)

# test all substrings for words and test full 7 letters for word

main()