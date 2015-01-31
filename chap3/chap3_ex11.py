import turtle

wn = turtle.Screen()
alex = turtle.Turtle()

alex.left(45)
for i in range(0,5):
	alex.forward(250)
	alex.left(720/5)


wn._root.mainloop()