import turtle

# my_screen = turtle.getscreen()
def my_ex():
    aturtle = turtle.Screen()
    my_turtle = turtle.Turtle()

    my_turtle.pendown()
    my_turtle.goto(23,78)
    my_turtle.forward(15)
    
    my_turtle.home()
    #my_turtle.done()
    turtle.mainloop()

my_ex()