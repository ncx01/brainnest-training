'''
The Caesar cipher is an ancient encryption algorithm used by Julius Caesar. It 
encrypts letters by shifting them over by a 
certain number of places in the alphabet. We 
call the length of shift the key. For example, if the 
key is 3, then A becomes D, B becomes E, C becomes 
F, and so on. To decrypt the message, you must shift 
the encrypted letters in the opposite direction. This 
program lets the user encrypt and decrypt messages 
according to this algorithm.

When you run the code, the output will look like this:

Do you want to (e)ncrypt or (d)ecrypt?
> e
Please enter the key (0 to 25) to use.
> 4
Enter the message to encrypt.
> Meet me by the rose bushes tonight.
QIIX QI FC XLI VSWI FYWLIW XSRMKLX.


Do you want to (e)ncrypt or (d)ecrypt?
> d
Please enter the key (0 to 26) to use.
> 4
Enter the message to decrypt.
> QIIX QI FC XLI VSWI FYWLIW XSRMKLX.
MEET ME BY THE ROSE BUSHES TONIGHT.
'''

temp = input('Do you want to (e)ncrypt or (d)ecrypt?\n> ')
key = input('Please enter the key (0 to 25) to use.\n> ')

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(string, key):
    letterList = list(string)
    result = ''
    for letter in letterList:
        try:
            index = alphabet.index(letter.lower())
            if index + key > len(alphabet):
                index = (index + key) % len(alphabet)
                result += alphabet[index]
            else:
                result += alphabet[index + key]
        except ValueError:
            result += letter
    return result.upper()

def decrypt(string, key):
    letterList = list(string)
    result = ''
    for letter in letterList:
        try:
            index = alphabet.index(letter.lower())
            if index - key < 0:
                index = (index - key) % len(alphabet)
                result += alphabet[index]
            else:
                result += alphabet[index - key]
        except ValueError:
            result += letter
    return result.upper()

if temp.lower() == 'e':
    string = input('Enter the message to encrypt.\n> ')
    print(encrypt(string, int(key)))
elif temp.lower() == 'd':
    string = input('Enter the message to decrypt.\n> ')
    print(decrypt(string, int(key)))