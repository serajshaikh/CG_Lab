"""2D transformations
Write a menu driven program to Implement 2D transformations on an equilateral triangle
A: Translation
B: Rotation 
C: Scaling
D: Reflection"""



from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math

def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    gluOrtho2D(-250.0, 250.0, -250.0, 250.0)


def ROUND(a):
	return int(a+0.5)

def setPixel(x1,y1,x2,y2,x3,y3):
	glPointSize(5.0)
	glBegin(GL_TRIANGLES)
	glVertex2i(x1,y1)
	glVertex2i(x2,y2)
	glVertex2i(x3,y3)
	glEnd()
	glFlush()
#   *************** Translation **************** 
def translation():
    newx = int(input('Enter x unit to be translated: '))
    newy = int(input('Enter y to be translated: '))
    setPixel(x1 + newx,y1 + newy,x2 + newx,y2 + newy,x3 + newx,y3 + newy)

#   *************** Rotation **************** 
def rotation():
    theeta = int(input('Enter the angle in degrees to be rotated w.r.t origin: '))
    theeta = (theeta*math.pi)/180
    newx1 = x1*math.cos(theeta) - y1*math.sin(theeta)
    newy1 = x1*math.sin(theeta) + y1*math.cos(theeta)
    newx2 = x2*math.cos(theeta) - y2*math.sin(theeta)
    newy2 = x2*math.sin(theeta) + y2*math.cos(theeta)
    newx3 = x3*math.cos(theeta) - y3*math.sin(theeta)
    newy3 = x3*math.sin(theeta) + y3*math.cos(theeta)
    setPixel(ROUND(newx1),ROUND(newy1),ROUND(newx2),ROUND(newy2),ROUND(newx3),ROUND(newy3))
#   *************** Scaling **************** 
def scaling():
    newx = int(input('Enter X scaling factor: '))
    newy = int(input('Enter Y scaling factor: '))
    setPixel(x1, y1, x2 * newx, y2 * newy, x3 * newx, y3 * newy)
    glColor3f(0.2,0.0,1.5)
    setPixel(x1,y1,x2,y2,x3,y3)
#   *************** Reflection **************** 
def reflection():
    ref = int(input('Select 1 reflection about x axis: \n 2 reflection about y axis: \n 3.Reflection about origin: \n 4.Reflection about x=y line:  \n 5.Reflection about x=-y line:'))
    
    if ref == 1:
        setPixel(x1,-y1,x2,-y2,x3,-y3)
    elif ref == 2:
        setPixel(-x1,y1,-x2,y2,-x3,y3)
    elif ref ==3:
        setPixel(-x1,-y1,-x2,-y2,-x3,-y3)
    elif ref==4:
        setPixel(y1,x1,y2,x2,y3,x3)
    elif ref ==5:
        setPixel(-y1,-x1,-y2,-x2,-y3,-x3)
    else:
        print('Invalid option')

def display():
    glColor3f(0.2,0.0,1.5)
    setPixel(x1,y1,x2,y2,x3,y3)
    if option == 1:
        glColor3f(1.0,0.0,1.0)
        translation()
    elif option == 2:
        glColor3f(1.0,0.0,1.0)
        rotation()
    elif option == 3:
        glColor3f(1.0,0.0,1.0)
        scaling()
    elif option == 4:
        glColor3f(1.0,0.0,1.0)
        reflection()
    else:
        print('Invalid option')

def main():
    global x1,x2,y1,y2,x3,y3,option
    x1,y1,x2,y2,x3,y3=map(int,input("Enter  x1,y1,x2,y2,x3,y3 space sapareted: ").split())
    option = int(input('Enter 1 for Translation, 2 for Rotation, 3 for Scaling and 4 for Reflection: '))
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(100, 100)
    glutCreateWindow('2D transformations')
    glutDisplayFunc(display)
    init()
    glutMainLoop()

main()