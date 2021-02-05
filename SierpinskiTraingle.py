"""
Generation of fractal image
Write a program to generate a Sierpinski traingle
"""


from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math

def init():
	glClearColor(0.0,0.0,0.0,0.0)		
	gluOrtho2D(-100.0,100.0,-100.0,100.0)
def glutFunc():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500,500)
    glutInitWindowPosition(70,70)  
    glutCreateWindow("Sierpinski Triangle")
    init()

def setAxes():  
    glColor3f(0.0,1.0,0.0) 
    glPointSize(5.0)
    glBegin(GL_LINES)
    glVertex2f(-100,0)
    glVertex2f(100,0)
    glEnd()
    glBegin(GL_LINES)
    glVertex2f(0,-100)
    glVertex2f(0,100)
    glEnd()
    glLineWidth(1.0)

def triangle(a,b,c):
    glVertex2fv(a)
    glVertex2fv(b)
    glVertex2fv(c)

def divide_triangle(a,b,c,m):
    v0=[]
    v1=[]
    v2=[]
    if(m>0):
        for j in range (0,2): 
            v0.append((a[j]+b[j])/2)
        for j in range(0,2):
            v1.append((a[j]+c[j])/2)
        for j in range(0,2): 
            v2.append((b[j]+c[j])/2)
        divide_triangle(a, v0, v1, m-1)
        divide_triangle(c, v1, v2, m-1)
        divide_triangle(b, v2, v0, m-1)
    else:
        triangle(a,b,c)

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1,0,0)
    setAxes()
    glColor3f(1,0,0)
    glBegin(GL_TRIANGLES)
    divide_triangle(coordinate[0], coordinate[1], coordinate[2], 6)
    glEnd()
    glFlush()
    
def main():
    global coordinate
    coordinate=[]
    print("**GENERATION OF FRACTAL IMAGE**")
    print("    **Sierpinski Triangle**    ")
    print("Enter Coordinates of Triangle: ")
    for i in range(0,3):
        x,y=map(int, input(f"Enter x{i+1} and y{i+1} coordinate : ").split(","))
        coordinate.append([x,y])   
    glutFunc()
    glutDisplayFunc(display)   
    glutMainLoop()

main()

# 888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
# # *****************************************************
# from OpenGL.GL import *
# from OpenGL.GLU import *
# from OpenGL.GLUT import *
# import sys
# from math import *

# X,Y=map(int,input().split())
# def init():
# 	glClearColor(0.0, 0.0, 0.0, 0.0)
# 	gluOrtho2D(-100.0, 100.0, -100.0, 100.0)

# def glutFunct():
# 	glutInit(sys.argv)
# 	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
# 	glutInitWindowSize(500, 500)
# 	glutInitWindowPosition(0, 0)
# 	glutCreateWindow("SierpinskiTriangle")
# 	init()

# def setPixel(x1,y1,x2,y2):
# 	glPointSize(5.0)
# 	glBegin(GL_LINE)
# 	glVertex2f(x1,y1)
# 	glVertex2f(x2,y2)
# 	# glVertex2f(x3,y3)
# 	glEnd()
# 	glFlush()

# def triangle(x, y, h, colorVal):
#     glColor3f(colorVal % 15 + 1,0.0,0.0)
#     for delta in range(0,-5,-1):
#         setPixel(x - (h + delta) / sqrt(3), y - (h + delta) / 3, x + (h + delta) / sqrt(3), y - (h + delta) / 3)
#         setPixel(x - (h + delta) / sqrt(3), y - (h + delta) / 3, x, y + 2 * (h + delta) / 3)
#         setPixel(x, y + 2 * (h + delta) / 3, x + (h + delta) / sqrt(3), y - (h + delta) / 3)


# def trianglev2(x, y, h, colorVal):
#         glColor3f(colorVal % 15 + 1,0.0,0.0)
#         for delta in range(0,-5,-1): 
#             setPixel(x - (h + delta) / sqrt(3), y + (h + delta) / 3, x + (h + delta) / sqrt(3), y + (h + delta) / 3) 
#             setPixel(x - (h + delta) / sqrt(3), y + (h + delta) / 3, x, y - 2 * (h + delta) / 3) 
#             setPixel(x, y - 2 * (h + delta) / 3, x + (h + delta) / sqrt(3), y + (h + delta) / 3) 

