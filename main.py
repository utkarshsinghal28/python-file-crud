from pathlib import Path as pa

def creating():
    try:
        name = input("Enter your file Name:- ")
        path = pa(name)
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
        path = pa(name)
        if path.exists():
            with open(path,"r") as fs:
                print(fs.read())
        else:
            print("The file does'nt exists")
    except Exception as err:
        print(f"An error has happend {err}")

def updating():
    try:
        name = input("please tell your file name :- ")
        path = pa(name)

        if path.exists():
            print("operations ")
            print("1 . Renaming the file ")
            print("2 . Appending the content")
            print("3 . Overwriting the file ")

            choice = int(input("Enter your option :- "))

            if choice == 1:
                newname = input("tell your new file name:- ")
                new_path = pa(newname)
                if not new_path.exists():
                    path.rename(new_path)
                    print("renamed successfully ")
                else:
                    print("file already exists")
            
            elif choice == 2:
                with open(path,'a') as fs:
                    data = input("what do you want to append :- ")
                    fs.write(data)
                print("successfully appended")
            
            elif choice == 3:
                with open(path , "w") as fs:
                    data = input("what do you want to overwrite :- ")
                    fs.write("\n"+data)
                print("successfully overwrittten")
            else:
                print("The option doesnt exit")    

        else:
            print("The file does'nt exit")

    except Exception as err:
        print(f"An error has happened {err}")


def deleting():
    try:
        name = input("Enter your file Name:- ")
        path = pa(name)
        if path.exists():
            path.unlink()
            print("File removed")
        else:
            print("File cant be found")    
    except Exception as err:
        print(f"An error has happend {err}")


def user():
    try:
        response = int(input("\ntell your response:- "))
        return response
    except Exception as err:
        print(f"There was a error {err}")


while True:
    print("press 1 for creating a file")

    print("press 2 for reading a file")

    print("press 3 for updating a file")

    print("press 4 for deleting a file")

    print("press 5 to exit")
    response = user()  


    if response == 1:
        creating()
    elif response == 2:
        reading()
    elif response == 3:
        updating()
    elif response == 4:
        deleting()
    elif response == 5:
        break
    else:
        print("Invalid option")



