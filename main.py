# 鼠标操作
import win32api
import win32gui
import win32con

'''通过spy++拿到应用程序主窗口的类名和窗口标题'''
mainHnd = win32gui.FindWindow("窗口类名", "窗口标题（全）")

'''根据GetWindowRect拿到主窗口的左顶点的位置坐标(x,y)和窗口的宽高(w*h)'''
rect = win32gui.GetWindowRect(mainHnd)
x, y = rect[0], rect[1]
w, h = rect[2] - x, rect[3] - y
# 模拟鼠标指针， 传送到指定坐标
long_position = win32api.MAKELONG(x, y)

# 模拟鼠标按下
win32api.SendMessage(hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, long_position)

# 模拟鼠标弹起
win32api.SendMessage(hwnd, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, long_position)
