# Import the required modules.
import numpy as np # np is an arbitrary variable which is used as an abbreviation instead of typing numpy every time.
import cv2 # Open cv2 module.
 
hog = cv2.HOGDescriptor() # Initialize the Histogram Oriented Gradient descriptor for human detection.
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector()) # Support Vector Machine algorithm is used for supervised detection of human. 

cv2.startWindowThread() # This function will access the video displayed on the respective window.

capture = cv2.VideoCapture(0) # Opens the webcam to start the video stream.

# The output will be written in the file named, "output.avi".
output = cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc(*'MJPG'), 15., (640, 480)) # This function is used to make annontations on a video. 

while(True) : # Infinite loop.
    # Captures the video frame-by-frame.
    ret, frame = capture.read()  

    # Resizing the frame for faster & more accurate detection.
    frame = cv2.resize(frame, (640, 480))
    # Converting the RGB colours to grayscale for faster detection.
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

    # The below two lines will detect people present in the frame, also returns the corresponding values of boxes & weights for the detected humans.
    boxes, weights = hog.detectMultiScale(frame, winStride = (8, 8))

    boxes = np.array([[x, y, x + w, y + h] for (x, y, w, h) in boxes]) # The sliding window parameters are stored in an array.

    for (xA, yA, xB, yB) in boxes :
        cv2.rectangle(frame, (xA, yA), (xB, yB), (0, 255, 0), 2) # This function draws a rectangular box around the detected human.
         
    output.write(frame.astype('uint8')) # Writes the boxes & weights on the output video.
    cv2.imshow('frame', frame) # Displays the output frame.
    
    # The user can close the webcam by pressing the key 'c'.
    if cv2.waitKey(1) & 0xFF == ord('c') :
        break 

# The output video is stored in the PWD of the jupyter notebook.
capture.release()
output.release()
# Closes the output window.
cv2.destroyAllWindows()
cv2.waitKey(1)
