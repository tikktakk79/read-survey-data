import cv2
import numpy as np
import image_handling.pixel_comp as px
import image_handling.match_test2 as match2

def check_none(img_file):
    img = cv2.imread(img_file)

    # cv2.imshow('image in', img)
    # cv2.waitKey(2000)

    """     img_slice = img[18:30, 110:190]



    ret, img_slice_proc = cv2.threshold(img_slice,127,255,cv2.THRESH_BINARY)

    cv2.imshow('sliced image', img_slice)
    cv2.waitKey(2000)

    img_arr = np.array(img_slice_proc)

    # cv2.imwrite("slice_ingen.png", img_arr)

    template = np.array(cv2.imread("slice_ingen.png"))

    matches = px.compare("slice_ingen.png", img_slice_proc)

    # print("matches", matches)

    ret, template_proc = cv2.threshold(template,127,255,cv2.THRESH_BINARY)
    template_proc = np.array(template_proc)

    cv2.imshow('template', template)
    cv2.waitKey(2000) """

    a = match2.detect_template(img_file, "./img/i_no_data.png", 12000000)

    print("matching no data", a)

    if len(a) != 0:
        print("NO DATA")
        return True
    else:
        print("DATA EXISTS!!!")
        return False