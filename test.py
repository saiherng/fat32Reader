
import os
import sys 
import struct


def main():

    f = open("fat32.img", 'rb')

    print(seekBytes(f,11,2))
    print(getString(f,11,8))



def getString(fs, pos, numBytes):
  fs.seek(pos)
  raw = fs.read(numBytes)
  return struct.unpack(str(numBytes)+"s", raw)[0]

    
    
def seekBytes(f, offset, size):

    f.seek(offset)
    data = f.read(size)

    if (size == 1):
        formatType = "b"
        
    elif (size == 2):
        formatType = "h"
        
    elif (size == 4):
        formatType = "i"
    
    return struct.unpack("<" + formatType, data)[0]


main()
