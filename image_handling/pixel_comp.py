import cv2
import numpy as np

char_arr = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
temp_arr = []

for char in char_arr:
    temp_arr.append("./img/template_" + char + ".png")


def compare(temp_file, img, start_point = 0, dist_end = 0):
    # print("Running compare with start point: ", start_point, "and dist end ", dist_end)
    temp = np.array(cv2.imread(temp_file))

    if isinstance(img, str):
        img = cv2.imread(img)

    temp_height = temp.shape[0]
    temp_width = temp.shape[1]
    img_width = img.shape[1]
    img_height = img.shape[0]
    matches = []

    for i in range(start_point, img_width - temp_width - dist_end):
        # print("X-index: ", i)
        comp_img = np.array(img[0:img_height, i:i + temp_width].copy())
        height, width, channels = comp_img.shape

        # print(temp_file)
        # print("Temp", temp_height, temp_width)
        # print("Comp img", height, width, channels)

        if (comp_img==temp).all():
            # print("X-POS is: ", i)
            # print("It's aHIT!!!")
            matches.append(i)

    return matches

def compare_multi(img_arr, resp_img):
    numbers_pos = []
    # Looping through the cropped images
    img = cv2.imread("./img/template_(.png")

    for index, img in enumerate(img_arr):
        print("INDEX", index)
        cv2.imwrite("img_slize" + str(index) + ".png", img)
        left_thesis = compare("./img/template_(.png", img)
        right_thesis = compare("./img/template_).png", img)
        img_width = img.shape[1]
        hits = []

        # Looping through the array of number images 0 - 9
        print("Left thesis: ", left_thesis, "Right thesis: ", right_thesis)
        print("Loop through cropped image: ")


        for temp_img in temp_arr:
            # hits.append(temp_img.split("_")[1])
            if (len(left_thesis) > 0 and len(right_thesis) > 0):
                hits.append(compare(temp_img, img, left_thesis[0] + 2, img_width - right_thesis[0] - 3))

        numbers_pos.append(hits)

    resp_hits = []

    cv2.imwrite("resp_img.png", resp_img)

    print("::::::::Compare RESP IMG:::::::")

    for temp_img in temp_arr:
        # resp_hits.append("R_" + temp_img.split("_")[1])
        resp_hits.append(compare(temp_img, resp_img))

    numbers_pos.append(resp_hits)

    return numbers_pos









