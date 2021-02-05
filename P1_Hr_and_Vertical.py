"""
Write an option based program that draws Horizontal, Vertical and Diagonal Lines based on User Inputs.
Option 1 : Horizontal Line - ask for X-coordinate range and specific Y-coordinate and plot the line.
Option 2 : Vertical Line - ask for specific X-coordinate and Y-coordinate range and plot the line.
Option 3 : Diagonal Line - ask for inputs - for example : the input : 5, 10; should plot the line (5,5) (6,6) (7,7) (8,8) (9,9) (10,10).
"""
from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*
import sys
import math

print("1.Horizontal Line\n2.Vertical Line\n3.Diagonal Line\n")
i=int(input("Choose from above option to draw lines: "))
if i==1:
    x1,x2,y1=input("Input x1,x2,y coordinate space separated: ").split()
    y2=y1
elif i==2:
    x1,y1,y2=input("Input x1,y1,y2 coordinate space separated: ").split()
    x2=x1
elif i==3:
    x1,x2=input("Input x1,x2 coordinate space separated: ").split()
    y1=x1
    y2=x2
else:
    print("invalid input\n\n\n")

def init():
    glClearColor(0.0,0.0,0.0,1.0)
    gluOrtho2D(-100.0,100.0,-100.0,100.0)

def plotlines():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0,0.0,0.0)
    glLineWidth(5.0)
    glBegin(GL_LINES)
    glVertex2f(float(x1), float(y1))
    glVertex2f(float(x2), float(y2))
    glEnd()
    glFlush()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
    glutInitWindowSize(700,700)
    glutCreateWindow("Plot Lines")
    glutDisplayFunc(plotlines)
    init()
    glutMainLoop()

main()