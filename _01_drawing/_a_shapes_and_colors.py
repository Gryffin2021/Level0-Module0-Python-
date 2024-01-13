import turtle

if __name__ == '__main__':
    window = turtle.Screen()
    window.bgcolor('white')

    # This code makes a new Turtle. Pick a new name for the turtle
    timmy = turtle.Turtle()

    # Make your turtle's shape 'turtle', .shape('turtle')
    timmy.shape('turtle')
    # Set your turtle's speed using .speed(2)
    timmy.speed(2)
    # Set your turtle's color using .color('green') and .pencolor('blue')
    timmy.color('green')
    timmy.pencolor('blue')
    # Move your turtle forward using .forward(100)
    # TEST    Did your turtle move forward?
    #timmy.forward(100)
    # Move your turtle left or right using .left(90) or .right(90)
    #timmy.left(90)
    # Now put the forward and left/right code into a for loop to repeat 4 times.
    # TEST    Did your turtle draw a square?
    for i in range(4):
        timmy.forward(100)
        timmy.left(90)
    # Move your turtle to a new place on the screen using .goto(x, y)
    # x=0 and y=0 is the center of the screen
    timmy.goto(150, 150)
    # Have your turtle draw a circle using .circle(radius, steps=30)
    # TEST    Did your turtle draw a circle?
    timmy.begin_fill()
    timmy.circle(100, steps=30)
    # Add color to your shape by adding .begin_fill() before drawing the circle
    # and .end_fill() below
    timmy.end_fill()
    # Draw 3 more shapes with different fill colors!
    timmy.goto(-150, -150)
    timmy.color('red')
    timmy.begin_fill()
    timmy.forward(150)
    timmy.left(120)
    timmy.forward(150)
    timmy.left(60)
    timmy.forward(150)
    timmy.end_fill()
    timmy.goto(150, -150)
    timmy.color('yellow')
    timmy.begin_fill()
    timmy.forward(-150)
    timmy.left(-120)
    timmy.forward(150)
    timmy.left(60)
    timmy.forward(150)
    timmy.end_fill()
    timmy.goto(-150, 150)
    timmy.color('purple')
    timmy.begin_fill()
    timmy.forward(150)
    timmy.left(-120)
    timmy.forward(150)
    timmy.left(60)
    timmy.end_fill()
    # ===================== DO NOT EDIT THE CODE BELOW ============================
    turtle.done()
