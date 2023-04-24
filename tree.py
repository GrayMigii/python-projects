#!/usr/bin/env python3

import random
import turtle

tur = turtle.Turtle()

# turtle configurations
tur.speed(0)
tur.hideturtle()
tur.color('brown')
tur.penup()
tur.goto(0, -250)
tur.pendown()

global initialBranchSize
initialBranchSize = 8
initialBranchLength = 150


def branch(size, length, direction):
    tur.pensize(size)
    tur.setheading(direction)
    tur.forward(length)


def leaf(radius):
    tur.color('green')
    tur.begin_fill()
    tur.circle(radius)
    tur.end_fill()
    tur.color('brown')


def tree(size, length, startingPos=()):
    if size == initialBranchSize:
        branch(size, length, 90)
        startingPos = [tur.position()]
        tree(size*(5/6), length*0.85, startingPos)
    elif size > initialBranchSize/4:
        for pos in startingPos:
            tur.penup()
            tur.goto(pos[0], pos[1])
            tur.pendown()
            positions = []
            for i in range(random.randint(1, 5)+1):
                branch(size, length, random.randint(1, 10)*18)
                leaf(10-(10-size))
                positions.append(tur.position())
                tur.penup()
                tur.goto(pos[0], pos[1])
                tur.pendown()
            leaf(10-(10-size))
        tree(size*(5/6), length*0.85, positions)
    else:
        pass


tree(initialBranchSize, initialBranchLength)
turtle.done()
