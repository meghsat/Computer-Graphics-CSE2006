from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from math import *

def init():
    glClearColor(1.0, 1.0, 1.0, 1.0)
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0)

def body():
        glBegin(GL_LINES)
        glColor3f(0.0,0.0,1.0)
        glVertex2f(0.0, -0.2)
        glVertex2f(0.0, -0.6)

        glVertex2f(0.0, -0.6)
        glVertex2f(-0.2, -0.8)

        glVertex2f(0.0, -0.6)
        glVertex2f(0.2, -0.8)

        glVertex2f(-0.2, -0.4)
        glVertex2f(0.2, -0.4)
        glEnd()

def head():
        glClear(GL_COLOR_BUFFER_BIT)
        glBegin(GL_LINES)
        glColor3f(0.0,0.0,0.0)
        glVertex2f(0.1, 0.2)
        glVertex2f(0.2, 0.1)
        
        glVertex2f(-0.1, 0.2)
        glVertex2f(-0.2, 0.1)

        glVertex2f(-0.1, -0.2)
        glVertex2f(-0.2, -0.1)

        glVertex2f(0.1, -0.2)
        glVertex2f(0.2, -0.1)

       
        glVertex2f(0.2, 0.1)
        glVertex2f(0.2, -0.1)

        glVertex2f(0.1, 0.2)
        glVertex2f(-0.1, 0.2)

        glVertex2f(-0.2, -0.1)
        glVertex2f(-0.2, 0.1)

        glVertex2f(-0.1, -0.2)
        glVertex2f(0.1, -0.2)
        
        glEnd()

        body()
        
        glFlush()

def main():
        glutInit(sys.argv)#
        glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)#
        glutInitWindowSize(500,500)
        glutInitWindowPosition(50,50)
        glutCreateWindow("Stick Man")
        glutDisplayFunc(head)
        init()
        glutMainLoop()
        
main()
