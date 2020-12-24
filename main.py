from viewer import Viewer
import matplotlib
import time

if __name__ == '__main__':
    matplotlib.interactive(True)
    v = Viewer()
    while True:
        v.drawNow()
        time.sleep(.1)

