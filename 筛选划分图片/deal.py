import cv2
import os
import shutil

# 检测一下文件夹是否存在
if not os.path.exists('./good'):
    os.mkdir('good')
if not os.path.exists('./bad'):
    os.mkdir('bad')



if __name__ == '__main__':
    # 源目录
    SOURCE_DIR = './Market-1501/bounding_box_test'

    files = os.listdir(SOURCE_DIR)
    print(f"文件总数为：{len(files)}")

    # 开始挨个判断
    for file in files:
        src_path = os.path.join(SOURCE_DIR, file)
        im = cv2.imread(src_path)
        im = cv2.resize(im, (200, 400))
        cv2.imshow('0', im)

        print(file)
        key = cv2.waitKey(0)
        if key == 32: # 空格键，按起来轻松点，保存到good
            dst_path = os.path.join('./good', file)
        elif key == ord('p'): # 跳过
            continue
        elif key == ord('q'): # 退出
            break
        else: # 移动到bad
            dst_path = os.path.join('./bad', file)

        shutil.move(src_path, dst_path)