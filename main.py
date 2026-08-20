import pathlib as path
import os

def creating():
    try:
        name = input("Enter your file Name:- ")
        path = path(name)
        if not path.exists():
            with open(path,"w") as fs:
                data = input("what do you want to write:- ")
                fs.write(data)
        else:
            print("File exists already")        
    except Exception as err:
        print(f"An error has happend {err}")

def reading():
    try:
        name=input("Enter your file Name:- ")
        path = path(name)
        if path.exists():
            with open(path,"r") as fs:
                print(fs.read())
        else:
            print("The file does'nt exists")
    except Exception as err:
        print(f"An error has happend {err}")

def updating():
    try:
        pass
    except Exception as err:
        pass


def deleting():
    try:
        name = input("Enter your file Name:- ")
        path = path(name)
        if path.exists():
            path.unlink()
            print("File removed")
        else:
            print("File cant be found")    
    except Exception as err:
        print(f"An error has happend {err}")


def user():
    try:
        response = int(input(":- "))
        print("works")
        return response
    except Exception as err:
            print(f"There was a error {err}")
            return 
while True:
    print("press 1 for creating a file")

    print("press 2 for reading a file")

    print("press 3 for updating a file")

    print("press 4 for deleting a file")

    print("press 5 to exit")
    response = user()  


    creating() if response == 1 else ""

    reading() if response == 2 else ""

    updating() if response == 3 else ""

    deleting() if response == 4 else "" 

    if response ==5:
        break



