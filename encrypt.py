import string
import random

def encrypt(text, shift, substitution_key):
    alphabet = string.ascii_lowercase
    result = ""

    for char in text:
        if char.islower():
            index = alphabet.index(char)
            shifted = alphabet[(index + shift) % 26]
            result += substitution_key[alphabet.index(shifted)]
        elif char.isupper():
            lower = char.lower()
            index = alphabet.index(lower)
            shifted = alphabet[(index + shift) % 26]
            result += substitution_key[alphabet.index(shifted)].upper()
        else:
            result += char

    return result

originalText = input("Enter the text to encrypt: ")
shiftValue = int(input("Enter the shift value: "))

alphabet = list(string.ascii_lowercase)
random.shuffle(alphabet)
substitutionKey = "".join(alphabet)

encryptedText = encrypt(originalText, shiftValue, substitutionKey)
print("Substitution key:", substitutionKey)
print("Encrypted text:", encryptedText)
