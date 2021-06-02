"""Starting in the top left corner of a 2×2 grid,
and only being able to move to the right and down,
there are exactly 6 routes to the bottom right corner.
How many such routes are there through a 20×20 grid?"""
# Length of any path is equal to the sum of the dimensions ie. 40
# There are 2 possible directions at any point in the path until the path reaches either the bottom or right most edge
# The path can only have reached either edged after 20 moves
# after 20 moves only 2 of the 2 ** 20 paths will have reached either edge
#
