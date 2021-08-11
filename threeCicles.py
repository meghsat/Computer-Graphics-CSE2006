from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from math import *

def init():
    glClearColor(1.0, 1.0, 1.0, 1.0)
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0)

def shade():
        glBegin(GL_LINE_LOOP)
        glColor3f(0.0,0.0,0.0)
        radius = 0.1 
        c1x = 0.1;
        c1y = 0.1;
        c2x = -0.1;
        c2y = 0.1;
        c3x = 0.0;
        c3y = -0.05;

        for i in range(360):
            theta = 2.0 * pi * float(i) / float(360);
            x = radius * cos(theta);
            y = radius * sin(theta);
            glVertex2f(x + c1x, y + c1y);
            glVertex2f(x + c2x, y + c2y);
            glVertex2f(x + c3x, y + c3y);
        glEnd()
    
    
def circles():
        glClear(GL_COLOR_BUFFER_BIT)
        glBegin(GL_LINE_LOOP)
        glColor3f(0.0,0.0,0.0)
        radius = 0.4 
        c1x = 0.2;
        c1y = 0.2;
        c2x = -0.2;
        c2y = 0.2;
        c3x = 0.0;
        c3y = -0.2;

        for i in range(360):
            theta = 2.0 * pi * float(i) / float(360);
            x = radius * cos(theta);
            y = radius * sin(theta);
            glVertex2f(x + c1x, y + c1y);
        glEnd()
        
        glBegin(GL_LINE_LOOP)
        for i in range(360):
            theta = 2.0 * pi * float(i) / float(360);
            x = radius * cos(theta);
            y = radius * sin(theta);
            glVertex2f(x + c2x, y + c2y);
        glEnd()
        
        glBegin(GL_LINE_LOOP)
        for i in range(360):
            theta = 2.0 * pi * float(i) / float(360);
            x = radius * cos(theta);
            y = radius * sin(theta);
            glVertex2f(x + c3x, y + c3y);
        glEnd()

        shade()
        glFlush()

def main():
        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
        glutInitWindowSize(500,500)
        glutInitWindowPosition(50,50)
        glutCreateWindow("3 Circles")
        glutDisplayFunc(circles)
        init()
        glutMainLoop()
        
main()
