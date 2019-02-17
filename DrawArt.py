from turtle import *
from random import *

#random
def randomColor():
  red = randint(0,255)
  blue = randint(0,255)
  green = randint(0,255)
  color(red,blue,green)
  
def randomPlace():
  penup()
  x = randint(-150,150)
  y = randint(-150,150)
  goto(x, y)
  pendown()
  
def randomHeading():
  setheading(randint(1,360))

#more_shape
def drawRectangle():
  randomColor()
  randomPlace()
  length = randint(10, 150)
  height = randint(10, 150)
  begin_fill()
  forward(length)
  right(90)
  forward(height)
  right(90)
  forward(length)
  right(90)
  forward(height)
  right(90)
  end_fill()
  
def drawCircle():
  randomColor()
  randomPlace()
  dot(randint(1,100))

speed(0.5)

for num in range(3):
  shapeList = ['turtle', 'circle', 'square', 'triangle', 'classic']
  shapeDraw = shapeList[randint(0,4)]
  if shapeDraw == 'circle':
    for i in range(30):
      drawCircle()
  else:
    for i in range(30):
      shape(shapeDraw)
      randomColor()
      randomPlace()
      randomHeading()
      stamp()
  clear()
  setheading(0)

for i in range(30):
      drawRectangle()
  


