import turtle
turtle.Screen().bgcolor("Purple")
turtle.Screen().setup(300,400)
polygon= turtle.Turtle()
number_of_sides = 5
side_length =180
angle= 180 / number_of_sides
for i in range(5):
    polygon.forward(angle)
    polygon.backward(side_length)
    polygon.right(angle)
    polygon.left(side_length)
turtle.done()