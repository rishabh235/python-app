"""Custom module : app.py"""
import os,sys

name="rishabh" #global variable
def greet(ename):
    os.system('cls')
    data=[10,20,"rishabh"] # private variable
    print(type(data))
    print(data)
    emps=[
        {'eno':101,'ename':'rishabh'},
        {'eno':102,'ename':'sinha'}
    ]
    print(type(emps))
    print(emps)
    first,second=(100,200)
    print(first)

if __name__=='__main__':
    greet("kiran")
    sys.exit()
       
