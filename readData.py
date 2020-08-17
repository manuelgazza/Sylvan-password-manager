import os
import sys

def loadFile(path):
    print('in loadfile')
    print(path[-4:])
    if path[-4:] == '.syl':
        print('Loaded the .syl File.')
        with open(path) as syl:
            cfgLines = (syl.readlines())
        cfgLines = [line.split('\n')[0] for line in cfgLines]
        print('CFGLines: ', cfgLines)
    return cfgLines

def readData(dataLines):
    dataDict = {}
    for line in dataLines:
        tempLine = line.split('=>')
        name = tempLine[0].strip('[]')
        data = tempLine[1].split(':')
        text = data[1]
        hashArr = [data[2], data[0]]
        hashStr = ''.join(hashArr)
        print(hashStr)
        dataDict[name] = [text, hashStr]

    # print(dataDict)
    return dataDict

def fetchData(path):
    return readData(loadFile(path))