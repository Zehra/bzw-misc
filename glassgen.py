import os
import sys
import string

def vrtxgn(x, y, z, num):
    vrt = "    vertex {} {} {}    #vertex {}\n".format(x,y,z,num)
    return vrt

def sqrfc(v1, v2, v3, v4, comment):
    sqr = "face\n    vertices {} {} {} {} # {}\nendface\n".format(v1, v2, v3, v4, comment)
    return sqr

def genMeshBox(posX, posY, posZ, sizeX, sizeY, sizeZ, meshcomment):
    # TBH, we'll just convert things here and make it a single mesh.
    xpos = posX
    ypos = posY
    zpos = posZ
    
    xsize = sizeX
    ysize = sizeY
    zsize = sizeZ
    #
    insidex = xpos
    insidey = ypos
    insidez = zpos + (zsize / 2)
    inside = "    inside {} {} {} #Inside point for mesh\n".format(insidex, insidey, insidez)
    # Mesh vertex points.
    v0 = vrtxgn(xpos+xsize, ypos+ysize, zpos, 0) # +x +y z
    v1 = vrtxgn(xpos+xsize, ypos-ysize, zpos, 1) # +x -y z
    v2 = vrtxgn(xpos-xsize, ypos-ysize, zpos, 2) # -x -y z
    v3 = vrtxgn(xpos-xsize, ypos+ysize, zpos, 3) # -x +y z
    # ^Above 'z' position are bottom coordinates of mesh 'box'.
    v4 = vrtxgn(xpos+xsize, ypos+ysize, zpos+zsize, 4) # +x +y +z
    v5 = vrtxgn(xpos+xsize, ypos-ysize, zpos+zsize, 5) # +x -y +z
    v6 = vrtxgn(xpos-xsize, ypos-ysize, zpos+zsize, 6) # -x -y +z
    v7 = vrtxgn(xpos-xsize, ypos+ysize, zpos+zsize, 7) # -x +y +z
    # We'll test coordinates.
    meshs = "mesh\n{}{}{}{}{}{}{}{}".format(v0,v1,v2,v3,v4,v5,v6,v7)
    #^ Mesh start and coordinates in space.
    # Below we add all the faces of the mesh.
    ctopo = sqrfc(7, 6, 5, 4, "Top outside face")
    # x pos side
    xspo = sqrfc(4, 5, 1, 0, "Positive x outside face")
    # x neg side
    xsno = sqrfc(3, 2, 6, 7, "Negative x outside face")
    # y pos side
    yspo = sqrfc(0, 3, 7, 4, "Positive y outside face")
    # y neg side
    ysno = sqrfc(2, 1, 5, 6, "Negative y outside face")
    # bottom outside face, bottom inside face.
    cboto = sqrfc(0, 1, 2, 3, "Bottom outside face")
    #
    # Code for mesh faces.
    # c = cube
    # bot/top/[]sp/[]sn = bottom, top, []side (x/y) positive, []side (x/y) negative
    # o/i = outside face, inside face
    meshe = "{}{}{}{}{}{}{}{}end".format(meshcomment, inside,ctopo,xspo,xsno,yspo,ysno,cboto)
    print("{}{}".format(meshs, meshe))



