
def multi_image_cut(data_path, img_num, save_path):
    '''
    将多张图片切割为宽高最大的相同大小
    Args:
        data_path: 原数据存储路径
        img_num: 图片数量
        save_path: 切割后的图片存储路径

    Returns:

    '''
    from PIL import Image
    import numpy as np

    w_h = np.zeros((img_num, 2))        # 预设一个数组，存储每张图片的宽和高
    for i in range(img_num):        # 存储每张图片的宽和高
        im = Image.open(data_path + str(i) + ".jpg")
        w_h[i] = im.size
    print("图片宽高为", w_h)
    w_min = min(w_h[:, 0])        # 找出最小的宽
    h_min = min(w_h[:, 1])        # 找出最小的高
    print("最小的宽为", w_min, "最小的高为", h_min)
    centre = w_h/2        # 计算每张图的中心坐标
    x_y = centre - [w_min/2, h_min/2]
    print("每张图切割部分的左上角坐标为", x_y)

    for k in range(img_num):        # 依次切割
        im = Image.open(data_path + str(k) + ".jpg")
        region = im.crop((x_y[k][0], x_y[k][1], x_y[k][0]+w_min, x_y[k][1]+h_min))  # 裁剪区域
        region.save(save_path + "new" + str(k) + ".jpg")  # str()是裁剪后的编号

if __name__ == "__main__":
    multi_image_cut("D:\\image\\", 1617, 'D:/wxn/code/test/cut/')



