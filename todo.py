import sys
import os

argLen = len(sys.argv)

if argLen >= 3:
    arg3 = sys.argv[3]
    arg1 = sys.argv[1]
    arg2 = sys.argv[2]


 


def addTask():
    if not os.path.exists(arg1):
        with open(arg1, 'w') as todo:
            todo.write("=========================To-Do List========================\n")
            task = arg2
            todo.write(f"{task}\n")
    else:
        with open(arg1, 'a') as todo:
            task = arg2
            todo.write(f"{task}\n")

def rmTask():
    with open(arg1, 'r') as todo:
        lines = todo.readlines()
        lenLines = len(lines)
    with open(arg1, 'w') as todo:
        task = arg2
        if int(task) <= lenLines:
            lines.pop(int(task))
            todo.writelines(lines)
        else:
            print("Error: task with this number does not exist. Nothing was removed.")

def viewTasks():
    with open(arg1, 'r') as todo:
            lines = todo.readlines()
            lines = [f"{i}. {lines[i]}" for i in range(1,len(lines))]  
            print('\n')
            print("=========================To-Do List========================\n")      
            print("".join(lines))  

##usage: python todo.py <filename> <task> <cmd>
if argLen ==4 and arg3 == 'w':
    addTask()
elif argLen ==3 and arg2 == 'r':
    viewTasks()
elif argLen ==4 and arg3 == 'rm':
    rmTask()
else:
    print("Usage: python todo.py <filename> <task> <cmd>\nTask:to-do line, line number to delete, omit task for read\ncmd: w (write), r (read), rm (remove)")