import os

import re


# list files

def listFiles(dirPath):
    fileList = []

    for root, dirs, files in os.walk(dirPath):

        for fileObj in files:
            fileList.append(os.path.join(root, fileObj))

    return fileList


def findString(filePath, regex):
    fileObj = open(filePath, 'r')
    print(fileObj)
    for eachLine in fileObj:

        if re.search(regex, eachLine, re.I):
            print(fileObj)

            break


def main():
    fileDir = r'D:\wxn\实验软件&纪要'
    regex = r'加速度'

    fileList = listFiles(fileDir)
    print(fileList)
    for fileObj in fileList:
        findString(fileObj, regex)

    os.system("pause")


if __name__ == '__main__':
    main()
