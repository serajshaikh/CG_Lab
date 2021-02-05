
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from numpy import *
import sys
def init():
    glClearColor(1.0, 1.0, 1.0, 1.0)
    gluOrtho2D(-5.0, 5.0, -5.0, 5.0)
def plotfunc():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0, 0.0, 0.0)
    glBegin(GL_LINES)
    glVertex2f(-5.0, 0.0)
    glVertex2f(5.0, 0.0)
    glVertex2f(0.0, 5.0)
    glVertex2f(0.0, -5.0)
    glEnd()
    glPointSize(3.0)
    for x in arange(-5.0, 5.0, 0.1):
        y = x*x
        glColor3f(.05, .0, 0.0)
        glPointSize(10)
        glBegin(GL_POINTS)
        glVertex2f(x, y)
        glEnd()
        glFlush()
def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
    glutInitWindowPosition(250,250)
    glutInitWindowSize(400,400)
    glutCreateWindow("Function Plotter")
    glutDisplayFunc(plotfunc)

    init()
    glutMainLoop()
main()
# End of program 
# # First Python OpenGL program
# # ogl1.py
# from OpenGL.GLUT import *
# from OpenGL.GL import *
# from OpenGL.GLU import *
# def draw():
#     glClear(GL_COLOR_BUFFER_BIT)
#     glutWireTeapot(0.5)
#     glFlush()
# glutInit(sys.argv)
# glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
# glutInitWindowSize(250, 250)
# glutInitWindowPosition(100, 100)
# glutCreateWindow("My Second OGL Program")
# glutDisplayFunc(draw)
# glutMainLoop()
# # End of program 
# # # ****************************************************
# from OpenGL.GL import *
# from OpenGL.GLU import *
# from OpenGL.GLUT import *
# import sys
# def init():
#     glClearColor(0.0, 0.0, 0.0, 1.0)
#     gluOrtho2D(-010.0, 10.0, -10.0, 10.0)
# def plotpoints():
#     glClear(GL_COLOR_BUFFER_BIT)
#     glColor3f(1.0, 0.0, 0.0)
#     glPointSize(5)
#     glBegin(GL_TRIANGLES)
#     glVertex2f(-5.0, 0.0)
#     glVertex2f(5.0, 0.0)
#     glVertex2f(5.0, 5.0)


#     # glVertex2f() 
#     glEnd()

#     glFlush()
# def main():
#     glutInit(sys.argv)
#     glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
#     glutInitWindowSize(500,500)
#     glutInitWindowPosition(50,50)
#     glutCreateWindow("Plote points")
#     glutDisplayFunc(plotpoints)

#     init()
#     glutMainLoop()
# main()
# # End of Program
# # *******
# PyFunc.py
# Plotting functions