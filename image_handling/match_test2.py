# importing libraries
import numpy as np
import imutils
import cv2
import os

os.chdir("../quicksearch")

# Resizes a image and maintains aspect ratio
def maintain_aspect_ratio_resize(image, width=None, height=None, inter=cv2.INTER_AREA):
    # Grab the image size and initialize dimensions
    dim = None
    (h, w) = image.shape[:2]

    # Return original image if no need to resize
    if width is None and height is None:
        return image

    # We are resizing height if width is none
    if width is None:
        # Calculate the ratio of the height and construct the dimensions
        r = height / float(h)
        dim = (int(w * r), height)
    # We are resizing width if height is none
    else:
        # Calculate the ratio of the 0idth and construct the dimensions
        r = width / float(w)
        dim = (width, int(h * r))

    # Return the resized image
    return cv2.resize(image, dim, interpolation=inter)

# Load template, convert to grayscale, perform canny edge detection

def detect_template(main_image, template_image, sensitivity = 900000):
    template = cv2.imread(template_image)
    template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
    template = cv2.Canny(template, 50, 200)
    (tH, tW) = template.shape[:2]
    cv2.imshow("template", template)

    # Load original image, convert to grayscale
    original_image = cv2.imread(main_image)
    gray = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
    found = None
    found2 = None
    arr = []

    # Dynamically rescale image for better template matching
    for scale in np.linspace(0.9, 1.1, 50)[::-1]:
        # Resize image to scale and keep track of ratio
        resized = maintain_aspect_ratio_resize(gray, width=int(gray.shape[1] * scale))
        r = gray.shape[1] / float(resized.shape[1])

        # Stop if template image size is larger than resized image
        if resized.shape[0] < tH or resized.shape[1] < tW:
            break

        # Detect edges in resized image and apply template matching
        canny = cv2.Canny(resized, 50, 200)
        detected = cv2.matchTemplate(canny, template, cv2.TM_CCOEFF)
        (_, max_val, _, max_loc) = cv2.minMaxLoc(detected)


        # Uncomment this section for visualization
        '''
        clone = np.dstack([canny, canny, canny])
        cv2.rectangle(clone, (max_loc[0], max_loc[1]), (max_loc[0] + tW, max_loc[1] + tH), (0,255,0), 2)
        cv2.imshow('visualize', clone)
        cv2.waitKey(0)
        '''


        # Keep track of correlation value
        # Higher correlation means better match



        found = (max_val, max_loc, r)

        if found is not None and found not in arr and max_val > sensitivity:
            # print("MAX LOC", max_loc)
            arr.append(found)
        found = (max_val, max_loc, r)


        # print(max_val)


    for thistuple in arr:
        # Compute coordinates of bounding box
        (_, max_loc, r) = thistuple
        (start_x, start_y) = (int(max_loc[0] * r), int(max_loc[1] * r))
        (end_x, end_y) = (int((max_loc[0] + tW) * r), int((max_loc[1] + tH) * r))

        # Draw bounding box on ROI

        # cv2.rectangle(original_image, (start_x, start_y), (end_x, end_y), (0,255,0), 2)


    # cv2.imshow('detected', original_image)
    # cv2.imwrite('detected.png', original_image)
    # cv2.waitKey(0)

    arr.sort(key= lambda tup: tup[0], reverse=True)

    return arr


def detect_numbers(img, sensitivity):

    char_arr = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    for char in char_arr:
        temp_arr.append("template_" + char + ".png")

    numbers_pos = []

    for temp in [temp_arr[3]]:
        detections = detect_template(img, temp, sensitivity)
        unique = []

        if len(detections) != 0:

            for i in range(0, len(detections)):
                duplicate = False
                for j in unique:
                    if (abs(detections[i][1][0] - j[1][0]) < 5):
                        duplicate = True

                for index, value in enumerate(numbers_pos):
                    for w, q in enumerate(value):

                        if (isinstance(q[1][0], int) and abs(detections[i][1][0] - q[1][0]) < 5):
                            if(q[0] >= detections[i][0]):
                                duplicate = True
                                # input("Duplicate - Press Enter to continue...")
                            else:
                                numbers_pos[index].pop(w)
                if not duplicate:
                    unique.append(detections[i])

        numbers_pos.append(unique)
        unique.append(temp.split("te_")[1])

    return numbers_pos



