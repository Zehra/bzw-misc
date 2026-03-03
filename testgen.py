import os
import sys

"""
Column = 
Edges = Column/2


Formula:

Wall = 



S1


M1


L1
xy
xy
xy
xy

L2
xy
xy
xy
xy

L3
xy
xy
xy
xy

L4
xy
xy
xy
xy


M2
=L2
=L3


S2

M3
L1
xy
xy
xy
xy


L2
xy
xy
xy
xy

Wall as Center Gen

Start
[0][0][1][0][0]
[0]         [0]
[1]         [1]
[0]         [0]
[0][0][1][0][0]

[0][1][1][1][0]
[1]         [1]
[1]         [1]
[1]         [1]
[0][1][1][1][0]

[1][1][1][1][1]
[1]         [1]
[1]         [1]
[1]         [1]
[1][1][1][1][1]


BoxToMesh
X= X*2
Y= Y*2
Z=GroundZ+Z


(60 - (5/2)=2.5)
"""

def genWall(posx, posy, posz):
    # L1
    # Layer 1
    vercount = 0
    print("mesh")
    print("    matref gwall")
    print("    vertex {} {} {} # vertex {}".format(posx+27.5, posy+1.0, posz, vercount))
    vercount += 1
    print("    vertex {} {} {} # vertex {}".format(posx-27.5, posy+1.0, posz, vercount))
    vercount += 1
    print("    vertex {} {} {} # vertex {}".format(posx-27.5, posy-1.0, posz, vercount))
    vercount += 1
    print("    vertex {} {} {} # vertex {}".format(posx+27.5, posy-1.0, posz, vercount))
    vercount += 1
    # L2
    # Layer 2.
    print("    vertex {} {} {} # vertex {}".format(posx+25.0, posy+1.0, posz+5.0, vercount))
    vercount += 1
    print("    vertex {} {} {} # vertex {}".format(posx-25.0, posy+1.0, posz+5.0, vercount))
    vercount += 1
    print("    vertex {} {} {} # vertex {}".format(posx-25.0, posy-1.0, posz+5.0, vercount))
    vercount += 1
    print("    vertex {} {} {} # vertex {}".format(posx+25.0, posy-1.0, posz+5.0, vercount))
    vercount += 1
    # L3
    # Layer 3
    print("    vertex {} {} {} # vertex {}".format(posx+25.0, posy+1.0, posz+10.0, vercount))
    vercount += 1
    print("    vertex {} {} {} # vertex {}".format(posx-25.0, posy+1.0, posz+10.0, vercount))
    vercount += 1
    print("    vertex {} {} {} # vertex {}".format(posx-25.0, posy-1.0, posz+10.0, vercount))
    vercount += 1
    print("    vertex {} {} {} # vertex {}".format(posx+25.0, posy-1.0, posz+10.0, vercount))
    vercount += 1
    # L4
    # Layer 4
    print("    vertex {} {} {} # vertex {}".format(posx+27.5, posy+1.0, posz+15.0, vercount))
    vercount += 1
    print("    vertex {} {} {} # vertex {}".format(posx-27.5, posy+1.0, posz+15.0, vercount))
    vercount += 1
    print("    vertex {} {} {} # vertex {}".format(posx-27.5, posy-1.0, posz+15.0, vercount))
    vercount += 1
    print("    vertex {} {} {} # vertex {}".format(posx+27.5, posy-1.0, posz+15.0, vercount))
    # Start of Faces
    # Pos y face (start)
    print("    face\n        vertices {} {} {} {}\n    endface".format(4, 8, 12, 0))
    print("    face\n        vertices {} {} {} {}\n    endface".format(1, 13, 9, 5))
    print("    face\n        vertices {} {} {} {}\n    endface".format(1, 5, 4, 0))
    print("    face\n        vertices {} {} {} {}\n    endface".format(9, 13, 12, 8))
    # Pos y face (end)

    # Neg y face (start)
    print("    face\n        vertices {} {} {} {}\n    endface".format(3, 15, 11, 7))
    print("    face\n        vertices {} {} {} {}\n    endface".format(6, 10, 14, 2))
    print("    face\n        vertices {} {} {} {}\n    endface".format(3, 7, 6, 2))
    print("    face\n        vertices {} {} {} {}\n    endface".format(11, 15, 14, 10))
    # Neg y face (end)

    # Inner face (start)
    print("    face\n        vertices {} {} {} {}\n    endface".format(4, 5, 6, 7))
    print("    face\n        vertices {} {} {} {}\n    endface".format(11, 10, 9, 8))
    print("    face\n        vertices {} {} {} {}\n    endface".format(7, 11, 8, 4))
    print("    face\n        vertices {} {} {} {}\n    endface".format(5, 9, 10, 6))
    # Inner face (end)

    print("end")

def genBlock(posx, posy, posz):
    v = 0
    print("mesh")
    print("    matref gcolumn")
    # L1
    print("    vertex {} {} {} # vertex {}".format(posx+2.5, posy+2.5, posz, v))
    v += 1
    print("    vertex {} {} {} # vertex {}".format(posx-2.5, posy+2.5, posz, v))
    v += 1
    print("    vertex {} {} {} # vertex {}".format(posx-2.5, posy-2.5, posz, v))
    v += 1
    print("    vertex {} {} {} # vertex {}".format(posx+2.5, posy-2.5, posz, v))
    v += 1
    # L2
    print("    vertex {} {} {} # vertex {}".format(posx+2.5, posy+2.5, posz+15.0, v))
    v += 1
    print("    vertex {} {} {} # vertex {}".format(posx-2.5, posy+2.5, posz+15.0, v))
    v += 1
    print("    vertex {} {} {} # vertex {}".format(posx-2.5, posy-2.5, posz+15.0, v))
    v += 1
    print("    vertex {} {} {} # vertex {}".format(posx+2.5, posy-2.5, posz+15.0, v))
    v += 1
    # face gen
    print("    face\n        vertices {} {} {} {}\n    endface".format(1, 5, 4, 0)) #(0, 4, 5, 1))
    print("    face\n        vertices {} {} {} {}\n    endface".format(2, 6, 5, 1)) #(1, 5, 6, 2))
    print("    face\n        vertices {} {} {} {}\n    endface".format(3, 7, 6, 2)) #(2, 6, 7, 3))
    print("    face\n        vertices {} {} {} {}\n    endface".format(0, 4, 7, 3)) #(3, 7, 4, 0))
    print("end")


i = 0
startz = 0
while i < 20:
    """
    genBlock(-150, -30, startz)
    genWall(-120,-30,startz)
    genBlock(-90, -30, startz)
    genWall(-60,-30,startz)
    genBlock(-30, -30, startz)
    genWall(0,-30,startz)
    genBlock(30, -30, startz)
    genWall(60,-30,startz)
    genBlock(90, -30, startz)
    genWall(120,-30,startz)
    genBlock(150, -30, startz)
    """
    
    genBlock(-150, 30, startz)
    genWall(-120,30,startz)
    genBlock(-90, 30, startz)
    genWall(-60,30,startz)
    genBlock(-30, 30, startz)
    genWall(0,30,startz)
    genBlock(30, 30, startz)
    genWall(60,30,startz)
    genBlock(90, 30, startz)
    genWall(120,30,startz)
    genBlock(150, 30, startz)
    
    i += 1
    startz += 15
