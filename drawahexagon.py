import turtle

turtle.Screen().bgcolor("Purple")
turtle.Screen().setup(400,500)
polygon = turtle.Turtle()


numsides = 6
sidelength = 70
angle = 360 / 6
for i in range (numsides):
    polygon.forward(sidelength)
    polygon.right(angle)
turtle.done()