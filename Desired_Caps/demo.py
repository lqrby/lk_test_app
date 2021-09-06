# 1.读取yaml文件得数据，并转换成python对象
# 2.打开yaml文件
# 3.使用yaml得load（）函数
from Common.splicing import caps
import os
import yaml

#
fs = open(os.path.join(caps, "demo.yaml"), encoding="utf-8")
rs = yaml.load(fs)
print(rs)
