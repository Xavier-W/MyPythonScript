# -*- coding: utf-8 -*-
# @Time : 2020/12/22 17:51
# @Author : Wu Xianning
# @Desc : xml_process.py
import os
from xml.etree.ElementTree import ElementTree, Element
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import random


def read_xml(in_path):
    '''''读取并解析xml文件
       in_path: xml路径
       return: ElementTree'''
    tree = ElementTree()
    tree.parse(in_path)
    return tree


def write_xml(tree, out_path):
    '''''将xml文件写出
       tree: xml树
       out_path: 写出路径'''
    tree.write(out_path, encoding="utf-8", xml_declaration=True)


def if_match(node, kv_map):
    '''''判断某个节点是否包含所有传入参数属性
       node: 节点
       kv_map: 属性及属性值组成的map'''
    for key in kv_map:
        if node.get(key) != kv_map.get(key):
            return False
    return True


# ----------------search -----------------
def find_nodes(tree, path):
    '''''查找某个路径匹配的所有节点
       tree: xml树
       path: 节点路径'''
    return tree.findall(path)


def get_node_by_keyvalue(nodelist, kv_map):
    '''''根据属性及属性值定位符合的节点，返回节点
       nodelist: 节点列表
       kv_map: 匹配属性及属性值map'''
    result_nodes = []
    for node in nodelist:
        if if_match(node, kv_map):
            result_nodes.append(node)
    return result_nodes


# ---------------change ----------------------
def change_node_properties(nodelist, kv_map, is_delete=False):
    '''修改/增加 /删除 节点的属性及属性值
       nodelist: 节点列表
       kv_map:属性及属性值map'''
    for node in nodelist:
        for key in kv_map:
            if is_delete:
                if key in node.attrib:
                    del node.attrib[key]
            else:
                node.set(key, kv_map.get(key))


def change_node_text(nodelist, text, is_add=False, is_delete=False):
    '''''改变/增加/删除一个节点的文本
       nodelist:节点列表
       text : 更新后的文本'''
    for node in nodelist:
        if is_add:
            node.text += text
        elif is_delete:
            node.text = ""
        else:
            node.text = text


def create_node(tag, property_map, content):
    '''新造一个节点
       tag:节点标签
       property_map:属性及属性值map
       content: 节点闭合标签里的文本内容
       return 新节点'''
    element = Element(tag, property_map)
    element.text = content
    return element


def add_child_node(nodelist, element):
    '''''给一个节点添加子节点
       nodelist: 节点列表
       element: 子节点'''
    for node in nodelist:
        node.append(element)


def del_node_by_tagkeyvalue(nodelist, tag, kv_map):
    '''''同过属性及属性值定位一个节点，并删除之
       nodelist: 父节点列表
       tag:子节点标签
       kv_map: 属性及属性值列表'''
    for parent_node in nodelist:
        children = parent_node.getchildren()
        for child in children:
            if child.tag == tag and if_match(child, kv_map):
                parent_node.remove(child)


