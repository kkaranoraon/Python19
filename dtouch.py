#!/usr/bin/env python2
# import the os module
import os

# detect the current working directory and print it
path = os.getcwd()  
print ("The current working directory is %s" % path)

folder = raw_input("enter folder name : ")

file = path + '/'+ folder

try:  
    os.mkdir(file)
except OSError:  
    print ("Creation of the directory %s failed" % path)
else:  
    print ("Successfully created the directory %s " % path)


