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
    
    def setImage(self):
        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardData(win32con.CF_DIB, self.msg)
        win32clipboard.CloseClipboard()
        
    def sendmsg(self):
        self.setText()
        hwndQQ = win32gui.FindWindow(None,self.friendName)
        if hwndQQ == 0:
            print('未找到qq对话框')
            return
        win32gui.SendMessage(hwndQQ, win32con.WM_PASTE, 0, 0)
        win32gui.SendMessage(hwndQQ, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
        
    def sendimg(self):
        self.setImage()
        hwndQQ = win32gui.FindWindow(None,self.friendName)
        if hwndQQ == 0:
            print('未找到qq对话框')
            return
        win32gui.SendMessage(hwndQQ, win32con.WM_PASTE, 0, 0)
        win32gui.SendMessage(hwndQQ, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)


img = Image.open('C:\\Users\\Dell\\Desktop\\1573372688.png')
output = BytesIO()
img.convert("RGB").save(output, "BMP")
data = output.getvalue()[14:]
output.close()
if __name__ == '__main__':
    friendName = '蔡三圈'
    qq = CSendQQMsg(friendName,data)
    qq.sendimg()
    print("输出图片成功")


    time.sleep(1)
    msg = '测试消息'
    friendName = '蔡三圈'
    qq = CSendQQMsg(friendName,msg)
    qq.sendmsg()
    print("输出文字成功")