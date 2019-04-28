import tkinter as tk
from tkinter import *
from tkinter import scrolledtext

import json
with open("recommend.json", "r", encoding='utf-8') as f:
    Rec_dic = json.load(f)

# 文本错误
def t_error():
    title = v1.get()
    if title:
        te_t.delete('1.0', END)
        te_t.insert(END, title + '\n')
    txt = txt_t.get('1.0', END)
    if txt and title:
        te_t.insert(END, txt)
    elif txt:
        te_t.delete('1.0', END)
        te_t.insert(END, txt)

#词语（搭配或替换）推荐
def wordColloc():
    v = v2.get()
    if v in Rec_dic:
        v3.set(Rec_dic[v])
    else:
        v3.set("error")

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
sys_title = Label(window, text = '智能写作辅助系统', font = ('宋体', 18, 'bold'))
sys_title.pack(side = 'top')

#输入标题
v1 = StringVar()
title_l = Label(window, text = '标题：', font = ('宋体', 12, 'bold')).place(x = int(win_wid / 160), y = int(win_heig / 16))
title_e = Entry(window, width = int(win_wid / 22), textvariable = v1, font = ('宋体', 12, 'bold')).place(x = int(win_wid / 140), y = int(win_heig / 11))            #使用show = 'none'会有不正常显示

#输入文本框
txt_l = Label(window, text = '正文：', font = ('宋体', 12, 'bold')).place(x = int(win_wid / 200), y = int(win_heig / 8))
txt_t = scrolledtext.ScrolledText(window, width = int(win_wid / 22), height = int(win_heig / 42), font = ('宋体', 12, 'bold'))                           #滚动文本框
txt_t.place(x = int(win_wid / 200), y = int(win_heig * 5 / 32), anchor = NW)

#文本纠错文本框
te_l = Label(window, text = '文本纠错：', font = ('宋体', 12, 'bold')).place(x = int(win_wid / 200), y = int(win_heig / 20 * 11))
te_t = scrolledtext.ScrolledText(window, width = int(win_wid / 22), height = int(win_heig / 50), font = ('宋体', 12, 'bold'))
te_t.place(x = int(win_wid / 200), y = int(win_heig / 12 * 7))

#词语推荐文本框
v2 = StringVar()
v3 = StringVar()
word_l1 = Label(window, text = '词语输入：', font = ('宋体', 12, 'bold')).place(x = int(win_wid / 30 * 14), y = int(win_heig / 8))
word_e1 = Entry(window, width = int(win_wid / 188), textvariable = v2, font = ('宋体', 12, 'bold')).place(x = int(win_wid / 30 * 16), y = int(win_heig / 8))
word_l2 = Label(window, text = '词语推荐：', font = ('宋体', 12, 'bold')).place(x = int(win_wid / 30 * 18), y = int(win_heig / 8))
word_e2 = Entry(window, width = int(win_wid / 35), textvariable = v3, font = ('宋体', 12, 'bold')).place(x = int(win_wid / 3 * 2), y = int(win_heig / 8))

#例句推荐文本框
sr_l = Label(window, text = '例句推荐：', font = ('宋体', 12, 'bold')).place(x = int(win_wid / 30 * 14), y = int(win_heig * 11 / 60))
sr_t = scrolledtext.ScrolledText(window, width = int(win_wid / 20), height = int(win_heig / 50), font = ('宋体', 12, 'bold')).place(x = int(win_wid / 30 * 14), y = int(win_heig * 13 / 60))

#主题推荐文本框
tr_l = Label(window, text = '主题推荐：', font = ('宋体', 12, 'bold')).place(x = int(win_wid / 30 * 14), y = int(win_heig / 20 * 11))
tr_t = scrolledtext.ScrolledText(window, width = int(win_wid / 20), height = int(win_heig / 50), font = ('宋体', 12, 'bold'))
tr_t.place(x = int(win_wid / 30 * 14), y = int(win_heig / 12 * 7))

#文本纠错按钮
t_b = Button(window, text = '文本纠错', width = int(win_wid / 120), height = int(win_heig / 500), command = t_error).place(x = int(win_wid / 2), y = int(win_heig / 14))
#词语推荐按钮
wr_b = Button(window, text = '词语推荐', width = int(win_wid / 120), height = int(win_heig / 500), command = wordColloc).place(x = int(win_wid / 8 * 5), y = int(win_heig / 14))
#例句推荐按钮
sr_b = Button(window, text = '例句推荐', width = int(win_wid / 120), height = int(win_heig / 500), command = t_error).place(x = int(win_wid / 8 * 6), y = int(win_heig / 14))
#主题推荐按钮
tr_b = Button(window, text = '主题推荐', width = int(win_wid / 120), height = int(win_heig / 500), command = t_error).place(x = int(win_wid / 8 * 7), y = int(win_heig / 14))

mainloop()
