from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
from math import *  
def init():
    glClearColor(0.0,0.0,0.0,0.0)
    gluOrtho2D(-1.0,1.0,-1.0,1.0)

def plotpoints():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0,0.0,0.0)
    posx, posy = 0.3,0.0    
    #sides = 32    
    radius = 0.2
    glBegin(GL_LINE_LOOP)
    c=0
    s=0
    for i in range(0,360):    
            c= radius * cos(i) + posx    
            s= radius * sin(i) + posy
            glVertex2f(c,s)
            #glVertex2f(-0.1,0.1)

    
    glEnd()
    
    posx, posy = -0.3,0.0   
    #sides = 32    
    radius = 0.1
    glBegin(GL_LINE_LOOP)
    c=0
    s=0
    for i in range(0,360): 
        c= radius * cos(i) + posx    
        s= radius * sin(i) + posy
        glVertex2f(c,s)
            #glVertex2f(-0.1,0.1)
    glEnd()
    glBegin(GL_LINES)
    glVertex2f(0.3,0.2)
    glVertex2f(-0.3,0.1)
    glVertex2f(0.3,-0.2)
    glVertex2f(-0.3,-0.1)
    glEnd()
    glFlush()

   

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
    glutInitWindowSize(500,500)
    glutInitWindowPosition(50,50)
    glutCreateWindow('Plot Points')
    glutDisplayFunc(plotpoints)
    init()
    glutMainLoop()

main()
