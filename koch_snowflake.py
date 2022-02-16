import turtle


def koch_curve(t, iterations, length, shortening_factor, angle):
    """

    :param t: Turtle instance
    :param iterations: represents the value of n in the image below this list
                       note that n=0 would represent a flat line, which will be the
                       base case in the recursive function
    :param length: the length of each side in our current (sub-) snowflake
    :param shortening_factor: determines the factor by which the side length
           is divided when we create a new sub-snowflake
    :param angle: determines the angle from which the new side emerges
    :return:
    """
    if iterations == 0:
        t.forward(length)
    else:
        iterations = iterations-1
        length = length / shortening_factor

        koch_curve(t, iterations, length, shortening_factor, angle)
        t.left(angle)
        koch_curve(t, iterations, length, shortening_factor, angle)
        t.right(angle * 2)
        koch_curve(t, iterations, length, shortening_factor, angle)
        t.left(angle)
        koch_curve(t,iterations, length, shortening_factor, angle)


t = turtle.Turtle()
t.speed(0)
t.color("blue")
t.hideturtle()

for i in range(3):
    koch_curve(t, 4, 200, 3, 60)
    t.right(120)

turtle.mainloop()
