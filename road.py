import os
import sys

if __name__ == '__main__':
    run = True
    starts = 0
    count = 20
    posstart = 90
    print("mesh")
    while run:
        print("    vertex 20 {} 5".format(posstart))
        print("    vertex 10 {} 5".format(posstart))
        posstart -= 10
        starts += 1
        if starts >= count:
            run = False
            break

    starts = 0
    run = True
    meshfaces = 0
    while run:
        #print("face\n    vertices {} {} {} {}\nendface".format(meshfaces, meshfaces+2,meshfaces+3,meshfaces+1))
        print("face\n    vertices {} {} {} {}\nendface".format(meshfaces+1, meshfaces+3,meshfaces+2,meshfaces))
        starts += 1
        meshfaces += 2
        if starts >= count:
            run = False
            break
    print("end")

