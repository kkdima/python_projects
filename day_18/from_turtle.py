import turtle
import random
import colorgram

# Extract colors from an image
colors = colorgram.extract('./day_18/image.jpg', 10)

# Prepare list of extracted colors and normalize RGB values
rgb_colors = []
for color in colors:
    r = color.rgb.r / 255
    g = color.rgb.g / 255
    b = color.rgb.b / 255
    print(r, g, b)
    rgb_colors.append((r, g, b))

# remove the first background colors from the list
rgb_colors = rgb_colors[2:]


def main():
    # Set up turtle
    screen = turtle.Screen()
    screen.bgcolor("white")
    screen.setup(width=800, height=800)

    t = turtle.Turtle()
    t.speed(0)
    t.penup()  # Prevent drawing lines between movements
    t.hideturtle()

    # Configuration
    dot_size = 10
    gap = 50
    num_dots_x = 10  # Number of dots in the x direction
    num_dots_y = 10  # Number of dots in the y direction

    # Initial position
    start_x = -200
    start_y = -200

    # Draw the dots
    for i in range(num_dots_y):
        for j in range(num_dots_x):
            x = start_x + j * gap
            y = start_y + i * gap
            t.goto(x, y)
            # Random color from extracted colors
            t.dot(dot_size, random.choice(rgb_colors))

    # Finish drawing
    screen.exitonclick()


if __name__ == "__main__":
    main()