if __name__ == "__main__":
    import os
    import xml.etree.ElementTree as ET

    path = u"D:/wxn/2020_12_work/20201221dataset/xml"  # xml文件所在的目录
    files = os.listdir(path)  # 得到文件夹下所有文件名称
    for xmlFile in files:
        xmlPath = os.path.join(path, xmlFile)
        tree = ET.parse(xmlPath)
        root = tree.getroot()

        for child in root:
            # print('1:',child.tag,child.text)
            if child.tag == 'object':
                for sub in child:
                    # print('2:',sub.tag, sub.text)
                    if sub.tag == 'name':
                        if sub.text == 'redcarwwd':
                            print("{}".format(xmlPath))
                            sub.text = 'redcar'
        tree.write(xmlPath)


    # width_arr = []
    # height_arr = []
    # for xmlFile in files:  # 遍历文件夹
    #     # print(xmlFile)
    #     xmlPath = os.path.join(path, xmlFile)
    #     xmlPartName = xmlFile.split(".")[0]
    #
    #     imageFile = xmlPartName + ".jpg"
    #     imagePath = os.path.join(u"E:\\UnderWaterDetection\\720_480\\train\\image\\", imageFile)
    #     fileHandle = open(imagePath, 'rb')
    #     img = Image.open(fileHandle)
    #
    #     ################ 1. 读取xml文件  ##########
    #     tree = read_xml(xmlPath)
    #     root = tree.getroot()
    #     '''
    #     ################ 删除特定类别  ##########
    #     for obj in root.iter('object'):  # 获取object节点中的name子节点
    #         name = obj.find("name").text
    #         if name == 'waterweeds':
    #             print(xmlFile)
    #             root.remove(obj)
    #             write_xml(tree, xmlPath)
    #     '''
    #
    #     # ################ 删除标注物体为空的标注文件与对应图片  ##########
    #     # obj = root.find("object")
    #     # if obj == None:
    #     #     fileHandle.close()
    #     #     os.remove(imagePath)
    #     #     os.remove(xmlPath)
    #     #     print(xmlFile)
    #
    #     '''
    #     ################ 根据xml生成可视化工具所需txt ###############
    #     txtPath = u"E:\\UnderWaterDetection\\车牌字符检测标注工具\\data\\720_480\\train\\image\\标注信息\\" + xmlPartName + ".txt"
    #     f = open(txtPath, 'w')
    #     size = root.find("size")
    #     orgin_width = size.find("width").text
    #     orgin_height = size.find("height").text
    #     f.write("<?xml version='1.0' encoding='GB2312'?>\n")
    #     f.write("<info>\n")
    #     f.write("	<src width=\"" + str(orgin_width) + "\" height = \"" + str(orgin_height) + "\" depth = \"" + str(3) + "\">" + imageFile + "</src>\n")
    #     for obj in root.iter('object'):  # 获取object节点中的name子节点
    #         name = obj.find("name")
    #         bndbox_node = obj.find("bndbox")
    #         xmin_node = bndbox_node.find("xmin")
    #         ymin_node = bndbox_node.find("ymin")
    #         xmax_node = bndbox_node.find("xmax")
    #         ymax_node = bndbox_node.find("ymax")
    #         f.write("	<object id=\"02720149-03FF-4866-" + str(random.randint(0, 1000000)) + "-" + str(random.randint(0, 1000000)) + "\">\n")
    #         f.write("		<rect lefttopx=\"" + xmin_node.text + "\" lefttopy = \"" + ymin_node.text + "\" rightbottomx = \"" + xmax_node.text + "\" rightbottomy = \"" + ymax_node.text + "\"></rect>\n")
    #         f.write("		<type>" + name.text + "</type>\n")
    #         f.write("		<descriinfo></descriinfo>\n")
    #         f.write("		<modifydate>2020-03-20 16:32:00</modifydate>\n")
    #         f.write("	</object>\n")
    #     f.write("</info>\n")
    #     f.close()
    #     '''
    #     '''
    #     ################ 训练集重设尺寸 ###############
    #     new_width = 300
    #     new_hieght = 300
    #     size = root.find("size")
    #     orgin_width = size.find("width")
    #     orgin_height = size.find("height")
    #     resize_img = img.resize((new_width, new_hieght), Image.ANTIALIAS)
    #     resize_img.save("E:\\UnderWaterDetection\\300_300\\train\\image\\" + imageFile)
    #     radio_width = float(new_width) / int(orgin_width.text)
    #     radio_height = float(new_hieght) / int(orgin_height.text)
    #     orgin_width.text = str(new_width)
    #     orgin_height.text = str(new_hieght)
    #
    #     for obj in root.iter('object'):  # 获取object节点中的name子节点
    #         bndbox_node = obj.find("bndbox")
    #         xmin_node = bndbox_node.find("xmin")
    #         xmin_node.text = str(int(int(xmin_node.text) * radio_width))
    #         ymin_node = bndbox_node.find("ymin")
    #         ymin_node.text = str(int(int(ymin_node.text) * radio_height))
    #         xmax_node = bndbox_node.find("xmax")
    #         xmax_node.text = str(int(int(xmax_node.text) * radio_width))
    #         ymax_node = bndbox_node.find("ymax")
    #         ymax_node.text = str(int(int(ymax_node.text) * radio_height))
    #     '''
    #     '''
    #     ################ 坐标越界检查 ###############
    #     for obj in root.iter('object'):  # 获取object节点中的name子节点
    #         bndbox_node = obj.find("bndbox")
    #         xmin_node = bndbox_node.find("xmin")
    #         ymin_node = bndbox_node.find("ymin")
    #         xmax_node = bndbox_node.find("xmax")
    #         ymax_node = bndbox_node.find("ymax")
    #         if int(xmin_node.text) <= 0:
    #             xmin_node.text = "0"
    #         if int(ymin_node.text) <= 0:
    #             ymin_node.text = "0"
    #         if int(xmax_node.text) > img.size[0]:
    #             xmax_node.text = str(img.size[0])
    #         if int(ymax_node.text) > img.size[1]:
    #             ymax_node.text = str(img.size[1])
    #     '''
    #     '''
    #     #################  获取训练集标注物体长宽分布 ##############
    #     for obj in root.iter('object'):  # 获取object节点中的name子节点
    #         bndbox_node = obj.find("bndbox")
    #         xmin_node = bndbox_node.find("xmin")
    #         ymin_node = bndbox_node.find("ymin")
    #         xmax_node = bndbox_node.find("xmax")
    #         ymax_node = bndbox_node.find("ymax")
    #         width = int(xmax_node.text) -  int(xmin_node.text)
    #         height = int(ymax_node.text) - int(ymin_node.text)
    #         width_arr.append(width)
    #         height_arr.append(height)
    #     '''
    #     '''
    #     #################  添加图片信息 ##############
    #     a = create_node("size", {}, "") # 新建节点
    #     w = create_node("width", {}, str(img.size[0])) # 新建节点
    #     a.append(w)
    #     h = create_node("height", {}, str(img.size[1]))  # 新建节点
    #     a.append(h)
    #     d = create_node("depth", {}, "3")  # 新建节点
    #     a.append(d)
    #     root.append(a)
    #     '''
    #     '''
    #     #################  保存修改后的xml ##############
    #     savePath = os.path.join("E:\\UnderWaterDetection\\300_300\\train\\box\\", xmlFile)
    #     write_xml(tree, savePath)
    #     '''
    # '''
    # #################  生成散点图 ##############
    # fig = plt.figure()
    # ax1 = fig.add_subplot(111)
    # ax1.set_title('训练集长宽分布')
    # plt.xlabel('width')
    # plt.ylabel('height')
    # ax1.scatter(width_arr, height_arr, c='r', marker='.')
    # plt.show()
    # '''
