from graphics import *
def main():
	win = GraphWin("Awesome Window!", 400, 400)
	segments = 5.0
	win.setCoords(0.0, 0.0, segments, segments)
	Text(Point(segments/2, segments/2),'awesome!').draw(win)
	for i in range(5):
		Line(Point(i,0), Point(i,segments)).draw(win)
		Line(Point(0,i), Point(segments,i)).draw(win)

	Entry(Point(segments/2, segments/4), 10).draw(win)


	p1 = win.getMouse()
	p1.draw(win)
	p2 = win.getMouse()
	p2.draw(win)
	p3 = win.getMouse()
	p3.draw(win)

	triangle = Polygon(p1,p2,p3)
	triangle.setFill("cyan")
	triangle.setOutline("cyan")
	triangle.draw(win)

	win.getMouse()

main()
