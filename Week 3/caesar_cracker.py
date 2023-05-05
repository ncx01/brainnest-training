'''
This program can hack messages encrypted 
with the Caesar cipher from the previous project, even 
if you don't know the key. There are only 26 
possible keys for the Caesar cipher, so a computer can easily try all possible decryptions and display the results to the user. In cryptography, we call 
this technique a brute-force attack.
'''

string = input('Enter the message to decrypt.\n> ')

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Shifts letters in string backwards by amount key
def decrypt(string, key):
    letterList = list(string)
    result = ''

    for letter in letterList:
        try:
            index = alphabet.index(letter.lower())

            # In the case when the index of the decrypted letter is less than 0
            if index - key < 0: 
                index = (index - key) % len(alphabet)
                result += alphabet[index]
            else:
                result += alphabet[index - key]

        # If letter is not in alphabet, it is not decrypted
        except ValueError:
            result += letter

    return result.upper()

print('All the possible decryptions are:')

# Print decrypted result for every possible key
for key in range(26):
    print(decrypt(string, key))