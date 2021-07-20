import os
import cv2
import numpy as np # np is an arbitrary variable which is used as an abbreviation instead of typing numpy every time.

def detect(filepath, file) :
    font = cv2.FONT_HERSHEY_SIMPLEX # The appropriate font is chosen.
    img = cv2.imread(filepath + file) # This command loads the images from a specific folder.
    cimg = img # cimg is a variable which stores the datasets.
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) # This command converts the image in RGB to HSV.
    # hsv is a variable which stores the HSV value.
    
    lower_red1 = np.array([0, 100, 100])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([160, 100, 100])
    upper_red2 = np.array([180, 255, 255])
    # The above four arrays determines the red colour intensity ranges. 
    lower_green = np.array([40, 50, 50])
    upper_green = np.array([90, 255, 255])
    lower_yellow = np.array([15, 150, 150])
    upper_yellow = np.array([35, 255, 255])
    # The above eight lines of code defines the array values for the colour ranges in HSV.   
    
    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
    maskg = cv2.inRange(hsv, lower_green, upper_green)
    masky = cv2.inRange(hsv, lower_yellow, upper_yellow)
    maskr = cv2.add(mask1, mask2)
    # The above five lines of code sets the threshold values.
    size = img.shape # This command determines the dimensions of the image. 
    
    r_circles = cv2.HoughCircles(maskr, cv2.HOUGH_GRADIENT, 1, 80, param1 = 50, param2 = 10, minRadius = 0, maxRadius = 30)
    g_circles = cv2.HoughCircles(maskg, cv2.HOUGH_GRADIENT, 1, 60, param1 = 50, param2 = 10, minRadius = 0, maxRadius = 30)
    y_circles = cv2.HoughCircles(masky, cv2.HOUGH_GRADIENT, 1, 30, param1 = 50, param2 = 5, minRadius = 0, maxRadius = 30)
    # Hough circle command is used to draw circles around the detected colour.    
    
    r = 5 # r is the optimum value of radius for the Hough circle.
    bound = 0.4 # bound is the multiplying constant to define the boundaries of the image.
    # Constant values for defining the image boundary.
    if r_circles is not None :
        r_circles = np.uint16(np.around(r_circles)) # This command returns a 16-bit integer number. 
        for i in r_circles[0, :] : # Edge detection.
            if i[0] > size[1] or i[1] > size[0] or i[1] > size[0]*bound :
                continue
            # It skips if the iteration goes outside the bounds of the image.
            h, s = 0.0, 0.0  # Loss function variables.
            for m in range(-r, r) : # Edge detection.
                for n in range(-r, r) :
                    if (i[1] + m) >= size[0] or (i[0] + n) >= size[1] :
                        continue
                    h += maskr[i[1] + m, i[0] + n] # Central co-ordinates of the circle.
                    s += 1 # The number of times (count) the itertion has gone outside the bounds of the image.
            if h/s > 50 : # Condition for reducing the loss (epoch value).
                cv2.circle(cimg, (i[0], i[1]), i[2] + 10, (0, 255, 0), 2)
                cv2.circle(maskr, (i[0], i[1]), i[2] + 30, (255, 255, 255), 2)
                # Prints the circle around the detected colour.
                cv2.putText(cimg, 'RED STOP', (i[0], i[1]), font, 1, (255, 0, 0), 2, cv2.LINE_AA) # The values in the tuple are in the order - BGR. 
                # Prints the text on the output image.
    
    # Detection of green light.            
    if g_circles is not None :
        g_circles = np.uint16(np.around(g_circles))  # This command returns a 16-bit integer number. 
        for i in g_circles[0, :] : # Edge detection.
            if i[0] > size[1] or i[1] > size[0] or i[1] > size[0]*bound :
                continue
            # It skips if the iteration goes outside the bounds of the image.    
            h, s = 0.0, 0.0 # Loss function variables.
            for m in range(-r, r) :  # Edge detection.
                for n in range(-r, r) :
                    if (i[1] + m) >= size[0] or (i[0] + n) >= size[1] :
                        continue
                    h += maskg[i[1] + m, i[0] + n] # Central co-ordinates of the circle.
                    s += 1  # The number of times (count) the itertion has gone outside the bounds of the image.
            if h/s > 100 : # Condition for reducing the loss (epoch value).
                cv2.circle(cimg, (i[0], i[1]), i[2] + 10, (0, 255, 0), 2)
                cv2.circle(maskg, (i[0], i[1]), i[2] + 30, (255, 255, 255), 2)
                # Prints the circle around the detected colour.
                cv2.putText(cimg, 'GREEN GO',(i[0], i[1]), font, 1, (255, 0, 0), 2, cv2.LINE_AA) # The values in the tuple are in the order - BGR.
                 # Prints the text on the output image.
    
    # Detection of amber light.             
    if y_circles is not None :
        y_circles = np.uint16(np.around(y_circles)) # This command returns a 16-bit integer number.
        for i in y_circles[0, :] : # Edge detection.
            if i[0] > size[1] or i[1] > size[0] or i[1] > size[0]*bound :
                continue
             # It skips if the iteration goes outside the bounds of the image.    
            h, s = 0.0, 0.0  # Loss function variables.
            for m in range(-r, r) : # Edge detection.
                for n in range(-r, r) :
                    if (i[1] + m) >= size[0] or (i[0] + n) >= size[1] :
                        continue
                    h += masky[i[1] + m, i[0] + n] # Central co-ordinates of the circle.
                    s += 1 # The number of times (count) the itertion has gone outside the bounds of the image.
            if h/s > 50 : # Condition for reducing the loss (epoch value).
                cv2.circle(cimg, (i[0], i[1]), i[2] + 10, (0, 255, 0), 2)
                cv2.circle(masky, (i[0], i[1]), i[2] + 30, (255, 255, 255), 2)
                # Prints the circle around the detected colour.
                cv2.putText(cimg, 'AMBER GET READY', (i[0], i[1]), font, 1, (255, 0, 0), 2, cv2.LINE_AA) # The values in the tuple are in the order - BGR.
                # Prints the text on the output image.
    cv2.imshow('Detected results', cimg) # Prints the output images.
    cv2.imwrite(path + '//result//'+file, cimg) # It saves the images in the specified path.
    cv2.waitKey(0) # This command doesn't delay in displaying the next image.
    cv2.destroyAllWindows() # This command will destroy all created windows.
   
    Loss = abs(100 - (h/s)) # Calculates the loss.
    print(Loss/100, '%') # Prints the loss.

    if __name__ == '__main__' : # Main function.
    path = os.path.abspath('..') + '//light//' # The address of folder which has the datasets.
    for f in os.listdir(path) : # f, the iteration variable iterates through every single file stored in the particular folder. 
        print(f) # Prints the name of every image stored in the specified folder.
        if f.endswith('.jpg') or f.endswith('.JPG') or f.endswith('.png') or f.endswith('.PNG') or f.endswith('.jpeg') or f.endswith('.JPEG') : # This command will check for images in the folder.
            detect(path, f) # Function call.
