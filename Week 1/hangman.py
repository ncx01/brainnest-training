'''
The hangman game is a word guessing game where the player is given a word and has to guess the letters that make up the word. 
The player is given a certain number of tries (no more than 6 wrong guesses are allowed) to guess the correct letters before the game is over.
'''

# Output
'''
You have 6 tries left.                                                                                                                                           
Used letters:                                                                                                                                                    
Word: _ _ _ _                                                                                                                                                    
Guess a letter: a 

You have 6 tries left.                                                                                                                                           
Used letters: a                                                                                                                                                  
Word: _ a _ a                                                                                                                                                    
Guess a letter: j    

You have 6 tries left.                                                                                                                                           
Used letters: j a                                                                                                                                                
Word: j a _ a                                                                                                                                                    
Guess a letter: v                                                                                                                                                
You guessed the word java !
'''

# Changes the colour of text to red and then back to the default colour
def printError(error):
    print(f'{FAIL}{error}{ENDC}')

FAIL = '\033[91m'
ENDC = '\033[0m'
OKGREEN = '\033[92m'

wordToGuess = 'java'
lettersToGuess = list(wordToGuess)
wrongCounter = 0
guessedLetters = ['_']*len(lettersToGuess)
usedLetters = []

while wrongCounter < 6 and guessedLetters != lettersToGuess:

    print(f'\nYou have {6 - wrongCounter} tries left.')
    print(f'Used letters: {" ".join(usedLetters)}')
    print(f'Word: {" ".join(guessedLetters)}')
    
    newLetter = input('Guess a letter: ')
    
    # Check if input is longer than 1 digit
    if len(list(newLetter)) > 1:
        printError('Enter just one letter.')
        wrongCounter += 1
        continue
    
    # Check if input has already been guessed
    if newLetter in usedLetters:
        printError(f'Letter {newLetter} already used.')
        wrongCounter += 1
        continue
    
    usedLetters.append(newLetter)

    # Reveal letter if guess is correct
    if newLetter in lettersToGuess:
        for i in range(len(lettersToGuess)):
            if newLetter == lettersToGuess[i]:
                guessedLetters[i] = newLetter
    else:
        wrongCounter += 1
        printError(f'{newLetter} is not a letter in the word.')

    # Check if all letters in word have been guessed
    # If the nummber of wrong guesses reaches 6, print 'Game over.'
    if guessedLetters == lettersToGuess:
        print(f'{OKGREEN}You guessed the word {wordToGuess}!{ENDC}')
    elif wrongCounter == 6:
        printError('Game over.')