def genWinPanelSixX(posx, posy, posz):
    winPanelThickness=1
    winPanelBorderSize=2
    winPanelSize=8
    matrefWin = "\nmatref window\n"
    matrefWinPanel = "\nmatref windowPanel\n"
    
    panelPos1x = (posx + winPanelBorderSize + (winPanelSize * 2))
    panelPos2x = posx
    panelPos3x = (posx - winPanelBorderSize - (winPanelSize * 2))
    panelHeightPos1 = (posz + winPanelBorderSize)
    panelHeightPos2 =  (posz + (winPanelBorderSize * 2) + (winPanelSize * 2))
    # Reason the math is confusing is since we are using a box for a base, hence the confusion.
    #Part 1 Windows:
    genMeshBox(panelPos1x, posy, panelHeightPos1, winPanelSize, (winPanelThickness / 2), (winPanelSize * 2), matrefWin)
    genMeshBox(panelPos2x, posy, panelHeightPos1, winPanelSize, (winPanelThickness / 2), (winPanelSize * 2), matrefWin)
    genMeshBox(panelPos3x, posy, panelHeightPos1, winPanelSize, (winPanelThickness / 2), (winPanelSize * 2), matrefWin)
    # Part 2 Windows:
    genMeshBox(panelPos1x, posy, panelHeightPos2, winPanelSize, (winPanelThickness / 2), (winPanelSize * 2), matrefWin)
    genMeshBox(panelPos2x, posy, panelHeightPos2, winPanelSize, (winPanelThickness / 2), (winPanelSize * 2), matrefWin)
    genMeshBox(panelPos3x, posy, panelHeightPos2, winPanelSize, (winPanelThickness / 2), (winPanelSize * 2), matrefWin)

    # Three rows generated
    genMeshBox(posx, posy, posz, 
        ((winPanelSize * 3) + (winPanelBorderSize * 1)), (winPanelBorderSize / 2), winPanelBorderSize, matrefWinPanel)
    genMeshBox(posx, posy, (posz + (winPanelSize * 2)+ winPanelBorderSize), 
        ((winPanelSize * 3) + (winPanelBorderSize * 1)), (winPanelBorderSize / 2), winPanelBorderSize, matrefWinPanel)
    genMeshBox(posx, posy, (posz + (winPanelSize * 4) + (winPanelBorderSize * 2)), 
        ((winPanelSize * 3) + (winPanelBorderSize * 1)), (winPanelBorderSize / 2), winPanelBorderSize, matrefWinPanel)
    # Six pillars generated
    genMeshBox((posx + winPanelSize + (winPanelBorderSize / 2)), posy, (posz + winPanelBorderSize), 
        (winPanelBorderSize / 2), (winPanelBorderSize / 2), (winPanelSize * 2), matrefWinPanel)
    genMeshBox((posx - winPanelSize - (winPanelBorderSize / 2)), posy, (posz + winPanelBorderSize), 
        (winPanelBorderSize / 2), (winPanelBorderSize / 2), (winPanelSize * 2), matrefWinPanel)
    genMeshBox((posx - winPanelSize - (winPanelBorderSize / 2)), posy, 
        (posz + (winPanelSize * 2) + (winPanelBorderSize * 2)), 
            (winPanelBorderSize / 2), (winPanelBorderSize / 2), (winPanelSize * 2), matrefWinPanel)
    genMeshBox((posx + winPanelSize + (winPanelBorderSize / 2)), posy, 
        (posz + (winPanelSize * 2) + (winPanelBorderSize * 2)), 
            (winPanelBorderSize / 2), (winPanelBorderSize / 2), (winPanelSize * 2), matrefWinPanel)
    genMeshBox((posx + (winPanelSize * 3) + (winPanelBorderSize * 1.5)), posy, posz, 
        (winPanelBorderSize / 2), (winPanelBorderSize / 2), ((winPanelSize * 4) + (winPanelBorderSize * 3)), matrefWinPanel)
    genMeshBox((posx - (winPanelSize * 3) - (winPanelBorderSize * 1.5)), posy, posz, 
        (winPanelBorderSize / 2), (winPanelBorderSize / 2), ((winPanelSize * 4) + (winPanelBorderSize * 3)), matrefWinPanel)

