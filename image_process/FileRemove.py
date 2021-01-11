import os

path_image = 'C:/Users/wxn/Desktop/fq_data/VOCdevkit/VOC2007/Annotations'
file_format = '.xml'
files_image = os.listdir(path_image)
for i in files_image:
    if (i[6:] == file_format) & (int(i[0:6])>=95) & (int(i[0:6])<=396) & (int(i[0:6])%2==1):
        print(int(i[0:6]))
        os.remove(path_image+'/'+i)