import win32gui
import win32con
import win32clipboard
import time
from PIL import Image
from io import BytesIO

class CSendQQMsg():
    def __init__(self, friendName, msg):
        self.friendName = friendName
        self.msg=msg

    def setText(self):
        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardData(win32con.CF_UNICODETEXT, self.msg)
        win32clipboard.CloseClipboard()

    def sendmsg(self):
        self.setText()
        hwndQQ = win32gui.FindWindow(None,self.friendName)
        if hwndQQ == 0:
            print('未找到qq对话框')
            return
        win32gui.SendMessage(hwndQQ,win32con.WM_PASTE, 0, 0)
        win32gui.SendMessage(hwndQQ, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)

    # 图像发送
    def setImage(self):
        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardData(win32con.CF_DIB, self.msg)
        win32clipboard.CloseClipboard()

    def sendimg(self):
        self.setImage()
        hwndQQ = win32gui.FindWindow(None,self.friendName)
        if hwndQQ == 0:
            print('未找到qq对话框')
            return
        win32gui.SendMessage(hwndQQ, win32con.WM_PASTE, 0, 0)
        win32gui.SendMessage(hwndQQ, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)


def send(msg, imgPath):
    friendName = 'MIT 国际服（内服）'
    qq = CSendQQMsg(friendName, msg)
    qq.sendmsg()
    print("文字发送完成！")
    # 图片输出
    time.sleep(1)
    img = Image.open(imgPath)
    output = BytesIO()
    img.convert("RGB").save(output, "BMP")
    data = output.getvalue()[14:]
    output.close()
    qq = CSendQQMsg(friendName, data)
    qq.sendimg()
    print("图片发送完成！")

if __name__ == '__main__':
    # friendName = 'MIT 国际服（内服）'
    friendName = '啊这什么随机名字'
    t = 0
    for i in range(1,3):
        t += 1
        msg="机器人测试第%s条" % t
        qq = CSendQQMsg(friendName,msg)
        qq.sendmsg()
        time.sleep(0.3)
        print("输出第：",i,"条")