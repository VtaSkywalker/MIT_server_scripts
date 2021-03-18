# 用于删除每天临时复制过来的log，以及整合图片
import os
import re

for eachFile in os.listdir("."):
    if(re.search(".*\.log", eachFile)):
        os.remove(eachFile)
    if(re.search(".*\.jpg", eachFile)):
        os.system("move %s outputImg/%s" % (eachFile, eachFile))