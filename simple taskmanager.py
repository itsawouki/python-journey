import os

readyTasks = ["test1","test2","test3"]
doneTasks = ["test","test2","test3"]
userQuit = False
userChoice = 0
def menu():
    print("-------------------Task Manager-------------------")
    print("1: show tasks\n2: remove task\n3: add task\n4: finish tasks\n5: quit")
    userChoice = int(input("your Choice: "))
    return userChoice


def addtask():

    readyTasks.append(input("input your task: "))


def removetask():
    i = 1
    print("-------------------Remove Tasks-------------------")
    if len(readyTasks) == 0:
        print("you don't have any new task to remove")
    else:
        for task in readyTasks:
            print(i, " " + task)
            i += 1
    remove = int(input("which one do you want to remove? "))
    readyTasks.pop((remove - 1))


def showtasks():
    i = 1
    print("-------------------Ready Tasks-------------------")
    if len(readyTasks) == 0:
        print("you don't have any new task")
    else:
        for task in readyTasks:
            print(i ," " +task)
            i +=1
    print("-------------------Done Tasks-------------------")
    i = 1
    if len(doneTasks)== 0:
        print("you don't have any done task")
    else:
        for task in doneTasks:
            print(i , " " +task)
            i+=1


def finishtasks():
    i = 1

    print("-------------------Finish Tasks-------------------")

    while True:
            i = 1
            if len(readyTasks) == 0:
                print("you don't have any tasks")
            else:
                for task in readyTasks:
                    print(i, " " + task)
                    i += 1
            usertask = int(input("which one do you want to finish? "))
            if usertask == 1000:
                return
            doneTasks.append(readyTasks[usertask-1])
            readyTasks.pop(usertask-1)
            print("input 1000 for quit")



while userQuit != True:
    userChoice = menu()
    if userChoice ==1 :
        showtasks()
    elif userChoice == 2:
        removetask()
    elif userChoice == 3:
        addtask()
    elif userChoice ==4:
        finishtasks()
    elif userChoice == 5:
        print("Goodbye")
        userQuit = True
