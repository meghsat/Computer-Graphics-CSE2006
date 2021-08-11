from OpenGL import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    gluOrtho2D(0.0, 500.0, 0.0, 400.0)

def fourlines():
        glVertex2f(100, 100)
        glVertex2f(100, 200)
        
        glVertex2f(100, 200)
        glVertex2f(400, 200)

        glVertex2f(400, 200)
        glVertex2f(400, 100)

        glVertex2f(400, 100)
        glVertex2f(100, 100)
    
def bresAlgo(x1, y1, x2, y2):

    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    slope = dy/float(dx)
    
    x, y = x1, y1 

    if slope > 1:
        dx, dy = dy, dx
        x, y = y, x
        x1, y1 = y1, x1
        x2, y2 = y2, x2

    p = 2 * dy - dx
    
    glVertex2f(x, y)
    
    
    for k in range(2, dx):
        if p > 0:
            y = y + 1 if y < y2 else y - 1
            p = p + 2*(dy - dx)
        else:
            p = p + 2*dy
 
        x = x + 1 if x < x2 else x - 1

        glVertex2f(x, y)
            

def lineBres():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glBegin(GL_LINES)
    glColor(1.0, 1.0, 1.0)
    fourlines()
    bresAlgo(100, 100, 400, 200)
    bresAlgo(400, 100, 100, 200)
        
    glEnd()
    glutSwapBuffers()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA|GLUT_DOUBLE|GLUT_ALPHA|GLUT_DEPTH)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(150,150)
    glutCreateWindow('Bresenham line drawing')
    init()
    glutDisplayFunc(lineBres)
    glutIdleFunc(lineBres)
    glutMainLoop()

main()
        
        

   
