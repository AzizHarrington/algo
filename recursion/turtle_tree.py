import turtle
from random import randint

def tree(branch_len, t):
    if branch_len > 5:
        style_pen(branch_len, t)
        t.pendown()
        t.forward(branch_len)
        t.right(20)
        tree(branch_len-randint(5, 15), t)
        t.left(40)
        tree(branch_len-randint(5, 25), t)
        t.right(20)
        t.penup()
        t.backward(branch_len)


def style_pen(branch_len, t):
    if branch_len > 75:
        t.pensize(10)
        t.color("#663300")
    elif branch_len > 50:
        t.pensize(7)
        t.color("#996633")
    elif branch_len > 25:
        t.pensize(4)
        t.color("#cccc00")
    elif branch_len > 10:
        t.pensize(1)
        t.color("#009900")
    else:
        t.pensize(5)
        t.color("#006600")


def main():
    t = turtle.Turtle()
    my_win = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(200)
    t.down()
    tree(100, t)
    my_win.exitonclick()


main()
