import turtle
turtle.Screen().setup(800,800)
turtle.Screen().bgcolor("Yellow")
side=int(input("Enter the number of sides you want!"))
angle=360/side
length=int(input("Please enter the length of the side"))
polygon=turtle.Turtle()
for i in range(side):
    polygon.forward(length)
    polygon.right(angle)
turtle.done()    