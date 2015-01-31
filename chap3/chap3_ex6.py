import turtle

fern = turtle.Turtle()
wn = turtle.Screen()

for i in range(0,3):
	fern.forward(100)
	fern.left(120)

for i in range(0,4):
	fern.forward(100)
	fern.left(90)

for i in range(0,6):
	fern.forward(100)
	fern.left(60)

for i in range(0,8):
	fern.forward(100)
	fern.left(180-1080/8)

wn._root.mainloop()