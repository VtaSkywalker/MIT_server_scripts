from calculate import calculate
from draw import draw
import sys
from qqrobot import send

# 识别文件名
LOG_FILE_NAME = sys.argv[1]
# 计算
[resultList, msg] = calculate(LOG_FILE_NAME)
# 绘图
imgPath = draw(resultList, LOG_FILE_NAME)
# 机器人发送信息
send(msg, imgPath)