# def drawTriangles( x = X / 2, y = 2 * Y / 3, h = Y / 2, colorVal = 0):
#     if h < 5:
#         return 0
  
#     if x > 0 and y > 0 and x < X and y < Y :
#         triangle(x, y, h, colorVal)
  
#     drawTriangles(x, y - 2 * h / 3, h / 2, colorVal + 1); 
#     drawTriangles(x - h / sqrt(3), y + h / 3, h / 2, colorVal + 1) 
#     drawTriangles(x + h / sqrt(3), y + h / 3, h / 2, colorVal + 1) 
#     return 0

# def input():
#     trianglev2(X / 2, 2 * Y / 3, Y, 2)
#     drawTriangles()

# def main():
#     glutFunct()
#     glutDisplayFunc(input)
#     glutMainLoop()
# main()
# **********************************************************************
# from OpenGL.GL import *
# from OpenGL.GLU import *
# from OpenGL.GLUT import *
# import sys
# import math

# X,Y=map(int,input("enter X and Y space separated").split())

# def init():
# 	glClearColor(0.0, 0.0, 0.0, 0.0)
# 	gluOrtho2D(-20.0, 20.0, -20.0, 20.0)

# def glutFunct():
# 	glutInit(sys.argv)
# 	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
# 	glutInitWindowSize(500, 500)
# 	glutInitWindowPosition(0, 0)
# 	glutCreateWindow("Sierpinski Triangle")
# 	init()
     
# def triangle(x,y,h,colorVal):
#     #glColor3f(colorVal) 
#     for delta in range(0,-5,-1):
#         setPixel(
#         x - (h + delta) / math.sqrt(3), y - (h + delta) / 3,
#         x + (h + delta) / math.sqrt(3), y - (h + delta) / 3,
#         x,y + 2 * (h + delta) / 3)

# def setPixel(x1,y1,x2,y2,x3,y3):
#     glPointSize(5.0)
#     glBegin(GL_LINES)
#     glVertex2f(x1,y1)
#     glVertex2f(x2,y2)
#     glVertex2f(x2,y2)
#     glVertex2f(x3,y3)
#     glVertex2f(x3,y3)
#     glVertex2f(x1,y1)
#     glEnd()
#     glFlush()

# def trianglev2(x,y,h,colorVal):
#     #glColor3f(colorVal)
#     for delta in range(0,-6,-1):
#         setPixel(x - (h + delta) / math.sqrt(3),y + (h + delta) / 3, 
#              x + (h + delta) / math.sqrt(3),y + (h + delta) / 3,
#              x,y - 2 * (h + delta) / 3)
#     drawTriangles()
         
# def drawTriangles(x = X / 2,y = 2 * Y / 3,h = Y / 2,colorVal = [1,0,0]): 
#     if (h < 5):
#         return 0
#     if x > 0 and y > 0 and x < X and y < Y:
#         triangle(x, y, h, colorVal)
#     drawTriangles(x,y - 2 * h / 3, h / 2, colorVal)
#     drawTriangles(x - h / math.sqrt(3), y + h / 3, h / 2, colorVal=[0,1,0]) 
#     drawTriangles(x + h / math.sqrt(3), y + h / 3, h / 2, colorVal=[0,0,1])
#     return 0

# #int main() 
# #{ 
# #    initwindow(X, Y); 
# #    trianglev2(X / 2, 2 * Y / 3, Y, 2); 
# #  
# #    drawTriangles(); 
# #    getch(); 
# #    closegraph(); 
# #  
# #    return 0; 
# #} 
# def main():
#     glutFunct()
#     glutDisplayFunc(lambda:trianglev2(X / 2, 2 * Y / 3, Y, 2))
#     init()
#     glutMainLoop()

# main()
# 88888888888888888888888888888888888888888888888888888888888888888888888888888888888888