from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

window = 0
width, height = 500, 500
start = [0, 0]
end =[0, 0]

def DDA():
    if start[0] < end[0]:
        dx = end[0] - start[0]
        dy = end[1] - start[1]
        x = start[0] 
        y = start[1]
    else:
        dx = start[0] - end[0]
        dy = start[1] - end[1]
        x = end[0] 
        y = end[1]

    if abs(dx) > abs(dy):
        steps = abs(dx)
    else:
        steps = abs(dy)
    
    x_inc = dx / steps
    y_inc = dy / steps


    glBegin(GL_POINTS)
    for _ in range(steps):
        glVertex2f(round(x), round(y))
        x += x_inc
        y += y_inc
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
    DDA()                       
      
   
    glutSwapBuffers()                                  


def main():
    glutInit()                                             
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
    glutInitWindowSize(width, height) 
    glutInitWindowPosition(0, 0)
    window = glutCreateWindow("Graphics Lab1 - DDA Line Algorithm")
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
