def convertToString(bite):
    str = bite.decode("utf-8")
    return str
def convertToBytes(str):
    byteStr = bytes(str, 'utf-8')
    return byteStr