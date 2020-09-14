import cv2
import image_handling.match_test2 as detection
import image_handling.slicer as slicer
import image_handling.pixel_comp as px
import image_handling.data_conversion as dcon


def get_data(img_file):
    (img_arr, resp_img) = slicer.slice_image(img_file)

    answers_arr = px.compare_multi(img_arr, resp_img)
    answers_arr = dcon.make_numbers(answers_arr)

    return answers_arr




