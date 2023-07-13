

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
        words.append(line.rstrip())
  return words
  

def main():
    # print("This program will find words that can be created from a phone number!")
    # phoneNumber = userInput()                # Collect phone number
    letters = initialize("6862377")    # Init phone letter string 

    combos, found, words = [], [], cleanWords()    

    # if "zum" in words:
    #    print("yes zum here")

    createStrings.counter = 0
    createStrings(letters, 0, combos, found, words)    # Recursive permute strings method call

    combos.sort()
    print("unique combos:", len(combos))

    found.sort()
    print(found)
    print("unique words:", len(found))

    print(len(words))
    # print(words)
    
  






def createStrings(letters, index, combos, found, words):  
    for x in range(3):
        if letters not in combos:
            combos.append(letters)

            # with open('words.txt', 'rb', 0) as f:
            #     if binary_search(letters, 0, 10000) != -1:
            #        found.append(letters)



            for i in range(len(letters)):
              for j in range(i + 1, len(letters) + 1):
                if letters[i:j] in words:
                   found.append(letters[i:j])
                  # print(letters[:i], letters[i: j], letters[j:])

            
        
        if index < 6:     
            createStrings(letters, index + 1, combos, found, words)

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