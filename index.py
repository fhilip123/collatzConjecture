startNum = int(input('Starting Number :'))
digits = 0
tof = True
currentNum = 0
collatzList = []


def collatz(x):
    # gets the next number
    if (x % 2) == 0:
        return x/2
    if (x % 2) != 0:
        return (x * 3) + 1


currentNum = startNum
while tof:
    # makes sure the 4 2 1 pattern shows up
    if len(collatzList) > 2:
        if collatzList[len(collatzList) - 1] == 2:
            tof = False

    collatzList.append(currentNum)
    currentNum = int(collatz(currentNum))


print(collatzList)
