import os
import sys
import time
import json

string = "hello world!"

# create file to store string in output directory
with open("output/log.txt", "w") as f:
    f.write(string)


