# -*- coding: utf-8 -*-
import os
from bs4 import BeautifulSoup
from urllib import request
import argparse

# 你觉得这是什么就是什么
print("\t\tPaperDown 0.1")
print("\tFirst Auther: Xiao_Jin")
print()

# 初始化ArgParse
ap = argparse.ArgumentParser()
ap.add_argument("-aria2", "--aria2", required=True, help="下载时所需的Aria2程序路径")
ap.add_argument("-save", "--save", required=True, help="保存paperclip-***.jar文件的路径")
args = vars(ap.parse_args())

# 获取版本号
print("\a正在获取版本信息...")
req = request.Request(url="https://papermc.io/ci/job/Paper-1.14/", headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36"})  # 没有UA会403
htmldoc_byte = request.urlopen(req)
content = htmldoc_byte.read().decode()  # 解码

soup = BeautifulSoup(content, "html5lib")  # pip3 install html5lib
all_a_tag = soup.find_all("a")  # 辣鸡办法拿所有<a>

dot_jar_location_in_str = str(all_a_tag).find(".jar")  # 海底捞针（定位）
paper_ver_location = dot_jar_location_in_str - 3  # 小学数学减掉版本号的三位长度
paper_ver = str(all_a_tag)[paper_ver_location:dot_jar_location_in_str]  # 提取三位版本号
print("\a目前PaperClip的最新构件号为 >>> " + paper_ver)  # 没什么用甚至听不到的声音

# Aria2c下载文件
url_of_jar = "https://papermc.io/ci/job/Paper-1.14/lastSuccessfulBuild/artifact/paperclip-" + paper_ver +".jar"  # 地址拼接

aria2c_path = r"" + args["aria2"]  # 再次拼接
aria2c_cmd = aria2c_path + " -x16 -d " + args["save"] + " " + url_of_jar  # aria2致命参数
os.system(aria2c_cmd)
print()

# 编译&启动      等下个版本吧（逃
exit("\a感谢使用 PaperDown")
