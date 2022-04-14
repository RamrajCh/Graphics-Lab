import numpy as np
import math

class Transformtion2D(object):

    def __init__(self, vertexes):
        self.vertexes = np.array(vertexes)
        self.T = None
    
    def translate2d(self, tx, ty):
        self.T = np.array([[1, 0, tx],[0, 1, ty], [0, 0, 1]])
        return self.transform2d()
    
    def scale2d(self, sx, sy):
        self.T = np.array([[sx, 0, 0],[0, sy, 0], [0, 0, 1]])
        return self.transform2d()

    def rotation2d(self, theta):
        theta = theta / 180 * math.pi
        self.T = np.array([[math.cos(theta), -math.sin(theta), 0], [math.sin(theta), math.cos(theta), 0], [0, 0, 1]])
        return self.transform2d()

    def reflection2d(self, axis):
        self.T = np.array([[1 if axis=="X" else -1, 0, 0], [0, -1 if axis=="X" else 1, 0], [0, 0, 1]])
        return self.transform2d()
    
    def shear2d(self, sh, axis):
        self.T = np.array([[1, sh if axis=="X" else 0, 0], [sh if axis=="Y" else 0, 1, 0], [0, 0, 1]])
        return self.transform2d()
    

    def transform2d(self):
        translated_vertexes = []
        for vertex in self.vertexes:
            V = list(vertex)
            V.append(1)
            translated_vertexes.append(list(self.T.dot(V))[:2])
        return translated_vertexes


if __name__ == "__main__":
    T = Transformtion2D([[0, 0], [1, 0], [0, 1], [1, 1]])
    print(T.shear2d(2, 'X'))
   