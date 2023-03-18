import turtle

# Set up the turtle window
window = turtle.Screen()
window.bgcolor("white")

# Create the turtle for the dancer
dancer = turtle.Turtle()
dancer.shape("circle")
dancer.color("black", "pink")
dancer.penup()

# Draw the head
dancer.goto(0, 100)
dancer.pendown()
dancer.begin_fill()
dancer.circle(50)
dancer.end_fill()

# Draw the body
dancer.penup()
dancer.goto(0, 50)
dancer.pendown()
dancer.begin_fill()
dancer.circle(25)
dancer.end_fill()

# Draw the arms
dancer.penup()
dancer.goto(-30, 75)
dancer.pendown()
dancer.pensize(10)
dancer.right(45)
dancer.forward(50)
dancer.left(90)
dancer.forward(50)
dancer.penup()
dancer.goto(30, 75)
dancer.pendown()
dancer.right(90)
dancer.forward(50)
dancer.left(90)
dancer.forward(50)

# Draw the legs
dancer.penup()
dancer.goto(-20, 0)
dancer.pendown()
dancer.right(45)
dancer.forward(75)
dancer.left(45)
dancer.forward(50)
dancer.penup()
dancer.goto(20, 0)
dancer.pendown()
dancer.right(90)
dancer.forward(75)
dancer.left(90)
dancer.forward(50)

# Hide the turtle when finished
dancer.hideturtle()

# Keep the window open until closed by the user
turtle.done()
