"""
Generiere eine beliebige Anzahl Rechtecke, die von vollflächig nach links unten regelmässig kleiner werden. 
Versuche nun, eine Farbabstufung zu programmieren: von blau (grösstes Rechteck) zu rot (kleinstes Rechteck).
"""

size(100, 100)
rectSize = 100
repNum = 10
r = 0
b = 1

for i in range(repNum):
    stroke(1)
    fill(r, 0, b)
    rect(0,0,rectSize,rectSize)
    rectSize -= width()/repNum
    b -= 0.1
    r += 0.1