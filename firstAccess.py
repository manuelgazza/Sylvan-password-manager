from xor import *
from saveData import *
import getpass

def masterPasswordSetup(configPath):
    print(
"""
Welcome! This looks like your first access to Sylvan!
Let's set up your master password.
It will be used to access all other passwords from other services so be careful!
""")
    masterPassword = getpass.getpass('Please write there your master password: ')
    masterPasswordRepeat = getpass.getpass('Please repeat the master password: ')
    dataPath = input('Please paste here the absolute path of the data file (.syl): \n')
    if masterPassword == masterPasswordRepeat:
        text, hashStr = encrypt(masterPassword)
        tempDelConfig = open(configPath, 'w')
        tempDelConfig.write('[FIRST_ACCESS]=>False\n')
        tempDelConfig.close()

        appendToFile(configPath, 'MASTER_PASSWORD', text, hashStr)
        appendNotEncrypted(configPath, 'DATA_PATH', dataPath)
        print('Done!')