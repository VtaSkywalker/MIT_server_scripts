import cv2
# from constants import LOG_FILE_NAME
import os

OUTPUT_FILE_NAME = ""

def mergeTitle(img, title): # 把标题叠加到背景图上
    heightOfTitle = len(title)
    widthOfTitle = len(title[0])
    for rowIdx in range(heightOfTitle):
        for columnIdx in range(widthOfTitle):
            if(title[rowIdx][columnIdx][3] != 0):
                img[rowIdx][columnIdx] = title[rowIdx][columnIdx]
    return img

def mergePanel(img, panel, stRow): # 把排行面板叠加到背景图上
    heightOfPanel = len(panel)
    widthOfPanel = len(panel[0])
    edRow = stRow + heightOfPanel
    for rowIdx in range(stRow, edRow):
        for columnIdx in range(widthOfPanel):
            if(panel[rowIdx - stRow][columnIdx][3] != 0):
                img[rowIdx][columnIdx] = panel[rowIdx - stRow][columnIdx]
    return img

def fixPlayerInfo(img, gameID, value, stRow): # 填写玩家信息
    cv2.putText(img, gameID, (12, stRow + 27), cv2.FONT_HERSHEY_COMPLEX, 0.4, (0xFF, 0xFF, 0xFF), 1) # 玩家id
    value = "%06s" % value
    cv2.putText(img, value, (120, stRow + 32), cv2.FONT_HERSHEY_COMPLEX, 0.6, (0xFF, 0x0, 0x0), 1) # 放置数
    return img

def fixDateInfo(img, LOG_FILE_NAME): # 填写日期信息
    global OUTPUT_FILE_NAME
    dateOnly = LOG_FILE_NAME.split(".")[0] # 仅包含日期的部分
    yyyy = dateOnly.split("_")[0]
    mm = dateOnly.split("_")[1]
    dd = dateOnly.split("_")[2]
    cv2.putText(img, "%04d-%02d-%02d" % (int(yyyy), int(mm), int(dd)), (35, 100), cv2.FONT_HERSHEY_COMPLEX, 0.6, (0x0, 0xFF, 0x0), 1) # 日期
    OUTPUT_FILE_NAME = "%04d年%02d月%02d日_放置榜.jpg" % (int(yyyy), int(mm), int(dd))
    return img

def initUI(resultList, LOG_FILE_NAME): # 初始化图形
    img = cv2.imread("img_source/bgimg.png", cv2.IMREAD_UNCHANGED) # 加载背景图
    title = cv2.imread("img_source/title.png", cv2.IMREAD_UNCHANGED) # 加载标题图
    panel = cv2.imread("img_source/panel.png", cv2.IMREAD_UNCHANGED) # 加载排行面板图
    # 加上标题
    img = mergeTitle(img, title)
    # 加上日期
    img = fixDateInfo(img, LOG_FILE_NAME)
    # 排名相关绘制
    idx = 0
    numOfPlayer = len(resultList)
    for eachStRow in range(100, 600, 50):
        if(idx >= numOfPlayer):
            break
        img = mergePanel(img, panel, eachStRow) # 绘制排行面板
        gameID = resultList[idx][0]
        value = resultList[idx][1]
        img = fixPlayerInfo(img, gameID, value, eachStRow)
        idx += 1
    return img

def draw(resultList, LOG_FILE_NAME):
    global OUTPUT_FILE_NAME
    img = initUI(resultList, LOG_FILE_NAME)
    cv2.imshow("graph", img)
    # cv2.waitKey()
    cv2.imwrite("temp.jpg", img)
    os.rename("temp.jpg", OUTPUT_FILE_NAME) # 改名
    return OUTPUT_FILE_NAME