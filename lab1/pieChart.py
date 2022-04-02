import math

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from midpointCircle import midpoint_circle

window = 0  
width, height = 500, 500
center = [250,250]
radius = 125

section = []

def pie_chart():
    slice_angle = 0
    previous_slice_angle = 0
    total = sum(section)
    for sec in section:
        slice_angle = ( 2 * math.pi * sec/total ) + previous_slice_angle
        x = center[0] + radius * math.cos(slice_angle)
        y = center[1] + radius * math.sin(slice_angle)
        glColor3f(1.0, 0.0, 1.0)
        glBegin(GL_LINES)
        glVertex2f(center[0], center[1])
        glVertex2f(x, y)
        glEnd()
        previous_slice_angle = slice_angle

def refresh2d(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, width, 0.0, height, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def draw():                                           
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity() 
    refresh2d(width, height)  
    glColor3f(0.0, 0.0, 1.0) 
    midpoint_circle(center, radius)
    pie_chart()
    glutSwapBuffers()
   

# initialization
def main():
    glutInit() 
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
    glutInitWindowSize(width, height)
    glutInitWindowPosition(0, 0) 
    window = glutCreateWindow("Graphics Lab1 - Piechart")
    glutDisplayFunc(draw)
    glutIdleFunc(draw)
    glutMainLoop()   

if __name__ == "__main__":
    inp = input("Give the data values for each section of pie chart. ")
    section = [int(i) for i in inp.split()]
    main()