import os
from shutil import copy
# 寻找两个文件夹中的同名文件，并复制到其中一个文件夹
path_image = 'C:/Users/wxn/Desktop/新建文件夹'   # 图像文件夹
path_xml = 'F:/VOC2007/Annotations'             # xml文件夹
files_image = os.listdir(path_image)
files_xml = os.listdir(path_xml)
for i in files_image:
    for j in files_xml:
        if i[0:6]==j[0:6]:      # 前6位字符相同
            print(j[0:6])
            copy(path_xml+'/'+j, path_image)        # 复制文件到path_image
