import random

hangman_pics = ['''
   +---+
       |
       |
       |
      ===''', '''
   +---+
   O   |
       |
       |
      ===''', '''
   +---+
   O   |
   |   |
       |
      ===''', '''
   +---+
   O   |
  /|   |
       |
      ===''', '''
   +---+
   O   |
  /|\  |
       |
      ===''', '''
   +---+
   O   |
  /|\  |
  /    |
      ===''', '''
   +---+
   O   |
  /|\  |
  / \  |
      ===''']

words = ["american", "history", "python"]
#secret = random.choice(words)
secret = "american"
print(secret)
secret_list=list(secret)
hidden = []
guesses = 0

for character in secret_list:
    hidden.append("_ ")
print("".join(hidden))

while guesses < len(hangman_pics)-1 and "_ " in hidden:
    while True:
        guess = str.lower(input("Enter a letter: "))

        if guess in ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]: 
            break
    if guess in secret_list:
        for index in range(len(secret_list)):
            if guess == secret_list[index]:
                hidden[index] = guess
        print("".join(hidden))
    else:
        print("That letter is not in here!")
        guesses += 1
        print(hangman_pics[guesses])

if "_ " in hidden:
    print("You lost!")
else:
    print("You win!")
  










