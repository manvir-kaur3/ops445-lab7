#!/usr/bin/env python3
# Student ID: 115583221

def function1():
    global schoolName
    schoolName = 'SICT'  # This modifies the global variable
    print('print() in function1 on schoolName:', schoolName)

def function2():
    global schoolName
    schoolName = 'SSDO'  # This modifies the global variable
    print('print() in function2 on schoolName:', schoolName)

schoolName = 'Seneca'
print('print() in main on schoolName:', schoolName)
function1()
print('print() in main on schoolName:', schoolName)
function2()
print('print() in main on schoolName:', schoolName)
