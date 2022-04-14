from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys


from transformation2d import Transformtion2D

window = 0 
width, height = 600, 600

theta = 10

base = [[300, 450], [210, 50], [390, 50]]
fin1 = [[300, 450], [450, 450], [375, 535]]
fin2 = [[300, 450], [300, 600], [225, 525]]
fin3 = [[300, 450], [150, 450], [225, 375]]
fin4 = [[300, 450], [300, 300], [375, 375]]


def draw_polygon(vertexes):
    glBegin(GL_POLYGON)
    for v in vertexes:
        glVertex2f(v[0], v[1])
    glEnd()

def draw_windmill():
    glColor3f(0.3, 0.9, 0.3)
    glPointSize(2)
    draw_polygon(base)
    glColor3f(0.7, 0.2, 0.8)
    draw_polygon(fin1)
    draw_polygon(fin2)
    draw_polygon(fin3)
    draw_polygon(fin4)

def signals(key, x, y):
    global theta, fin1, fin2, fin3, fin4
    if key == b's':
        fin1 = rotate(fin1, theta)
        fin2 = rotate(fin2, theta)
        fin3 = rotate(fin3, theta)
        fin4 = rotate(fin4, theta)
    rotate_fins()
    glutPostRedisplay()

def rotate_fins():
    draw_polygon(fin1)
    draw_polygon(fin2)
    draw_polygon(fin3)
    draw_polygon(fin4)

def rotate(vertexes, theta=90):
    t_vertexes = []
    for vertex in vertexes:
        V = list(vertex)
        t_vertexes.append([V[0]-300, V[1]-450])
    T = Transformtion2D(t_vertexes)
    rotated_vertexes = T.rotation2d(theta)
    t_vertexes = []
    for vertex in rotated_vertexes:
        V = list(vertex)
        t_vertexes.append([V[0]+300, V[1]+450])
    return t_vertexes


def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    draw_windmill()
    glutSwapBuffers()

def init():
    glClearColor(0.3,0.3,0.3,0)
    gluOrtho2D(0.0, width, 0.0, height)    

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(width, height)
    window = glutCreateWindow("Raycaster in python")
    init()
    glutDisplayFunc(display)
    glutKeyboardFunc(signals)
    glutMainLoop()

if __name__ == "__main__":
    main()