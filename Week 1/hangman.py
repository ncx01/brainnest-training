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
def printError(error):
    print(f'{FAIL}{error}{ENDC}')

wordToGuess = 'java'
lettersToGuess = list(wordToGuess)
FAIL = '\033[91m'
ENDC = '\033[0m'
OKGREEN = '\033[92m'
wrongCounter = 0
guessedLetters = ['_']*len(lettersToGuess)
usedLetters = []

while wrongCounter < 6 and guessedLetters != lettersToGuess:

    print(f'\nYou have {6 - wrongCounter} tries left.')
    print(f'Used letters: {" ".join(usedLetters)}')
    print(f'Word: {" ".join(guessedLetters)}')
    
    newLetter = input('Guess a letter: ')
    
    if len(list(newLetter)) > 1:
        printError('Enter just one letter.')
        wrongCounter += 1
        continue

    if newLetter in usedLetters:
        printError(f'Letter {newLetter} already used.')
        wrongCounter += 1
        continue
    
    usedLetters.append(newLetter)

    if newLetter in lettersToGuess:
        for i in range(len(lettersToGuess)):
            if newLetter == lettersToGuess[i]:
                guessedLetters[i] = newLetter
    else:
        wrongCounter += 1
        printError(f'{newLetter} is not a letter in the word.')

    if guessedLetters == lettersToGuess:
        print(f'{OKGREEN}You guessed the word {wordToGuess}!{ENDC}')
    elif wrongCounter == 6:
        printError('Game over.')

# Create repository on Git and give him the link