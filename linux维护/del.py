"""
    - 需要配置: 
        文件路径:
            TRASH_PATH: 垃圾邮件文件夹
            RECORD_PATH: 日志文件路径
            MAX_RECORD: 最大的记录条数

        修改.bashrc，添加 alias del='python3 xxx/xxx/del.py' 绝对路径

    - 简单原理:
        使用del时，先将其移动到.trash文件夹；同时，维护一个.record文件，当其中的条目数一定时，删除文件

"""



import sys
import os
import shutil
import pickle


TRASH_PATH = '/home/fxy/.trash'
RECORD_PATH = '/home/fxy/.trash/.record'
MAX_RECORD = 2

def find_valid_name(path):
    if not os.path.exists(path):
        return path
    else:
        count = 0
        while True:
            cur_path = f'{path}_{count}'
            if not os.path.exists(cur_path):
                return cur_path
            else:
                count += 1

if __name__ == '__main__':
    # 创建目录
    if not os.path.exists(TRASH_PATH):
        os.mkdir(TRASH_PATH)

    # 记录文件
    if not os.path.exists(RECORD_PATH):
        records = []
    else:
        with open(RECORD_PATH, 'rb') as f:
            records = pickle.load(f)
    
    # 如果溢出，删除
    if len(records) > MAX_RECORD:
        tmp_file = records.pop(0)
        if os.path.isdir(tmp_file):
            os.rmdir(tmp_file)
        else:
            os.remove(tmp_file)
    
    # 处理需要删除的文件
    files = sys.argv[1:]
    cur_path = os.getcwd()
    for file in files:
        src = os.path.join(cur_path, file)
        dst = os.path.join(TRASH_PATH, file)
        dst = find_valid_name(dst)
        try:
            shutil.move(src, dst) 
            records.append(dst)
        except FileNotFoundError:
            print(f"不存在文件: {file}")

    # 保存信息
    with open(RECORD_PATH, 'wb') as f:
        pickle.dump(records, f)