import turtle
from random import randint

def tree(branch_len, t):
    if branch_len > 5:
        style_pen(branch_len, t)
        t.pendown()
        # randomly set branch len
        forward_distance = randint(branch_len-10, branch_len+10)
        t.forward(forward_distance)
        # randomly set angle
        angle = randint(10, 20)
        t.right(angle)
        tree(branch_len-randint(5, 15), t)
        t.left(angle*2)
        tree(branch_len-randint(5, 25), t)
        t.right(angle)
        t.penup()
        t.backward(forward_distance)


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
    t.backward(400)
    t.down()
    tree(100, t)
    my_win.exitonclick()


main()
