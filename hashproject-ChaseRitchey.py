# Hashing script written by Chase Ritchey
# Some code from StackOverflow and https://nitratine.net/blog/post/how-to-hash-files-in-python/

import sys
import hashlib
from tkinter import Tk     
from tkinter.filedialog import askopenfilename

print("This application will open a file and will create a hash of that file.")
print("It will display the file and then create SHA1 hash.")
print("Please select a file to hash.")

Tk().withdraw() 
filename = askopenfilename() 

BLOCK_SIZE = 65536

#SHA1 hashing
hashfile = hashlib.sha1()
with open(filename, 'rb') as f:
    fb = f.read(BLOCK_SIZE)
    while len(fb) > 0:
        hashfile.update(fb)
        fb = f.read(BLOCK_SIZE)

#MD5 hashing
#hashfilemd5 = hashlib.md5()
#with open(filename, 'rb') as f:
    #fb = f.read(BLOCK_SIZE)
    #while len(fb) > 0:
        #hashfile.update(fb)
        #fb = f.read(BLOCK_SIZE)

#SHA256 hashing
#hashfile256 = hashlib.sha256()
#with open(filename, 'rb') as f:
    #fb = f.read(BLOCK_SIZE)
    #while len(fb) > 0:
        #hashfile.update(fb)
        #fb = f.read(BLOCK_SIZE)

print("The file you selected is", filename)
#print("This is the MD5 hash of the selected file:", hashfilemd5.hexdigest())
print("This is the SHA1 hash of the selected file:", hashfile.hexdigest())
#print("This is the SHA256 hash of the selected file:", hashfile256.hexdigest())
