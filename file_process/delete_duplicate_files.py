import os
# 读取path目录下的文件名，返回文件名list列表
def readFileName(path):
    lists = []
    for root, dirs, files in os.walk(path):
        for file in files:
            lists.append(os.path.join(root, file))
    return lists

# 删除路径为filepath的文件
def delFile(filepath):
    os.remove(filepath)
    print("ok")

L = os.listdir(r'E:\照片&视频\照片\20200510存')
print(L)
for i in L:
    print(i)