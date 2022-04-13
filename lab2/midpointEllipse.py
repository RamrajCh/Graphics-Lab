from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

window = 0 
width, height = 1000, 1000
rx, ry = 0, 0
center = [0, 0]

def midpoint_ellipse():
    glBegin(GL_POINTS)
    
    x = 0
    y = ry


    dx = 2 * ry**2 * x
    dy = 2 * rx**2 * y

    p1 = round(ry**2 + ((1/4)*rx**2) - (rx**2 * ry))
    plot_ellipse_points(x, y)
    while (dx < dy):
        if (p1 < 0):
            x += 1
            dx = 2 * ry**2 * x
            p1 += 2 * ry**2 * x + ry**2
        
        else:
            x += 1
            y -= 1
            dx = 2 * ry**2 * x
            dy = 2 * rx**2 * y
            p1 += (2 * ry**2 * x) - (2 * rx**2 * y) + ry**2
        plot_ellipse_points(x, y)
    
    p2 = round((ry**2 * (x + 0.5)**2) + (rx**2 * (y - 1)**2) - (rx**2 * ry**2))
    plot_ellipse_points(x, y)
    while(y > 0):
        if p2 > 0:
            y -= 1
            dy = 2 * rx**2 * y
            p2 += rx**2 - (2 * rx**2 * y)
        
        else:
            y -= 1
            x += 1
            dx = 2 * ry**2 * x
            dy = 2 * rx**2 * y
            p2 += (2 * ry**2 * x) - (2 * rx**2 * y) + rx**2
        plot_ellipse_points(x, y)
    glEnd()


def plot_ellipse_points(x, y):
    four_symmetry_points = [[x,y], [-x,y], [x,-y], [-x,-y]]
    for point in four_symmetry_points:
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
    midpoint_ellipse()    
    glutSwapBuffers()
   

# initialization
def main():
    glutInit() 
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
    glutInitWindowSize(width, height)
    glutInitWindowPosition(0, 0) 
    window = glutCreateWindow("Graphics Lab2 - midpoint ellipse Algorithm") 
    glutDisplayFunc(draw)
    glutIdleFunc(draw)
    glutMainLoop()   

if __name__ == "__main__":
    print("Give the values of rx, ry and center point (xc, yc)")
    rx = int(input("rx = "))
    ry = int(input("ry = "))
    xc = int(input ("xc = "))
    yc = int(input("yc = "))
    center = [xc, yc]
    main()