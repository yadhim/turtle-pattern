import turtle
import random

def draw_shape(sides, size):
    angle = 360 / sides
    for _ in range(sides):
        turtle.forward(size)
        turtle.right(angle)

def draw_pattern():
    # Setup screen
    screen = turtle.Screen()
    screen.bgcolor("red")
    screen.title("Geometric Pattern Generator")
    
    # Setup turtle
    artist = turtle.Turtle()
    artist.speed(2)  # Fastest speed
    artist.pensize(4)
    
    # Get user input
    try:
        complexity = int(turtle.numinput("Pattern Complexity", 
                                        "Enter complexity level (3-12):", 
                                        default=7, minval=3, maxval=12))
    except:
        complexity = 7
    
    size = 100
    rotations = 360 // complexity
    
    # Draw pattern
    for i in range(rotations):
        # Change color
        r = random.random()
        g = random.random()
        b = random.random()
        artist.pencolor(r, g, b)
        
        draw_shape(complexity, size)
        artist.right(360 / rotations)
    
    artist.hideturtle()
    turtle.done()

if __name__ == "__main__":
    draw_pattern()