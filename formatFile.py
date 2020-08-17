def formatHashed(text, hashStr):
    tempHalfHash = []
    splitHash = []
    counter = 1
    if len(hashStr) % 2 == 0:
        while counter <= len(hashStr):
            tempHalfHash.append(hashStr[counter - 1])
            if counter == (len(hashStr) / 2) or counter == len(hashStr):
                splitHash.append(''.join(tempHalfHash))
                tempHalfHash = []
            counter += 1
    else:
        print('Hash Error.')
    formatted = '{}:{}:{}'.format(splitHash[1], text, splitHash[0])
    return formatted

def unformatHash(hashed):
    hashedStr = hashed.split(':')
    hashStr = '{}{}'.format(hashedStr[2], hashedStr[0])
    print('hashStr:', hashStr)

    return hashedStr[1], hashStr