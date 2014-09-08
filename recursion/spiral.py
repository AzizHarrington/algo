import turtle

my_turtle = turtle.Turtle()
my_win = turtle.Screen()

def draw_spiral(my_turtle, linelen):
    if linelen > 0:
        my_turtle.forward(linelen)
        my_turtle.right(20)
        draw_spiral(my_turtle, linelen-1)


draw_spiral(my_turtle, 100)
my_win.exitonclick()
