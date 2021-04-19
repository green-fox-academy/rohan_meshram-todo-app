import sys
from typing import TextIO

f: TextIO

def read_file(file_name, mode):
    count = 1
    with open(file_name, mode) as f:
        if mode == "r":
            for f_contents in f:
                print(str(count) + "- " + f_contents)
                count += 1
            return f_contents

def append_element(file_name, mode):
    with open(file_name, mode) as f:
        if mode == "a":
            append = sys.argv[2] + "\n"
            f_contents = f.write(append)
            return f_contents

def remove_element(file_name, mode):
    with open(file_name, mode) as f:
        if mode == "r+":
            data = f.readlines()
            todo_index = int(sys.argv[2]) - 1
            if sys.argv[1] == "-r":
                remove_element = data[todo_index]
                data.remove(remove_element)
                f.seek(0)
                f.truncate()
                f_contents = f.writelines(data)
                return f_contents

def check_element(file_name, mode):
    with open(file_name, mode) as f:
        if mode == "r+":
            data = f.readlines()
            todo_index = int(sys.argv[2]) - 1
            if sys.argv[1] == "-c":
                count_2 = 0
                for f_contents in range(len(data)):
                    if count_2 == todo_index:
                        data[f_contents] = "[ x ]" + data[f_contents]
                    count_2 += 1
                f.seek(0)
                f.truncate()
                f_contents = f.writelines(data)
                return f_contents

if len(sys.argv) < 2:
    print("$ todo" "\n"
          "Command Line Todo application" "\n"
          "=============================" "\n"
          "                             " "\n"
          "Command line arguments:" "\n"
          "   -l   Lists all the tasks" "\n"
          "   -a   Adds a new task" "\n"
          "   -r   Removes an task" "\n"
          "   -c   Completes an task""\n")

elif sys.argv[1] == "-l":
    if len(sys.argv) < 3:
        read_file("list.txt", "r")
    elif len(sys.argv) < 4:
        print("Invalid Selection, don't have to provide any value after -l ")

elif sys.argv[1] == "-a":
    if len(sys.argv) < 3:
        print("Unable to add: no task provided")
    elif len(sys.argv) < 4:
        append_element("list.txt", "a")

elif sys.argv[1] == "-r":
    if len(sys.argv) < 3:
        print("Unable to remove: no index provided")
    elif len(sys.argv) < 4:
        remove_element("list.txt", "r+")

elif sys.argv[1] == "-c":
    if len(sys.argv) < 3:
        print("Unable to check: no index provided")
    elif len(sys.argv) < 4:
        check_element("list.txt", "r+")
