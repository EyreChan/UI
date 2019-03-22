import tkinter as tk
from tkinter import *
from tkinter import scrolledtext

#创建
window = tk.Tk()
window.title('智能写作辅助系统')

#获取屏幕长宽
win_wid = window.winfo_screenwidth()
win_heig = window.winfo_screenheight()

#设置成屏幕大小
window.geometry('%dx%d'%(win_wid, win_heig))

#隐藏任务栏
window.attributes('-topmost', True)

#系统标题
sys_title = Label(window, text = '智能写作辅助系统', font = ('宋体', 20, 'bold'))
sys_title.pack(side = 'top')

#输入标题
v1 = StringVar()
title_l = Label(window, text = '标题：', font = ('宋体', 13, 'bold')).place(x = int(win_wid / 200), y = int(win_heig / 16))
title_e = Entry(window, width = int(win_wid / 24), textvariable = v1, font = ('宋体', 13, 'bold')).place(x = int(win_wid / 150), y = int(win_heig / 11))            #使用show = 'none'会有不正常显示

#输入文本框
txt_l = Label(window, text = '正文：', font = ('宋体', 13, 'bold')).place(x = int(win_wid / 200), y = int(win_heig / 8))
txt_t = scrolledtext.ScrolledText(window, width = int(win_wid / 24), height = int(win_heig / 2), font = ('宋体', 13, 'bold'))                           #滚动文本框
txt_t.pack(side = LEFT, padx = int(win_wid / 150), pady = int(win_heig / 9))

#例句推荐文本框
sr_l = Label(window, text = '例句推荐：', font = ('宋体', 13, 'bold')).place(x = int(win_wid / 30 * 14), y = int(win_heig / 6))
sr_t = scrolledtext.ScrolledText(window, width = int(win_wid / 20), height = int(win_heig / 50), font = ('宋体', 13, 'bold')).place(x = int(win_wid / 30 * 14), y = int(win_heig / 5))

#主题推荐文本框
tr_l = Label(window, text = '主题推荐：', font = ('宋体', 13, 'bold')).place(x = int(win_wid / 30 * 14), y = int(win_heig / 20 * 11))
tr_t = scrolledtext.ScrolledText(window, width = int(win_wid / 20), height = int(win_heig / 50), font = ('宋体', 13, 'bold')).place(x = int(win_wid / 30 * 14), y = int(win_heig / 12 * 7))

#文本错误
def t_error():
    title = v1.get()
    if title:
        print(title)
    txt = txt_t.get('1.0', END)
    if txt:
        print(txt)

def w_recommend():



#文本纠错按钮
t_b = Button(window, text = '文本纠错', width = int(win_wid / 120), height = int(win_heig / 300), command = t_error).place(x = int(win_wid / 2), y = int(win_heig / 14))
#词语推荐按钮
wr_b = Button(window, text = '词语推荐', width = int(win_wid / 120), height = int(win_heig / 300), command = t_error).place(x = int(win_wid / 8 * 5), y = int(win_heig / 14))
#例句推荐按钮
sr_b = Button(window, text = '例句推荐', width = int(win_wid / 120), height = int(win_heig / 300), command = t_error).place(x = int(win_wid / 8 * 6), y = int(win_heig / 14))
#主题推荐按钮
tr_b = Button(window, text = '主题推荐', width = int(win_wid / 120), height = int(win_heig / 300), command = t_error).place(x = int(win_wid / 8 * 7), y = int(win_heig / 14))
mainloop()
