import numpy as np
import matplotlib.pyplot as plt

class Viewer:
    def __init__(self):
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111, projection='3d' )
        self.ax.set_zlim3d(-10, 10)
        self.x = []
        self.y = []
        self.z = []

    def drawNow(self):
        self.x.append(np.random.randint(-10,10))
        self.y.append(np.random.randint(-10,10))
        self.z.append(np.random.randint(-10,10))
        print('x = ' + str(self.x) + '\t y =' + str(self.y) + '\t z =' + str(self.z))
        self.ax.plot(self.x, self.y, self.z, 'b')
        plt.draw()
        self.fig.canvas.flush_events()
