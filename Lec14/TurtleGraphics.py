from turtle import forward, left, right, backward, penup, pendown, pos, goto


def drawTally():
    left(90)
    forward(20)
    backward(20)
    right(90)
    shiftRight()


def shiftRight():
    penup()
    forward(5)
    pendown()

def drawSlash():
    left(90)
    penup()
    forward(3)
    pendown()
    startposition = pos()
    goto(startposition[0]-25, startposition[1]+14)
    penup()
    goto(startposition)
    backward(3)
    right(90)
    pendown()

    # move to the next group
    shiftRight()
    shiftRight()

def drawFive():
    drawTally()
    drawTally()
    drawTally()
    drawTally()
    drawSlash()

def drawTallies(num):
    while num >= 5:
        drawFive()
        num -= 5
    while num >= 1:
        drawTally()
        num -= 1

numberOfTallies = int(input('Enter number of tallies'))
drawTallies(numberOfTallies)

input()