def genWinPanelTwelveX(posx, posy, posz):
    winPanelThickness=1
    winPanelBorderSize=2
    winPanelSize=8
    matrefWin = "\nmatref window\n"
    matrefWinPanel = "\nmatref windowPanel\n"
    
    panelPos1x = (posx + winPanelBorderSize + (winPanelSize * 2))
    panelPos2x = posx
    panelPos3x = (posx - winPanelBorderSize - (winPanelSize * 2))
    panelHeightPos1 = (posz + winPanelBorderSize)
    panelHeightPos2 =  (posz + (winPanelBorderSize * 2) + (winPanelSize * 2))
    # Reason the math is confusing is since we are using a box for a base, hence the confusion.
    #Part 1 Windows:
    genMeshBox(panelPos1x, posy, panelHeightPos1, winPanelSize, (winPanelThickness / 2), (winPanelSize * 2), matrefWin)
    genMeshBox(panelPos2x, posy, panelHeightPos1, winPanelSize, (winPanelThickness / 2), (winPanelSize * 2), matrefWin)
    genMeshBox(panelPos3x, posy, panelHeightPos1, winPanelSize, (winPanelThickness / 2), (winPanelSize * 2), matrefWin)
    # Part 2 Windows:
    genMeshBox(panelPos1x, posy, panelHeightPos2, winPanelSize, (winPanelThickness / 2), (winPanelSize * 2), matrefWin)
    genMeshBox(panelPos2x, posy, panelHeightPos2, winPanelSize, (winPanelThickness / 2), (winPanelSize * 2), matrefWin)
    genMeshBox(panelPos3x, posy, panelHeightPos2, winPanelSize, (winPanelThickness / 2), (winPanelSize * 2), matrefWin)

    # Three rows generated
    genMeshBox(posx, posy, posz, 
        ((winPanelSize * 3) + (winPanelBorderSize * 1)), (winPanelBorderSize / 2), winPanelBorderSize, matrefWinPanel)
    genMeshBox(posx, posy, (posz + (winPanelSize * 2)+ winPanelBorderSize), 
        ((winPanelSize * 3) + (winPanelBorderSize * 1)), (winPanelBorderSize / 2), winPanelBorderSize, matrefWinPanel)
    genMeshBox(posx, posy, (posz + (winPanelSize * 4) + (winPanelBorderSize * 2)), 
        ((winPanelSize * 3) + (winPanelBorderSize * 1)), (winPanelBorderSize / 2), winPanelBorderSize, matrefWinPanel)
    # Six pillars generated
    genMeshBox((posx + winPanelSize + (winPanelBorderSize / 2)), posy, (posz + winPanelBorderSize), 
        (winPanelBorderSize / 2), (winPanelBorderSize / 2), (winPanelSize * 2), matrefWinPanel)
    genMeshBox((posx - winPanelSize - (winPanelBorderSize / 2)), posy, (posz + winPanelBorderSize), 
        (winPanelBorderSize / 2), (winPanelBorderSize / 2), (winPanelSize * 2), matrefWinPanel)
    genMeshBox((posx - winPanelSize - (winPanelBorderSize / 2)), posy, 
        (posz + (winPanelSize * 2) + (winPanelBorderSize * 2)), 
            (winPanelBorderSize / 2), (winPanelBorderSize / 2), (winPanelSize * 2), matrefWinPanel)
    genMeshBox((posx + winPanelSize + (winPanelBorderSize / 2)), posy, 
        (posz + (winPanelSize * 2) + (winPanelBorderSize * 2)), 
            (winPanelBorderSize / 2), (winPanelBorderSize / 2), (winPanelSize * 2), matrefWinPanel)
    genMeshBox((posx + (winPanelSize * 3) + (winPanelBorderSize * 1.5)), posy, posz, 
        (winPanelBorderSize / 2), (winPanelBorderSize / 2), ((winPanelSize * 4) + (winPanelBorderSize * 3)), matrefWinPanel)
    genMeshBox((posx - (winPanelSize * 3) - (winPanelBorderSize * 1.5)), posy, posz, 
        (winPanelBorderSize / 2), (winPanelBorderSize / 2), ((winPanelSize * 4) + (winPanelBorderSize * 3)), matrefWinPanel)

# @TODO genWindowFrame, since that will help make us really efficient too.


if __name__ == '__main__':
    print("material\nname window\ncolor 0.52 0.80 0.98 0.2\nend")
    print("material\nname windowPanel\ntexture mesh.png\ncolor DarkSlateGray\nend")
    count = 0
    while count >= -512:
        count -= 56
    
    while count <= 512:
        genWinPanelSixX(count, 0, 0)
        genWinPanelSixX(count, 0, 38)
        genWinPanelSixX(count, 0, 76)
        genWinPanelSixX(count, 0, 114)
        count += 56
    #genWinPanelSixX(0, 0, 0)
    #genWinPanelSixX(56, 0, 0)
    
