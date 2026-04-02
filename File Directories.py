import os
import sys


def DirectoryWatcher(path):
    flag = os.path.isabs(path)
    if flag == False:
        path = os.path.abspath(path)
    exists = os.path.isdir(path)
    if exists:
        for foldername, subfolder, filename in os.walk(path):
            print("current folder is ", foldername)
            for subf in subfolder:
                print("Sub folder of " + foldername + "is " + subf)
            for filen in filename:
                print("file inside " + foldername, "is : " + filen)
            print(" ")
    else:
        print("invaild path")


def main():
    argv = sys.argv
    print("Application name : " + argv[0])
    if argv[1] == "-h" or (argv[1] == "-H"):
        print("this script is used to traverse the specific directory")
        exit()
    if argv[1] == "-u" or (argv[1] == "-U"):
        print("usage of application absolute_directory")
        exit()
    try:
        DirectoryWatcher(argv[1])
    except ValueError:
        print("Error: invaild data input")
    except Exception:
        print("error invaild input")


if __name__ == "__main__":
    main()
