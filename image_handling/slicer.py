import cv2

def slice_image(img_file):
    answers_img = []
    img = cv2.imread(img_file)

    for x in range(7):
        y_step = 28
        ans_img = img[16 + y_step * x:33 + y_step * x, 148:524].copy()

        ret,ans_img_black = cv2.threshold(ans_img,127,255,cv2.THRESH_BINARY)
        answers_img.append(ans_img_black)

    resp_img = img[218:235, 503:541]

    # Convert resp image to black and white
    ret,resp_img_black = cv2.threshold(resp_img,127,255,cv2.THRESH_BINARY)

    return [answers_img, resp_img_black]

def slice_pthesis(xmin, xmax, img):
    height = img.shape[0]
    result_img = img[0:height, xmin - 4:xmax + 4]
    # cv2.imshow("cropped", result_img)
    # cv2.waitKey(3000)
    return result_img
