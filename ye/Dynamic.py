"""
    Created by   莜叶
    Time         17-7-7
    github       https://github.com/youyeyuki/Combination_Tool/
    description  动态修改配置文件(生产环境请不要使用 注意检查安全值)
    author_email youyeku@gmail.com
    Reprinted link 需要说明出处
"""

import os
from threading import Thread
import importlib
import time
# import ye.conf  as conf
from ye import conf as conf

def watch_loop():
    while True:
        print(conf.ip)
        time.sleep(2)


class auto_load():

    def __init__(self,file_name):
        self.mdf_time = ""
        self.file_name =file_name
        self.main()
    def main(self):
        # 开启监控
        Thread(target=self.moniter).start()

        # 观察变量情况
        watch_loop()



    def moniter(self):
        while True:
            mdf_time = os.path.getmtime(self.file_name)
            if self.mdf_time != mdf_time :
                #todo 检查变量是否为空 空的话要报错
                print("配置改变重新加载")
                importlib.reload(conf)
                time.sleep(2)
                self.mdf_time=mdf_time
# https://juejin.im/entry/570c6b6771cfe40067310370 请放在单独包测试
if __name__ == '__main__':

    auto_load("conf.py")
