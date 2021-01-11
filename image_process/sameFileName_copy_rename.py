import os
from shutil import copy
path_image1 = 'D:/wxn/redcar/data1'
path_image2 = 'C:/Users/wxn/Desktop/100'
files_image = os.listdir(path_image1)
j=0
for i in files_image:
    if j%5==0:
        copy(path_image1+'/'+i, path_image2)
    j=j+1
files_image2 = os.listdir(path_image2)
j=0
for i in files_image2:
    os.rename(path_image2+'/'+i, path_image2+'/'+str(j).zfill(6)+'.jpg')
    j=j+1