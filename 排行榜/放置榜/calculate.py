import re
from constants import *

placeDic = {}

def playerPlaceUpdate(playerID): # 更新存储玩家放置信息的字典
    global placeDic
    if(playerID not in placeDic):
        placeDic[playerID] = 1
    else:
        placeDic[playerID] += 1
    return

def printAndGetResult(): # 打印排行榜
    resultList = [] # 存储结果的列表
    global placeDic
    rankList = list(placeDic.items())
    # 按放置数排序
    def scoreEle(ele):
        return ele[1]
    rankList.sort(key = scoreEle)
    rankList.reverse()
    rank = 1
    for eachEle in rankList:
        tempList = []
        print("=" * 10)
        print("排名：%d" % rank)
        print("id：%s" % eachEle[0])
        tempList.append(eachEle[0])
        print("放置数：%d" % eachEle[1])
        tempList.append(eachEle[1])
        resultList.append(tempList)
        rank += 1
    print("=" * 10)
    return resultList

# 计算部分
def calculate():
    file = open(LOG_FILE_NAME, "r")
    for eachLine in file:
        matchRes = re.search("玩家.*放置", eachLine) # 匹配放置子句
        if(matchRes): # 匹配成功
            pos = matchRes.span()
        else:
            continue
        placeSubSen = eachLine[pos[0]:pos[1]] # 放置子句
        playerID = placeSubSen.split(" ")[1]
        playerPlaceUpdate(playerID)
    resultList = printAndGetResult()
    return resultList