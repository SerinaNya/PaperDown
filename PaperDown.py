# -*- coding: utf-8 -*-
import os
import json
from urllib import request
import argparse

# 脚本信息
print("\t\tPaperDown 0.2")
print("\tFirst Auther: Xiao_Jin")
print()

# 初始化ArgParse
ap = argparse.ArgumentParser()
ap.add_argument("-aria2", "--aria2", required=True, help="下载时所需的Aria2程序路径")
ap.add_argument("-save", "--save", required=True, help="保存paper-***.jar文件的路径")
args = vars(ap.parse_args())

# 获取Paper支持的最新的Minecraft版本
print("[PaperDown] 正在获取Paper最新的Minecraft版本信息...")
mc_ver_json_req = request.Request(url="https://papermc.io/api/v1/paper", headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36"})  # 没有UA会403
mc_ver_byte = request.urlopen(mc_ver_json_req)
mc_ver_json = mc_ver_byte.read().decode()
mc_ver_py = json.loads(str(mc_ver_json))
latest_mc_ver = mc_ver_py['versions'][0]
print("\a[PaperDown] 目前Paper支持的的最新Minecraft版本为 >>> Minecraft " + latest_mc_ver)  # 没什么用甚至听不到的声音

# 获取Build ID
print("[PaperDown] 正在获取Paper-" + latest_mc_ver + "最新的Build ID...")
paper_bid_json_req = request.Request(url="https://papermc.io/api/v1/paper/" + latest_mc_ver + "/latest", headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36"})  # 没有UA会403
paper_bid_byte = request.urlopen(paper_bid_json_req)
paper_bid_json = paper_bid_byte.read().decode()
paper_bid_py = json.loads(str(paper_bid_json))
paper_latest_bid = paper_bid_py['build']

print("\a[PaperDown] 目前Paper-" + latest_mc_ver + "最新的Build ID为 >>> Build " + paper_latest_bid)  # 没什么用甚至听不到的声音

# Aria2c下载文件
print("[PaperDown] 已将下载任务移交至Aria2")
url_of_jar = "https://papermc.io/api/v1/paper/" + latest_mc_ver + "/" + paper_latest_bid + "/download"  # 地址拼接
# https://paper.readthedocs.io/en/stable/site/api.html#endpoint-documentation

aria2c_path = r"" + args["aria2"]  # 再次拼接
aria2c_cmd = aria2c_path + " -x16 -s16 -d " + args["save"] + " " + url_of_jar  # aria2致命参数
os.system(aria2c_cmd)
print() # 空一行

# 编译&启动      等下个版本吧（逃
exit("\a[PaperDown] 感谢使用 PaperDown :D")
