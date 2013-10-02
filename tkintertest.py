from Tkinter import *

master = Tk()

w = Canvas(master, width=200, height=100)
w.pack()

w.create_line(0, 0, 200, 100)
w.create_line(0, 100, 200, 0, fill="red", dash=(4, 4))
rect = w.create_rectangle(0, 0, 10, 10, fill="blue")

new_x = 10
new_y = 10

def update_square(thisevent):
	try:
		new_x
		new_y
	except:
		print 'error'
		new_x = 0
		new_y = 0
	old_x=new_x
	old_y=new_y
	new_x,new_y=thisevent.x, thisevent.y
	dx = -(old_x - new_x)
	print "dx=", dx
	dy = -(old_y - new_y)
	print "dy=", dy
	w.move(rect, dx, dy)


w.bind("<Motion>", update_square)



mainloop()