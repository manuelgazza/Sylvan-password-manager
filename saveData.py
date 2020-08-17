from formatFile import *
import json

def appendToFile(path, name, text, hashStr):
    syl = open(path, 'a')
    passLine = '[{}]=>{}\n'.format(name.upper(), formatHashed(text, hashStr))
    syl.writelines(passLine)
    syl.close()
    # print(passLine)

def appendNotEncrypted(path, name, text):
    syl = open(path, 'a')
    passLine = '[{}]=>{}\n'.format(name.upper(), text)
    syl.writelines(passLine)
    syl.close()