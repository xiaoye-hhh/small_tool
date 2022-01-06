import cv2
import os
import random


if not os.path.exists('./part'):
    os.mkdir("part")

def fourSqureSplit(num:int = -1):
    """ 进行四个角的裁剪，可以得到一些低质量数据 """
    DIR_PATH = './campus'
    files = os.listdir(DIR_PATH)
    num = len(files) if num == -1 else num

    for i, file in enumerate(files):
        path = os.path.join(DIR_PATH, file)
        im = cv2.imread(path)

        H, W, C = im.shape
       
        w1 = int(W * random.random() * 0.2 +  W * 0.4) 
        w2 = int(W * random.random() * 0.2 +  W * 0.4) 
        h1 = int(H * random.random() * 0.2 +  H * 0.4) 
        h2 = int(H * random.random() * 0.25 +  H * 0.45) 


        # 左上
        cv2.imwrite(os.path.join('./part', f"left_up_{file}"), im[:h1, :w1])
        # 左下
        cv2.imwrite(os.path.join('./part', f"left_down_{file}"), im[-h2:, :w1])
        # 右上
        cv2.imwrite(os.path.join('./part', f"right_up_{file}"), im[:h1, -w2:])
        # 右下
        cv2.imwrite(os.path.join('./part', f"right_down_{file}"), im[-h2:, -w2:])

        if i == num:
            break


def centralSplit(num:int = -1):
    """ 取一些正中间的数据 """
    DIR_PATH = './campus'
    files = os.listdir(DIR_PATH)
    num = len(files) if num == -1 else num

    for i, file in enumerate(files):
        path = os.path.join(DIR_PATH, file)
        im = cv2.imread(path)

        H, W, C = im.shape
       
        w1 = int(W * random.random() * 0.2 +  W * 0.1) 
        w2 = int(W * random.random() * 0 +  W * 0.1) 
        h1 = int(H * random.random() * 0.5 +  H * 0.5) 

        cv2.imwrite(os.path.join('./part', f"central_up_3_{file}"), im[:h1, w1:-w2])

        if i == num:
            break


if __name__ == '__main__':
    # fourSqureSplit()
    centralSplit()