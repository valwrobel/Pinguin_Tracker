"""module docstring"""

# imports
import cv2
import numpy as np
import sys
import video_process as vp

# constants
# exception classes
# interface functions
# classes
# internal functions & classes

def main():
    cap = cv2.VideoCapture('input/pinguins.avi')
    print "hello world"


if __name__ == '__main__':
    status = main()
    sys.exit(status)
