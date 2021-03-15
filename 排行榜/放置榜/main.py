from calculate import calculate
from draw import draw
import sys

# 识别文件名
LOG_FILE_NAME = sys.argv[1]
# 计算
resultList = calculate(LOG_FILE_NAME)
print(resultList)
# 绘图
draw(resultList, LOG_FILE_NAME)