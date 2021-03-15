import os
import os.path

logPath = "./logs"
fileList = os.listdir(logPath)
# 下述方法来自于https://www.cnblogs.com/xiao-erge112700/p/11276304.html
fileList = sorted(fileList, key=lambda x : os.path.getmtime(os.path.join(logPath, x)))
print(fileList[-2]) # 获取最近一天的
file = open("temp.bat", "w")
file.write("python main.py %s\ncmd /k" % fileList[-2])
file.close()
os.system("temp.bat")