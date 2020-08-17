def toBin(hexStr):
    tempHex = []
    binArr = []
    for char in hexStr:
        tempHex.append(char)
        if len(tempHex) == 2:
            tempHex = ''.join(tempHex)
            binArr.append(bin(int(tempHex, 16))[2:].zfill(7))
            tempHex = []
    return (''.join(binArr))

def toHex(binStr):
    hexArr = []
    tempBin = []
    counter = 1
    for char in binStr:
        # print(char)
        tempBin.append(char)
        if counter % 7 == 0 and counter != 0:
            tempBin = ''.join(tempBin)
            # print('Hex: ', hex(int(tempBin, 2))[2:].zfill(2))
            # print(int(tempBin, 2))
            hexArr.append(hex(int(tempBin, 2))[2:].zfill(2))
            tempBin = []
        counter += 1
    hexVal = ''.join(hexArr)
    # print('HexVal:', hexVal)
    return hexVal