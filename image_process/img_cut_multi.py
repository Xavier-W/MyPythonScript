

def img_cut_multil(data_path, save_path, w, h, d=0, ii=0):
    '''
    对任意像素的图片裁剪为352*352，并存储其左上角坐标
    Args:
        data_path: 数据读取文件夹
        save_path: 数据存储文件夹
        w: 要分割的小图的宽度
        h: 要分割的小图的高度
        d: 重叠部分的长度，默认为0

    Returns:每张小图在大图中的左上角坐标

    '''

    from PIL import Image
    import numpy as np

    im = Image.open(data_path)
    img_size = im.size
    m = img_size[0]     # 读取图片的宽度
    n = img_size[1]     # 读取图片的高度
    w = w                  # 设置要裁剪的小图的宽度
    h = h                  # 设置要裁剪的小图的高度
    a = m//(w-d)
    b = n//(h-d)
    x = np.zeros(a+1)
    y = np.zeros(b+1)
    for i in range(a):
        x[i] = (w-d)*i
    for i in range(b):
        y[i] = (h-d)*i
    x[a] = m-w
    y[b] = n-h
    # print(x)
    # print(y)
    if (m == w) or (n == h):        # 如果输入图片刚好为需要大小，不裁
        if m == w:
            x = np.array([0])
        if n == h:
            y = np.array([0])
        p = np.zeros(shape=(x.size * y.size, 2))  # 创建一个二维数组，记录图片左上角坐标
        k = -1  # 给裁剪后的图片编号
        for i in range(y.size):
            _y = y[i]
            for j in range(x.size):
                _x = x[j]
                k = k + 1
                p[k] = [_x, _y]
                region = im.crop((_x, _y, _x + w, _y + h))  # 裁剪区域
                region.save(save_path + str(ii) + str(k) + ".jpg")  # str()是裁剪后的编号
        return x.size * y.size, p

    p = np.zeros(shape=(x.size*y.size, 2))        # 创建一个二维数组，记录图片左上角坐标
    k = -1                    # 给裁剪后的图片编号
    for i in range(y.size):
        _y = y[i]
        for j in range(x.size):
            _x = x[j]
            k = k+1
            p[k] = [_x, _y]
            region = im.crop((_x, _y, _x + w, _y + h))  # 裁剪区域
            region.save(save_path + str(ii) + str(k) + ".jpg")  # str()是裁剪后的编号
    return x.size * y.size, p

# if __name__ == "__main__":
#     import cv2
#     # for i in range(1, 16):
#     # img = cv2.imread('C:/users/wxn/Desktop/jpg/old/1 + "（"+1+"）"+".jpg"')
#     num, p = img_cut_multi(r'C:/Users/wxn/Desktop/jpg/old/6.jpg', r'C:/Users/wxn/Desktop/jpg/new/0', 352, 352, 20)
#     print(num, p)




def img_cut_multi_array(data_path, save_path, w, h, d=0):
    '''
    对任意像素的图片裁剪为352*352，并存储其左上角坐标
    Args:
        data_path: 数据读取文件夹
        save_path: 数据存储文件夹
        w: 要分割的小图的宽度
        h: 要分割的小图的高度
        d: 重叠部分的长度，默认为0

    Returns:每张小图在大图中的左上角坐标

    '''

    import cv2
    import numpy as np

    im = cv2.imread(data_path)
    # print(np.shape(im))
    img_size = im.shape
    n = img_size[0]     # 读取图片的高度
    m = img_size[1]     # 读取图片的宽度
    a = m//(w-d)
    b = n//(h-d)
    x = np.zeros(a+1)
    y = np.zeros(b+1)
    for i in range(a):
        x[i] = (w-d)*i
    for i in range(b):
        y[i] = (h-d)*i
    if (m-x[a-1])<=w:
        x[a-1]=x[a-1]-d    # 防止溢出
    if (n-y[b-1])<=h:
        y[b-1]=y[b-1]-d    # 防止溢出
    x[a] = m-w
    y[b] = n-h
    # print(x)
    # print(y)
    if (m <= w) or (n <= h):        # 输入图片小于等于裁图大小的情况
        if m <= w:
            x = np.array([0])
            w = m
        if n <= h:
            y = np.array([0])
            h = n
        p = np.zeros(shape=(x.size * y.size, 2))  # 创建一个二维数组，记录图片左上角坐标
        img_cut = np.zeros(shape=(x.size * y.size, w, h, 3))
        k = -1  # 给裁剪后的图片编号
        for i in range(y.size):
            _y = y[i]
            for j in range(x.size):
                _x = x[j]
                k = k + 1
                p[k] = [_x, _y]
                region = im[int(_y):int(_y + h), int(_x):int(_x + w)]  # 裁剪区域
                img_cut[k] = region  # 裁剪后的图像数组存储在img_cut中
        return x.size * y.size, p, img_cut

    p = np.zeros(shape=(x.size*y.size, 2))        # 创建一个二维数组，记录图片左上角坐标
    img_cut = np.zeros(shape=(x.size * y.size, h, w, 3))
    k = -1                    # 给裁剪后的图片编号
    for i in range(y.size):
        _y = y[i]
        for j in range(x.size):
            _x = x[j]
            k = k+1
            p[k] = [_x, _y]
            # print('p[k] is ', p[k])
            region = im[int(_y):int(_y + h), int(_x):int(_x + w)]  # 裁剪区域
            # print('裁剪区域为', int(_y),':',int(_y + h),',',int(_x),':',int(_x + w))
            # print('img_cut.shape is ', img_cut.shape)
            # print('region.shape is ', region.shape)
            img_cut[k] = region        # 裁剪后的图像数组存储在img_cut中
            # cv2.imshow('im', region)
            # cv2.waitKey(0)
            # cv2.imwrite(save_path +'\\'+'{}.jpg'.format(k), region)  # str()是裁剪后的编号
    return x.size * y.size, p, img_cut

if __name__ == "__main__":
    import cv2
    from PIL import Image
    import numpy as np
    # for i in range(1, 16):
    save_path = 'D:/wxn/code/test/cut/'
    # img_path = 'D:/wxn/code/test/数据包/波浪20000.jpg'
    # Image.open(img_path)
    # Image._show()
    for ii in range(20000, 21617):
        img_path = 'D:/wxn/code/test/img_flow/'+str(ii)+'.jpg'
        print(img_path)
        img = cv2.imread(img_path)
        # img = img.astype(np.uint8)
        print(img)
        img = cv2.resize(img, (960, 540))
        cv2.imwrite(img, 'D:/wxn/code/test/cut/'+str(ii)+'.jpg')
        # # num, p, cut = img_cut_multi_array(img_path, save_path , 1200, 300, 30)
        # _,_ = img_cut_multil(img_path, save_path, 1000, 600, 30, ii)
        # # print('num is {}\n p is {}\n cut is {}'.format(num,p,cut))
