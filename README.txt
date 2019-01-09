"""
File       : project3.py
Authors    : Sai Herng
Description: This program inteprets a FAT32 file system image. 
Date       : 4/18/2018
"""

File Directory
-----------------

1. project3.py
2. README.txt


Instructions for compiling program
------------------------------------

> python3 project3.py fat32.img      ---> This step is opening a fat32.img file to interpret


Instructions for running program
------------------------------------
Program runs automatically if input file is given. If not, the program prompts for a file name. 


Challenges Encountered
------------------------------------

It was very confusing to understand which sector and clusters to actually look into, therefore it becomes a huge problem trying to understand how the calcuation works.

The first submission of the program, the calcuation functions should have been more modular.


The program is still in progress of building the FAT directory structure. After this directory is built, it should be so much easier to implement read and ls. 

This is the first time I have seek






Sources
-----------------------------------
https://docs.python.org/2/library/struct.html  