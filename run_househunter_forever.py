#!/usr/bin/python
from subprocess import Popen
while True:

    print("\nStarting househunter.py")
    p = Popen("python3 househunter.py", shell=True)
    p.wait()