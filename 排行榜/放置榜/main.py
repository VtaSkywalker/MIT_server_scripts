import re

placeDic = {}

def playerPlaceUpdate(playerID): # 更新存储玩家放置信息的字典
    global placeDic
    if(playerID not in placeDic):
        placeDic[playerID] = 1
    else:
        placeDic[playerID] += 1
    return

def printResult(): # 打印排行榜
    global placeDic
    rankList = list(placeDic.items())
    # 按放置数排序
    def scoreEle(ele):
        return ele[1]
    rankList.sort(key = scoreEle)
    rankList.reverse()
    rank = 1
    for eachEle in rankList:
        print("=" * 10)
        print("排名：%d" % rank)
        print("id：%s" % eachEle[0])
        print("放置数：%d" % eachEle[1])
        rank += 1
    print("=" * 10)

file = open("2021_3_14.log", "r")
for eachLine in file:
    matchRes = re.search("玩家.*放置", eachLine) # 匹配放置子句
    if(matchRes): # 匹配成功
        pos = matchRes.span()
    else:
        continue
    placeSubSen = eachLine[pos[0]:pos[1]] # 放置子句
    playerID = placeSubSen.split(" ")[1]
    playerPlaceUpdate(playerID)
printResult()