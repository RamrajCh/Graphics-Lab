from xmlrpc.client import MAXINT
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

window = 0                                             # glut window number
width, height = 1000, 1000                              # window size
start = [0, 0]
end =[0, 0]

def BLA():
    x = start[0]
    y = start[1]

    dx = end[0] - start[1]
    dy = end[1] - start[1]

    if not dx == 0:
        m = dy / dx
    else:
        m = MAXINT

    if abs(m) < 1:
        c1 = 2 * dy
        c2 = 2 * (dy - dx)

        p = c1 - dx

        glBegin(GL_LINES)
        for _ in range(abs(dx)):
            glVertex2f(x, y)
            if p < 0:
                p += c1
            else:
                p += c2
                y += 1
            x += 1
        glEnd()
        glFlush()
    
    else:
        c1 = 2 * dx
        c2 = 2 * (dx - dy)

        p = c1 - dy

        glBegin(GL_LINES)
        for _ in range(abs(dy)):
            glVertex2f(x, y)
            if p < 0:
                p += c1
            else:
                p += c2
                x += 1
            y += 1
        glEnd()
        glFlush()

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
    BLA()
      
   
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
    inp = input("Give start and end points in the format x1 y1 x2 y2 separated by space.")
    points = inp.split()
    start = [int(points[0]), int(points[1])]
    end = [int(points[2]), int(points[3])]
    main()