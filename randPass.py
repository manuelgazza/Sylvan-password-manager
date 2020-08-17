from random import randint

LC_ASCII = (97, 122)              # from 97 to 122
UC_ASCII = (65, 90)               # from 65 to 90
N_ASCII = (48, 57)                # from 48 to 57
S_ASCII = (33, 47)                # from 33 to 47

def getCharSet(charSet):
    charArr = [False, False, False, False]
    range = ()
    if charSet == '':
        charArr = [True, True, True, True]
    else:
        for char in charSet:
            if str(char).islower():
                charArr[0] = True
            elif str(char).isupper():
                charArr[1] = True
            elif str(char).isnumeric():
                charArr[2] = True
            elif ord(char) >= 33 and ord(char) <= 47:
                charArr[3] = True
    return charArr

def between(sp, num, ep):
    bw = False
    if num >= sp and num <= ep : bw = True
    return bw

def genRandPass(charNum, charSet=''):
    charSet = getCharSet(str(charSet))
    passArr = []
    counter = 0
    while counter < charNum:
        counter += 1
        randChar = randint(33, 122)
        if between(33, randChar, 47) and charSet[3] == True:
            passArr.append(chr(randChar))
        elif between(48, randChar, 57) and charSet[2] == True:
            passArr.append(chr(randChar)) 
        elif between(65, randChar, 90) and charSet[1] == True:
            passArr.append(chr(randChar)) 
        elif between(97, randChar, 122) and charSet[0] == True:
            passArr.append(chr(randChar))
        else:
            counter -= 1
    psw = ''.join(passArr)
    return psw