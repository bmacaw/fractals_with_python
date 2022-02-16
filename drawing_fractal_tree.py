# This is a place to practice creating fractals with python using info from
# https://towardsdatascience.com/creating-fractals-with-python-d2b663786da6
# by Dhanesh Budhrani
import turtle

MINIMUM_BRANCH_LENGTH = 5  # Sets the minimum threshold to create further sub-branches


def build_tree(t, branch_length, shorten_by, angle):
    """

    :param t: Turtle instance
    :param branch_length: the current length of the branch in pixels
    :param shorten_by: determines by how many pixels the sub-branches will be shorter than the parent branch
    :param angle: the angles from which the sub-branches emerge from the parent branch
    :return:
    """
    if branch_length > MINIMUM_BRANCH_LENGTH:
        t.forward(branch_length)
        new_length = branch_length - shorten_by

        t.left(angle)
        build_tree(t, new_length, shorten_by, angle)

        t.right(angle * 2)
        build_tree(t, new_length, shorten_by, angle)

        t.left(angle)
        t.backward(branch_length)


tree = turtle.Turtle()
tree.hideturtle()
tree.setheading(90)
tree.color('green')

build_tree(tree, 50, 5, 30)
turtle.mainloop()
