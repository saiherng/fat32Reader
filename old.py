
"""
File       : project3.py
Authors    : Sai Herng
Description: This program inteprets a FAT32 file system image. 
Date       : 4/18/2018
"""

import os
import sys 
import struct


def main():
        
    if len(sys.argv) > 1:
        argv = sys.argv[1]
        
    else:
##        argv = input("Enter file: ")
          argv = "fat32.img"

    interpret_fat32(argv)


def interpret_fat32(fileName):

    f = open(fileName, 'rb')
   
    info = seekInfo(f)
    rootAddr = getRootAddr(f)
    
     
    while True:

        print("\] ", end="")
        args = input().split()

        if args[0] == "info":
            
            print("BPB_BytesPerSec is %s, %s"% (hex(info[0]),info[0]))
            print("BPB_SecPerClus is %s, %s" % (hex(info[1]),info[1]))
            print("BPB_RsvdSecCnt is %s, %s" % (hex(info[2]),info[2]))
            print("BPB_NumFATs is %s, %s"    % (hex(info[3]),info[3]))
            print("BPB_FATSz32 is %s, %s"    % (hex(info[4]),info[4]))

            

        elif args[0] == "stat":
     
            if len(args) > 1 and args[1] == "root":               
                print("Root Address is %s, %s" %(hex(rootAddr),rootAddr))

            else:
                print("Enter directory as argument for stat command")

        elif args[0] == "ls":

            offset = rootAddr
            directory = []

            
            for i in range(int(info[0]*info[1] / 64) * 2):

                attribute = (seekString(f, offset + 0x0B , 1))

                if attribute == 0x0F:
                    pass

                elif attribute == 0x10:

                    directory = (parseFileName(seekString (f, offset, 8)))
                    print(directory)
                    
                elif attribute == 0x20:
                    
                    highFN = seekString(f, offset, 8)
                    lowFN = seekString(f, offset + 8, 3)
                    print(highFN,lowFN)

         
               
                offset += 32
            

        elif args[0] == "read":
                
            pass 
                  

        elif args[0] == "volume":
        	print("volume")

        elif args[0] == "quit":
            print("Exit")
            break
        
        else:
            print("Invalid Command")


def parseFileName(fileName, fileType):

    if fileType == None:
        return fileName.decode("utf-8")
    else:
        
        fn = fileName.decode("utf-8")
        ft = fileType.decode("utf-8")

        parsed = fn + "." + ft
  
        return parsed.lower().replace(" ","")


def getRootAddr(f):

    info = seekInfo(f)

    BPB_BytesPerSec = info[0]
    BPB_SecPerClus = info[1]
    BPB_RsvdSecCnt = info[2]
    BPB_NumFATs =  info[3]
    BPB_FATSz32 = info[4]


    #Root Address Calculation
    BPB_FATSz16 = seekBytes(f,22,2) 

    if (BPB_FATSz16 != 0):
        FATSz = BPB_FATSz16
    else:
        FATSz = BPB_FATSz32
        

    N = 2
    RootDirSectors = 0   
    FirstDataSector = BPB_RsvdSecCnt + (BPB_NumFATs * FATSz) + RootDirSectors
    FirstSectorofCluster = ((N - 2) * BPB_SecPerClus) + FirstDataSector

    rootAddr = int(BPB_BytesPerSec * FirstSectorofCluster)

    return rootAddr



def seekInfo(f):

    #info display
    BPB_BytesPerSec = seekBytes(f,11,2)
    BPB_SecPerClus = seekBytes(f,13,1)
    BPB_RsvdSecCnt = seekBytes(f,14,2)
    BPB_NumFATs =  seekBytes(f,16,1)
    BPB_FATSz32 = seekBytes(f,36,4)
    
    infoArray = [BPB_BytesPerSec, BPB_SecPerClus, BPB_RsvdSecCnt, BPB_NumFATs, BPB_FATSz32]

    return infoArray

        
def seekBytes(f, offset, size):

    f.seek(offset)
    data = f.read(size)

    if (size == 1):
        formatType = "B"
        
    elif (size == 2):
        formatType = "H"
        
    elif (size == 4):
        formatType = "i"
    
    return struct.unpack("<" + formatType, data)[0]


def seekString(f, offset, size):
    
    f.seek(offset)
    data = f.read(size)

    if size == 1:
        formatType = "b"
        return struct.unpack(formatType, data)[0]
    else:
        formatType = "s"
        return struct.unpack(str(size) + formatType, data)[0]
        

    


main()
    


