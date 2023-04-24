#!/usr/bin/env python3

import turtle

tur = turtle.Turtle()
tur.speed(0)
tur.color('blue')
tur.pensize(1)
turtle.screensize(canvwidth=10000, canvheight=10000)


def fractal(direction=0, count=0, coefficient=0):
    if count <= 576:
        tur.setheading(direction)
        tur.forward(25)
        if count % 576 == 0:
            coefficient += 1
        fractal((direction-(coefficient*360))+(1.25*count), count+1)
    else:
        return False


fractal()


turtle.done()
