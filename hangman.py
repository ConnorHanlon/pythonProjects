def main():
    hang = ['obsolete', 'touch','ludicrous', 'comma', 'dazzling', 'pets', 'change', 'ghost', 'superb', 'economic', 'callous', 'winter', 'obscene', 'striped', 'border', 'argue', 'lamp', 'torpid', 'bawdy', 'fines']
    import random
    x = random.randint(0, 19)
    rword = hang[x]
    y = len(rword)
    import turtle
    unders = turtle.Turtle()
    unders.hideturtle()
    unders.speed(0)
    gallows = turtle.Turtle()
    gallows.hideturtle()
    gallows.speed(0)
    turtle.hideturtle()
    turtle.penup()
    turtle.speed(0)
    gallow(gallows)
    drawunder(unders)
    drawundnum(unders, y)
    hangman(y, unders, gallows, rword, turtle)


def hangman(y, unders, gallows, rword, turtle):
    hitcount, wincount = 0, 0
    guesseslist =[]
    turtle.goto(50, 100)
    while hitcount < 6 and wincount < y:
        g = turtle.textinput('Enter guess', 'Letter')
        if g not in guesseslist:
            guesseslist += [g]
            unders.goto(-75, -70)
            unders.penup()
            z, nohit = 0, False
            while z < y:
                if g == rword[z]:
                    unders.pendown()
                    unders.write(g)
                    unders.penup()
                    unders.forward(10)
                    z += 1
                    wincount += 1
                    nohit = True
                else:
                    unders.forward(10)
                    z += 1
            if nohit == False:
                drawbody(hitcount, gallows)
                hitcount += 1
    if wincount == y:
        turtle.write('Congratulations!!')
        playagain(turtle)
    else:
        turtle.write('Sorry, you lose!')
        playagain(turtle)


def playagain(turtle):
    p = turtle.textinput('Would you like to play again?', 'Enter "Yes" or "No"')
    turtle.clearscreen()
    if p == 'Yes':
        main()
    else:
        exit()

def drawbody(hitcount, gallows):
    if hitcount == 0:
        drawhead(gallows)
    if hitcount == 1:
        drawtorso(gallows)
    if hitcount == 2:
        drawarm1(gallows)
    if hitcount == 3:
        drawarm2(gallows)
    if hitcount == 4:
        drawleg1(gallows)
    if hitcount == 5:
        drawleg2(gallows)


def drawhead(gallows):
    gallows.right(90)
    gallows.circle(10)
    gallows.left(90)
    gallows.penup()
    gallows.forward(20)

def drawtorso(gallows):
    gallows.pendown()
    gallows.forward(40)
    gallows.backward(25)

def drawarm1(gallows):
    gallows.right(45)
    gallows.forward(15)
    gallows.backward(15)

def drawarm2(gallows):
    gallows.left(90)
    gallows.forward(15)
    gallows.backward(15)
    gallows.right(45)

def drawleg1(gallows):
    gallows.forward(25)
    gallows.right(45)
    gallows.forward(15)
    gallows.backward(15)

def drawleg2(gallows):
    gallows.left(90)
    gallows.forward(15)
    gallows.backward(15)

def gallow(gallows):
    gallows.left(90)
    gallows.forward(200)
    gallows.left(90)
    gallows.forward(100)
    gallows.left(90)
    gallows.forward(50)

def drawundnum(unders, y):
    n = 0
    while n < y:
        unders.pendown()
        unders.forward(5)
        unders.penup()
        unders.forward(5)
        n += 1

def drawunder(unders):
    unders.penup()
    unders.goto(-75, -75)
