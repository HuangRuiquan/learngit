import shutil

import PIL
from PIL import Image
import os


def get_user_defined_size_img(w, h, img):
    """
    修改图片尺寸
    :param w: 目标宽
    :param h: 目标高
    :param img: 源图片，格式是PIL.Image
    :return: 返回修改后的图片，格式是PIL.Image
    """
    if img.width <= w and img.height <= h:
        new_img = Image.new(img.mode, (w, h))
        y = h / 2 - img.height / 2
        x = w / 2 - img.width / 2
        new_img.paste(img, (int(x), int(y)))
        return new_img
    else:
        img.thumbnail((w, h))
        return get_user_defined_size_img(w, h, img)


def get_pic_path(path, pic_list):
    """
    遍历文件夹得到.bmp图片路径列表
    :param path: 需要遍历的文件夹
    :param pic_list: 存储图片路径的列表
    :return: None
    """
    dirs = os.listdir(path)
    for d in dirs:
        if os.path.isdir(path + "\\" + d):
            get_pic_path(path + "\\" + d, pic_list)
        elif ".bmp" in d:
            pic_list.append(os.path.join(path, d))


def text():
    path = r'D:\AI标注\V5000\20230206\维修站'
    pic_path_list = []
    error_path = []
    get_pic_path(path, pic_path_list)
    # print(pic_path_list)
    for pic_path in pic_path_list:
        try:
            img = Image.open(pic_path)
        except PIL.UnidentifiedImageError:
            error_path.append(pic_path)
            continue
        new_img = get_user_defined_size_img(960, 960, img)

        print(new_img.size)
        new_img.save(pic_path)
        if not os.path.exists(os.path.dirname("D:\\work\\processed" + str.split(pic_path, ':')[1])):
            os.makedirs(os.path.dirname("D:\\work\\processed" + str.split(pic_path, ':')[1]))
        shutil.move(pic_path, "D:\\work\\processed" + str.split(pic_path, ':')[1])
    print("处理失败图片{0}张:".format(error_path.__len__()))
    print_string_list(error_path)


def print_string_list(str_list):
    for string in str_list:
        print("     " + string)


if __name__ == "__main__":
    text()
