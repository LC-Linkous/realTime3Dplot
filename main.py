from viewer import Viewer
import matplotlib
import time

def main():
    matplotlib.interactive(True)
    v = Viewer()
    while True:
        v.drawNow()
        time.sleep(.1)


if __name__ == '__main__':
    main()

