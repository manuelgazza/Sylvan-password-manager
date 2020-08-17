from random import randint
from conversion import *

def xor(cipher, hashStr):
    encryptedArr = []
    encrypted = ''
    for num in range(len(cipher)):
        # print(int(cipher[num])^int(hashStr[num]))
        encryptedArr.append(str(int(cipher[num])^int(hashStr[num])))
    encrypted = ''.join(encryptedArr)
    return encrypted

def encrypt(text):
    cipher = []
    hashArr = []
    hashStr = ''
    cipherStr = ''
    textLen = len(text)

    for char in text:
        rand = randint(0, 63)
        hashArr.append(bin(rand)[2:].zfill(7))
        # print(char, '=', bin(ord(char))[2:].zfill(7))
        cipher.append(bin(ord(char))[2:].zfill(7))
        # print(cipher)
    cipherStr = ''.join(cipher)
    hashStr = ''.join(hashArr)
    # print(cipherStr)

    # print('Hash: ', hashStr)
    # print('Text: ', cipherStr)

    encryptedText = toHex(xor(cipherStr, hashStr))
    encryptedHash = toHex(hashStr)
    
    return encryptedText, encryptedHash

def decrypt(text, hash):
    binTemp = []
    binArr = []
    charArr = []

    binText = toBin(text)
    binHash = toBin(hash)

    binMsg = xor(binText, binHash)
    for bit in binMsg:
        binTemp.append(bit)
        if len(binTemp) == 7:
            binArr.append(''.join(binTemp))
            binTemp = []
    for char in binArr:
        charArr.append(chr(int(char, 2)))
    return (''.join(charArr))