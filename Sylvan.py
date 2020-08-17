from xor import *
from formatFile import *
from randPass import *
from conversion import *
from readConfig import *
import argparse
from firstAccess import *
import sys
import getpass

VERSION = '1.0.0'

parser = argparse.ArgumentParser()
parser.add_argument('-mP', '--masterPassword', type=str, help='Insert the Master Password to start the software.')
parser.add_argument('-cP', '--configPath', type=str, help='Absolute Path of the config.')
parser.add_argument('-f', '--firstAccess', action='store_true', help='Starts the first-access wizard')
parser.add_argument('-sA', '--showAll', action='store_true', help='Shows all the listed Services and Passwords.')
parser.add_argument('-V', '--verbose', action='store_true', help='Enables verbose output.')
parser.add_argument('-v', '--version', action='version', version=f"Sylvan - Python Crypted Password Storage v{VERSION}")

if __name__ == '__main__':
    args = parser.parse_args()

    if args.firstAccess:
        if not args.configPath:
            print('Please add -cP ABSOLUTECONFIGPATH.syl')
            sys.exit()
        else:
            if not readConfig(args.configPath, 'mp'):
                masterPasswordSetup(args.configPath)

    elif args.showAll:
        masterPassFromUser = getpass.getpass('Write your master password:')
        print('\n\nMASTERPASS')
        masterPass = readConfig(args.configPath, 'mp')
        print('\n\nDATAPATH')
        dataPath = readConfig(args.configPath, 'dp')
        print(dataPath)

        text, hashStr = unformatHash(masterPass)
        masterPass = decrypt(text, hashStr)

        if masterPass == masterPassFromUser:
            print(fetchData(dataPath.strip('\"')))
            