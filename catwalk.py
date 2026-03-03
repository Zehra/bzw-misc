import os
import sys

def vrtxgn(x, y, z, num):
    vrt = "    vertex {} {} {}    #vertex {}".format(x,y,z,num)
    return vrt

def sqrfc(v1, v2, v3, v4, comment):
    sqr = "face\n    vertices {} {} {} {} # {}\nendface".format(v1, v2, v3, v4, comment)
    return sqr



#L1:
#Inner4:low
#    v0 = vrtxgn(xpos+xsize, ypos+ysize, zpos, 0) # +x +y z
#    v1 = vrtxgn(xpos+xsize, ypos-ysize, zpos, 1) # +x -y z
#    v2 = vrtxgn(xpos-xsize, ypos-ysize, zpos, 2) # -x -y z
#    v3 = vrtxgn(xpos-xsize, ypos+ysize, zpos, 3) # -x +y z
#Outer4:low
#    v0 = vrtxgn(xpos+xsize, ypos+ysize, zpos, 4) # +x +y z
#    v1 = vrtxgn(xpos+xsize, ypos-ysize, zpos, 5) # +x -y z
#    v2 = vrtxgn(xpos-xsize, ypos-ysize, zpos, 6) # -x -y z
#    v3 = vrtxgn(xpos-xsize, ypos+ysize, zpos, 7) # -x +y z
#L2:
#Inner4:up
#    v0 = vrtxgn(xpos+xsize, ypos+ysize, zpos, 8) # +x +y z
#    v1 = vrtxgn(xpos+xsize, ypos-ysize, zpos, 9) # +x -y z
#    v2 = vrtxgn(xpos-xsize, ypos-ysize, zpos, 10) # -x -y z
#    v3 = vrtxgn(xpos-xsize, ypos+ysize, zpos, 11) # -x +y z
#Outer4:up
#    v0 = vrtxgn(xpos+xsize, ypos+ysize, zpos, 12) # +x +y z
#    v1 = vrtxgn(xpos+xsize, ypos-ysize, zpos, 13) # +x -y z
#    v2 = vrtxgn(xpos-xsize, ypos-ysize, zpos, 14) # -x -y z
#    v3 = vrtxgn(xpos-xsize, ypos+ysize, zpos, 15) # -x +y z
#
#
#
#
#




