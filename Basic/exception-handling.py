#!/usr/bin/python

import os
# Simple program to open a file and we will capture the error

file1 = "/Users/Arun/Downloads/Run-Book-SitesCope"

# Check if we have read permission
try:
    os.access(file1, os.F_OK)
except (IOError, SyntaxError) as message:
    print("The file is incorrect" + message)
