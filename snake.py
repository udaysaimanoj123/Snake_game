from turtle import Turtle
positions=[(0,0),(-20,0),(-40,0)]

class Snake:

     def __init__(self):
         self.segments=[]
         self.create_snake()
         self.head=self.segments[0]

     def create_snake(self):
         for i in positions:
             self.add_segments(i)

     def add_segments(self,position):
         t = Turtle("square")
         t.penup()
         t.color("white")
         t.goto(position)
         self.segments.append(t)

     def extend(self):
         self.add_segments(self.segments[-1].position())


     def move(self):
         for seg in range(len(self.segments) - 1, 0, -1):
             head_cox = self.segments[seg - 1].xcor()
             head_coy = self.segments[seg - 1].ycor()
             self.segments[seg].goto(head_cox, head_coy)
         self.segments[0].forward(20)

     def restart(self):
         for j in self.segments:
             j.goto(1000,1000)
         self.segments.clear()
         self.create_snake()
         self.head = self.segments[0]

     def Up(self):
         if self.head.heading()!=270:
             self.head.setheading(90)
     def Right(self):
         if self.head.heading() != 180:
             self.head.setheading(0)
     def Left(self):
         if self.head.heading() != 0:
             self.head.setheading(180)
     def Down(self):
         if self.head.heading() != 90:
             self.head.setheading(270)
     def gofood(self,location):
         self.head.goto(location)




