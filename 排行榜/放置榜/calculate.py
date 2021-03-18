import re
# from constants import *

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
def calculate(LOG_FILE_NAME):
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
    msg = convert2Msg(resultList, LOG_FILE_NAME)
    return [resultList, msg]

# 将结果以文字形式呈现
def convert2Msg(resultList, LOG_FILE_NAME):
    dateOnly = LOG_FILE_NAME.split(".")[0] # 仅包含日期的部分
    yyyy = dateOnly.split("_")[0]
    mm = dateOnly.split("_")[1]
    dd = dateOnly.split("_")[2]
    msg = ""
    msg += "%04d年%02d月%02d日——挖掘榜：\n" % (int(yyyy), int(mm), int(dd))
    rank = 1
    for eachEle in resultList:
        msg += "=" * 10
        msg += "\n"
        msg += "排名：%d\n" % rank
        msg += "id：%s\n" % eachEle[0]
        msg += "放置数：%d\n" % eachEle[1]
        rank += 1
    msg += "=" * 10
    msg += "\n"
    return msg