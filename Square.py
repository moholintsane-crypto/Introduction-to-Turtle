import turtle

# Create a screen (drawing window or canvas)
wn = turtle.Screen()
wn.bgcolor("light blue") # Optional: set background color
wn.title("Drawing a Square")

# Create a turtle object (pen)
t = turtle.Turtle()
t.pensize(4) # Optional: set pen size
t.color("red") # Optional: set pen color
t.speed('normal')  # You can change speed to 'fastest', 'fast', 'normal', 'slow', or 'slowest'

# Draw a square using a loop
for _ in range(4):
    t.forward(100) # Move forward by 100 steps
    t.left(90)     # Turn left by 90 degrees

# Keep the window open until clicked
turtle.done()