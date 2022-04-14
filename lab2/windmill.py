from itertools import count
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from transformation2d import Transformtion2D

window = 0 
width, height = 600, 600

theta = 0
speed = 0

base = [[300, 450], [210, 50], [390, 50]]

fin1 = [[300, 450], [275, 600], [325, 600]]



def draw_polygon(vertexes):
    glBegin(GL_TRIANGLES)
    for v in vertexes:
        glVertex2f(v[0], v[1])
    glEnd()

def draw_windmill():
    global fin1
    glColor3f(0.3, 0.9, 0.3)
    glPointSize(2)
    draw_polygon(base)
    glColor3f(0.7, 0.2, 0.8)
    draw_polygon(fin1)
    fin2 = rotate(fin1, 120)
    fin3 = rotate(fin2, 120)
    draw_polygon(fin2)
    draw_polygon(fin3)

def signals(key, x, y):
    global speed, theta
    if key == b's':
        speed = 1 if speed == 0 else 0
    if key == b'd':
        speed += 1
    if key == b'a':
        speed -= 1
    theta = speed
    glutPostRedisplay()

def rotate_fins():
    global theta, fin1
    fin1 = rotate(fin1, theta)
    glutPostRedisplay()

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
    draw_windmill()
    glutSwapBuffers()
   

# initialization
def main():
    glutInit() 
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
    glutInitWindowSize(width, height)
    glutInitWindowPosition(0, 0) 
    window = glutCreateWindow("Graphics Lab1 - Windmill") 
    glutDisplayFunc(draw)
    glutIdleFunc(rotate_fins)
    glutKeyboardFunc(signals)
    glutMainLoop()   

if __name__ == "__main__":
    print("Commands:\n 's': start/stop windmill \n 'a': rotate fins clockwise, press repetedly to increase speed \n 'd': rotate fins anti-clockwise ")
    main()