if __name__ == '__main__':
    initPosInner = 14
    initPosOuter = 15
    initSizeZ=2
    initPosX=-285
    initPosY=0
    initPosZ=15
    
    while initPosX <= 285:
        print("mesh")
        #inner (lower)
        print(vrtxgn((initPosX + initPosInner), (initPosY + initPosInner), initPosZ, 0))
        print(vrtxgn((initPosX + initPosInner), (initPosY - initPosInner), initPosZ, 1))
        print(vrtxgn((initPosX - initPosInner), (initPosY - initPosInner), initPosZ, 2))
        print(vrtxgn((initPosX - initPosInner), (initPosY + initPosInner), initPosZ, 3))
        #outer (lower)
        print(vrtxgn((initPosX + initPosOuter), (initPosY + initPosOuter), initPosZ, 4))
        print(vrtxgn((initPosX + initPosOuter), (initPosY - initPosOuter), initPosZ, 5))
        print(vrtxgn((initPosX - initPosOuter), (initPosY - initPosOuter), initPosZ, 6))
        print(vrtxgn((initPosX - initPosOuter), (initPosY + initPosOuter), initPosZ, 7))
        #inner (upper)
        print(vrtxgn((initPosX + initPosInner), (initPosY + initPosInner), (initPosZ + initSizeZ), 8))
        print(vrtxgn((initPosX + initPosInner), (initPosY - initPosInner), (initPosZ + initSizeZ), 9))
        print(vrtxgn((initPosX - initPosInner), (initPosY - initPosInner), (initPosZ + initSizeZ), 10))
        print(vrtxgn((initPosX - initPosInner), (initPosY + initPosInner), (initPosZ + initSizeZ), 11))
        #outer (upper)
        print(vrtxgn((initPosX + initPosOuter), (initPosY + initPosOuter), (initPosZ + initSizeZ), 12))
        print(vrtxgn((initPosX + initPosOuter), (initPosY - initPosOuter), (initPosZ + initSizeZ), 13))
        print(vrtxgn((initPosX - initPosOuter), (initPosY - initPosOuter), (initPosZ + initSizeZ), 14))
        print(vrtxgn((initPosX - initPosOuter), (initPosY + initPosOuter), (initPosZ + initSizeZ), 15))
        #Now print faces of the platform mesh
        print(sqrfc(0, 1, 2, 3, "bottom middle section (lower)\nmatref inner"))
        print(sqrfc(3, 2, 1, 0, "bottom middle section (upper)\nmatref inner"))
        # Sides x (outer/inner)
        print(sqrfc(4, 7, 15, 12, "+/- x +y z(outer)\nmatref outer"))
        print(sqrfc(3, 0, 8, 11, "+/- x +y z (inner)\nmatref outer"))
        print(sqrfc(1, 2, 10, 9, "+/- x -y z (inner)\nmatref outer"))
        print(sqrfc(13, 14, 6, 5, "+/- x -y z(outer)\nmatref outer"))
        # Sides (upper)
        print(sqrfc(15, 14, 10, 11, "-x +/-y z(upper)\nmatref outer"))
        print(sqrfc(13, 12, 8, 9, "+x +/-y z(upper)\nmatref outer"))
        print(sqrfc(12, 15, 11, 8, "+/-x +y z(upper)\nmatref outer"))
        print(sqrfc(10, 14, 13, 9, "+/-x -y z(upper)\nmatref outer"))
        # Sides (lower)
        print(sqrfc(1, 0, 4, 5, "+x +/-y z(lower)\nmatref outer"))
        print(sqrfc(0, 3, 7, 4, "+/-x +y z(lower)\nmatref outer"))
        print(sqrfc(1, 5, 6, 2, "+/-x -y z(lower)\nmatref outer"))
        print(sqrfc(6, 7, 3, 2, "-x +/-y z(lower)\nmatref outer"))
        # Sides y (outer/inner)
        print(sqrfc(2, 3, 11, 10, "-x +/-y z(inner)\nmatref outer"))
        print(sqrfc(0, 1, 9, 8, "+x +/-y z(inner)\nmatref outer"))
        print(sqrfc(12, 13, 5, 4, "+x +/-y z(outer)\nmatref outer"))#4, 5, 13, 12, ""))
        print(sqrfc(14, 15, 7, 6, "-x +/-y z(outer)\nmatref outer"))#(6, 7, 15, 14, "-x +/-y z(outer)"))
        # Upper sides
        print(sqrfc(8, 9, 10, 11, "top middle section (lower)\nmatref inner"))
        print(sqrfc(11, 10, 9, 8, "top middle section (upper)\nmatref inner"))
        # end of mesh
        print("end")
        initPosX += 30

#    v0 = vrtxgn(xpos+xsize, ypos+ysize, zpos, 0) # +x +y z
#    v1 = vrtxgn(xpos+xsize, ypos-ysize, zpos, 1) # +x -y z
#    v2 = vrtxgn(xpos-xsize, ypos-ysize, zpos, 2) # -x -y z
#    v3 = vrtxgn(xpos-xsize, ypos+ysize, zpos, 3) # -x +y z
#    # ^Above 'z' position are bottom coordinates of mesh 'box'.
#    v4 = vrtxgn(xpos+xsize, ypos+ysize, zpos+zsize, 4) # +x +y +z
#    v5 = vrtxgn(xpos+xsize, ypos-ysize, zpos+zsize, 5) # +x -y +z
#    v6 = vrtxgn(xpos-xsize, ypos-ysize, zpos+zsize, 6) # -x -y +z
#    v7 = vrtxgn(xpos-xsize, ypos+ysize, zpos+zsize, 7) # -x +y +z
#yspo = sqrfc(0, 3, 7, 4, "Positive y outside face")
#    yspi = sqrfc(4, 7, 3, 0, "Positive y inside face")
