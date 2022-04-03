from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

window = 0 
width, height = 500, 500
start = [0, 0]
end =[0, 0]

def BLA():
    if start[0] < end[0]:
        x = start[0]
        y = start[1]
        dx = end[0] - start[0]
        dy = end[1] - start[1]

    else:
        x = end[0]
        y = end[1]
        dx = start[0] - end[0]
        dy = start[1] - end[1]

    if abs(dy) < abs(dx):   # Slope less than 1
        c1 = 2 * dy
        c2 = 2 * (dy - dx)

        p = c1 - dx

        glBegin(GL_POINTS)
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
    
    else:   # Slope equal or greater than 1
        c1 = 2 * abs(dx)
        c2 = 2 * (abs(dx) - abs(dy))

        p = c1 - dy

        glBegin(GL_POINTS)
        glVertex2f(x, y)
        for _ in range(abs(dy)):
            if p < 0:
                p += c1
            else:
                p += c2
                x += 1
            y += 1
            glVertex2f(x, y)
        glEnd()
        glFlush()

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
    BLA()    
    glutSwapBuffers()
   

# initialization
def main():
    glutInit() 
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
    glutInitWindowSize(width, height)
    glutInitWindowPosition(0, 0) 
    window = glutCreateWindow("Graphics Lab1 - BLA Line Algorithm") 
    glutDisplayFunc(draw)
    glutIdleFunc(draw)
    glutMainLoop()   

if __name__ == "__main__":
    print("Give the values of endpoints (x1, y1) and (x2, y2)")
    x1 = input("x1 = ")
    y1 = input("y1 = ")
    x2 = input ("x2 = ")
    y2 = input("y2 = ")
    start = [int(x1), int(y1)]
    end = [int(x2), int(y2)]
    main()