import os

path_image = 'C:/Users/wxn/Desktop/20201213redcar_data2_xml'
files_image = os.listdir(path_image)
j=432
for i in files_image:
    if i[6:] == '.xml':
        os.rename(path_image+'/'+i, path_image+'/'+str(j).zfill(6)+'.xml')
        j=j+1
# for k in range(1000):
#     m = 0
#     j = j + 1
#     for i in files_image:
#         if i[0:6] == str(k).zfill(6):
#             if i[6:] == '.jpg':
#                 os.rename(path_image + '/' + i, path_image + '/' + str(j).zfill(6) + '.jpg')
#                 print('!'*10)
#                 m=m+1
#                 print(m)
#             if i[6:] == '.xml':
#                 os.rename(path_image + '/' + i, path_image + '/' + str(j).zfill(6) + '.xml')
#                 m = m + 1
#             if m == 2:
#                 break
