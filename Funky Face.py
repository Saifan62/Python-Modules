from turtle import *
class Face:
    def __init__(self,xpos,ypos):
        self.size = 90
        self.coord= (xpos,ypos)
    def setsize(self,radius):
        self.size = radius
    def draw(self):
        self.gohome()
        pensize(3)
        speed(0)
        self.drawoutline()
        self.draweye(135)
        self.draweye(45)
        self.drawmouth()
        self.drawnose()
        pensize(5)
    def gohome(self):
        penup()
        goto(self.coord)
        setheading(0)
    def drawoutline(self):
        penup()
        forward(self.size)
        left(90)
        pendown()
        circle(self.size)
        self.gohome()
    def draweye(self,angle):
        penup()
        left(angle)
        forward(self.size/2.5)
        pendown()
        dot(self.size/10)
        self.gohome()
    def drawmouth(self):
        penup()
        right(135)
        forward(self.size/1.7)
        left(90)
        pendown()
        circle(self.size/1.7,90)
        self.gohome()
    def drawnose(self):
        dot(self.size/6, "grey")
        self.gohome()
f1 = Face(0,0)
f1.draw()
showturtle()
done()



