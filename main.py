import os
import requests

print("欢迎来到MZ-OS!")
print("如果你需要一些帮助，请输入“帮助”")

def iput():
    global iputContent
    iputContent = input("$ ")

def oput():
    if iputContent == "退出":
        print("拜拜~")
        exit()
    elif iputContent == "清屏":
        os.system("clear")
    elif iputContent == "帮助":
        print("命令列表:")
        print("退出: 退出MZ-OS")
        print("清屏: 清空屏幕")
        print("帮助: 显示此界面")
        print("下载: 下载指定URL里的内容\n\t语法: 下载 URL")
        print("当前目录: 输出当前的工作目录")
        print("目录内容: 输出当前工作目录里的所有内容")
    elif iputContent[:2] == "下载":
        spLst = iputContent.split()
        req = requests.get(spLst[1])
        filename = spLst[1].split('/')[-1]
        if req.status_code != 200:
            print("\033[31m错误 请检查您的网络连接或输入的网址\033[0m")
        try:
            with open(filename, "wb") as f:
                f.write(req.content)
                print("下载成功")
        except:
            print("\033[31m未知错误\033[0m")
    elif iputContent == "当前目录":
        print(os.path.abspath(os.curdir))
    elif iputContent == "目录内容":
        print(os.listdir())
    else:
        print("找不到命令“%s”" % iputContent)
        
while True:
    iput()
    oput()
