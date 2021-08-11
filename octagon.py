from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import sys

def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    gluOrtho2D(1.0, -1.0, 1.0, -1.0)
def plotpoints():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 0.0, 0.0)
    glBegin(GL_LINES)
    glVertex2f(0.0, 0.1)
    glVertex2f(0.1, 0.0)
    glVertex2f(0.1, 0.0)
    glVertex2f(0.2, 0.0)
    glVertex2f(0.2, 0.0)
    glVertex2f(0.3, 0.1)
    glVertex2f(0.0, 0.2)
    glVertex2f(0.1, 0.3)
    glVertex2f(0.2, 0.3)
    glVertex2f(0.3, 0.2)
    glVertex2f(0.3, 0.2)
    glVertex2f(0.3, 0.1)
    glVertex2f(0.2, 0.3)
    glVertex2f(0.1, 0.3)
    glVertex2f(0.0, 0.2)
    glVertex2f(0.0, 0.1)
    glEnd()
    

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
    glutInitWindowSize(500,500)
    glutInitWindowPosition(50,50)
    glutCreateWindow("Plot Points")
    glutDisplayFunc(plotpoints)
    init()
    glutMainLoop()
main()
