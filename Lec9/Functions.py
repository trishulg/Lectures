def getInput():
    mainString = input("Enter a string : ")
    letterToFind = input("Enter a letter to find in the string : ")
    return mainString, letterToFind


def getCount(mainstring, letterToFind):
    count = 0
    for i in range(len(mainString)):
        if mainstring[i] == letterToFind:
            count += 1
    return count


mainString, letterToFind = getInput()
print(letterToFind + " appears ", getCount(mainString, letterToFind), " times in the string")
