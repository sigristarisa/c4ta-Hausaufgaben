"""
Schreibe ein Programm, das konzentrische Kreise auf die Seite zeichnet.
Der grösste Kreis soll die Seite ausfüllen, die anderen Kreise sollen regelmässig kleiner werden.
Das Programm soll so geschrieben sein, dass du die Anzahl Kreise über eine Variable verändern kannst, so dass immer noch dieselben Regeln gelten.
"""
size(100, 100)
width = width()
height = height()
diameter = width
repNum = 10
r = 0
b = 1

for i in range(repNum):
    fill(r, 0, b)
    oval(width/2-diameter/2, height/2-diameter/2 ,diameter,diameter)
    diameter -= width/repNum
    b -= 0.1
    r += 0.1