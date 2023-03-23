import os
import xml.dom.minidom
import math

import labelme_json


def get_pic_path(path, pic_list):
    """
    遍历文件夹得到xml文件路径列表
    :param path: 需要遍历的文件夹
    :param pic_list: 存储图片路径的列表
    :return: None
    """
    dirs = os.listdir(path)
    for dir in dirs:
        if os.path.isdir(path+"\\"+dir):
            get_pic_path(path+"\\"+dir, pic_list)
        elif ".xml" in dir:
            pic_list.append(os.path.join(path, dir))


def read_xml(xmlfile_path):
    shapes = []
    # 打开xml文档
    dom = xml.dom.minidom.parse(xmlfile_path)
    # 得到文档元素对象
    root = dom.documentElement

    # 获取imagePath
    path = root.getElementsByTagName('path')[0].firstChild.data
    # print(path)
    imagePath = os.path.basename(path)
    # print(imagePath)

    # 获取imageHeight
    imageHeight = root.getElementsByTagName('height')[0].firstChild.data
    # print(imageHeight)

    # 获取imageWidth
    imageWidth = root.getElementsByTagName('width')[0].firstChild.data

    # 获取label
    label = root.getElementsByTagName('name')[0].firstChild.data
    #print(label)

    # 获取filename
    filename = root.getElementsByTagName('filename')[0].firstChild.data

    # 获取矩形四个角点坐标
    cx = float(root.getElementsByTagName('cx')[0].firstChild.data)
    cy = float(root.getElementsByTagName('cy')[0].firstChild.data)
    w = float(root.getElementsByTagName('w')[0].firstChild.data)
    h = float(root.getElementsByTagName('h')[0].firstChild.data)
    angle = float(root.getElementsByTagName('angle')[0].firstChild.data)
    x1 = cx + w / 2 * math.cos(angle) - h / 2 * math.sin(angle)
    y1 = cy - w / 2 * math.sin(angle) - h / 2 * math.cos(angle)

    x2 = cx - w / 2 * math.cos(angle) - h / 2 * math.sin(angle)
    y2 = cy + w / 2 * math.sin(angle) - h / 2 * math.cos(angle)

    x3 = cx - w / 2 * math.cos(angle) + h / 2 * math.sin(angle)
    y3 = cy + w / 2 * math.sin(angle) + h / 2 * math.cos(angle)

    x4 = cx + w / 2 * math.cos(angle) + h / 2 * math.sin(angle)
    y4 = cy - w / 2 * math.sin(angle) + h / 2 * math.cos(angle)
    # print(x1, y1, x2, y2, x3, y3, x4, y4)
    points = [[x1, y1], [x2, y2], [x3, y3], [x4, y4]]

    shapes.append(labelme_json.shape(label, points, "polygon"))
    labelme = labelme_json.labelme_json(shapes, imagePath, imageHeight, imageWidth, filename)
    shapes.clear()
    return labelme


if __name__ == "__main__":
    xml_paths = []
    path = r"F:\templateMatching"
    get_pic_path(path, xml_paths)
    # print(xml_paths)
    for xml_file in xml_paths:
        print(xml_file)
        labelme = read_xml(xml_file)
        # print(labelme.shapes)
        labelme.write_to_file(os.path.dirname(xml_file)+"\\"+labelme.filename + ".json")
