import cv2
import os

# Read the video from specified path
vid = cv2.VideoCapture('Camera3.mp4')

try:
    # creating a folder named data
    if not os.path.exists('data'):
        os.makedirs('data')

# if not created then raise error
except OSError:
    print('Error: Creating directory of data')

# frame
currentframe = -1

while (True):

    # reading from frame
    success, frame = vid.read()
    currentframe += 1
    if success:
        if currentframe % 15 == 0:
            # continue creating images until video remains
            name = './data/frame' + str(currentframe) + '.jpg'
            print('Creating...' + name)
            frame = frame[210:445,115:350]
            frame = cv2.resize(frame,(116,116))
            # writing the extracted images
            cv2.imwrite(name, frame)


        # show how many frames are created

    else:
        break



# Release all space and windows once done
vid.release()
cv2.destroyAllWindows()