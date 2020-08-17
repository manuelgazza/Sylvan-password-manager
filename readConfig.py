from readData import *

def readConfig(path, spec=None):
    """
    path -> The absolute path to the config.syl file
    spec -> fa: Checks if First Access
            mp: Outputs Master Password
            dp: Data Absolute Path
    """
    FIRST_ACCESS = False
    MASTER_PASSWORD = ''
    DATA_PATH = ''

    cfgLines = loadFile(path)
    print('cfgLines: ', cfgLines)
    cfgDict = {}
    for line in cfgLines:
        tempLine = line.split('=>')
        name = tempLine[0].strip('[]')
        data = tempLine[1]

        if name == 'FIRST_ACCESS':
            if data == 'True':
                FIRST_ACCESS == True
        elif name == 'MASTER_PASSWORD':
            MASTER_PASSWORD = data
        elif name == 'DATA_PATH':
            DATA_PATH = data
        else:
            print('{}: Config Value not recognized.')
        
    if not spec:
        return [FIRST_ACCESS, MASTER_PASSWORD, DATA_PATH]
    elif str(spec).lower() == 'mp':
        return MASTER_PASSWORD
    elif str(spec).lower() == 'fa':
        return FIRST_ACCESS
    elif str(spec).lower() == 'dp':
        print('DATA_PATH:', DATA_PATH)
        return DATA_PATH