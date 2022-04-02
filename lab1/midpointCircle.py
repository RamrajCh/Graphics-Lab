from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

window = 0  
width, height = 600,600
center = [0,0]
radius = 0

def midpoint_circle(center, radius):
    x = 0
    y = radius

    p = 1 - radius

    glBegin(GL_POINTS)
    while(x < y):
        plot_circle_points(x, y, center)
        x += 1
        if p < 0:
            p += 2 * x + 1
        else:
            y -= 1
            p += 2 * (x - y) + 1
    glEnd()
    glFlush()

def plot_circle_points(x, y, center):
    eight_symmetry_points = [[x,y], [-x,y], [x,-y], [-x,-y], 
                        [y,x], [y,-x], [-y,x], [-y,-x]]
    for point in eight_symmetry_points:
        glVertex(point[0]+center[0], point[1]+center[1])
    

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
    glutSwapBuffers()
   

# initialization
def main():
    glutInit() 
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
    glutInitWindowSize(width, height)
    glutInitWindowPosition(0, 0) 
    window = glutCreateWindow("Graphics Lab1 - Midpoint Circle Algorithm")
    glutDisplayFunc(draw)
    glutIdleFunc(draw)
    glutMainLoop()   

if __name__ == "__main__":
    print("Give the values of center point (xc, yc) and radius")
    xc = input("xc = ")
    yc = input("yc = ")
    radius = int(input ("radius = "))
    center = [int(xc), int(yc)]
    main()