from xmlrpc.client import MAXINT
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

window = 0                                             # glut window number
width, height = 1000, 1000                               # window size
center = [0,0]
radius = 0

def midpoint_circle():
    x = 0
    y = radius

    p = 1 - radius

    glBegin(GL_POLYGON)
    plot_circle_points(x,y)
    while(x < y):
        if p < 0:
            p += 2 * x + 1
        else:
            p += 2 * (x - y) + 1
            y -= 1
        x += 1
        plot_circle_points(x,y)
    glEnd()
    glFlush()

def plot_circle_points(x, y):
    eight_symmetry_points = [[x,y], [-x,y], [x,-y], [-x,-y], [y,x], [y,-x], [-y,x], [-y,-x]]
    for point in eight_symmetry_points:
        glVertex(point[0]+center[0], point[1]+center[1])
    

def refresh2d(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, width, 0.0, height, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def draw():                                            # ondraw is called all the time
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # clear the screen
    glLoadIdentity()                                   # reset position
                                     # reset position
    refresh2d(width, height)                           # set mode to 2d
       
    glColor3f(0.0, 0.0, 1.0)                           # set color to blue
    midpoint_circle()
   
    glutSwapBuffers()                                  # important for double buffering
   

# initialization
def main():
    glutInit()                                             # initialize glut
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
    glutInitWindowSize(width, height)                      # set window size
    glutInitWindowPosition(0, 0)                           # set window position
    window = glutCreateWindow("Graphics Lab1 - DDA Line Algorithm")              # create window with title
    glutDisplayFunc(draw)                                  # set draw function callback
    glutIdleFunc(draw)                                     # draw all the time
    glutMainLoop()   

if __name__ == "__main__":
    inp = input("Give center and radius in the format xc yc radius separated by space.")
    points = inp.split()
    center = [int(points[0]), int(points[1])]
    radius = int(points[2])
    main()