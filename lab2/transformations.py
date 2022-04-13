from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from transformation2d import Transformtion2D

vertexes = [[20, 140], [140, 20], [110, 150]]
window = 0 
width, height = 600, 600

transformation = None
translation = [None, None]
rotation = [None]
scaling = [None, None]
reflection = [None]
shearing = [None, None]

def plot_points(x, y):
    glVertex2f(x + 300, y + 300)

def draw_axes():
    glColor3f(0.0, 0.0, 1.0)
    glBegin(GL_LINES)
    plot_points(0, -300)
    plot_points(0,300)
    plot_points(-300,0)
    plot_points(300,0)
    glEnd()
    draw_triangle()

def draw_triangle():
    glColor3f(0.3, 0.9, 0.3)
    glPointSize(2)
    glBegin(GL_POLYGON)
    for vertex in vertexes:
        plot_points(vertex[0], vertex[1])
    glEnd()
    transform()

def transform():
    glColor3f(0.8, 0.3, 0.5)
    glPointSize(2)
    T = Transformtion2D(vertexes)
    if transformation == "translation":
        transformed_vertexes = T.translate2d(translation[0], translation[1])
    elif transformation == "rotation":
        transformed_vertexes = T.rotation2d(rotation[0])
    elif transformation == "scaling":
        transformed_vertexes = T.scale2d(scaling[0], scaling[1])
    elif transformation == "reflection":
        transformed_vertexes = T.reflection2d(reflection[0])
    elif transformation == "shearing":
        transformed_vertexes = T.shear2d(shearing[0], shearing[1])
    glBegin(GL_POLYGON)
    for vertex in transformed_vertexes:
        plot_points(vertex[0], vertex[1])
    glEnd()

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
    draw_axes()  
    glutSwapBuffers()
   

# initialization
def main():
    glutInit() 
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
    glutInitWindowSize(width, height)
    glutInitWindowPosition(0, 0) 
    window = glutCreateWindow("Graphics Lab1 - 2D transformation") 
    glutDisplayFunc(draw)
    glutIdleFunc(draw)
    glutMainLoop()   

if __name__ == "__main__":
    try:
        transformation = sys.argv[1]
        if transformation == "translation":
            translation = [int(sys.argv[2]), int(sys.argv[3])]
        elif transformation == "rotation":
            rotation = [int(sys.argv[2])]
        elif transformation == "scaling":
            scaling = [int(sys.argv[2]), int(sys.argv[3])]
        elif transformation == "reflection":
            reflection = [sys.argv[2]]
        elif transformation == "shearing":
            shearing = [int(sys.argv[2]), sys.argv[3]]
    except IndexError:
        print("usage: transformations.py <string:transformation type> <string:args required for transformation> ...")
    main()