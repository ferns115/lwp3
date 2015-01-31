import turtle

fern=turtle.Turtle()
wn=turtle.Screen()
wn.bgcolor("lightgreen")


fern.shape("turtle")
fern.color("blue")

poo=turtle.Turtle()
poo.color("blue")

fern.penup()
poo.penup()

for i in range(0,12):
	fern.forward(150)
	fern.stamp()
	fern.setposition(0,0)
	fern.left(30)

	poo.forward(100)
	poo.stamp()
	poo.setposition(0,0)
	poo.left(30)

wn._root.mainloop()

