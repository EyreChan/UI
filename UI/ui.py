import tkinter as tk
from tkinter import *
from tkinter import scrolledtext

window = tk.Tk()
window.title('智能写作辅助系统')
win_wid = window.winfo_screenwidth()
win_heig = window.winfo_screenheight()
window.geometry('%dx%d'%(win_wid, win_heig))
window.attributes('-topmost', True)                                 #隐藏任务栏

sys_title = Label(window, text = '智能写作辅助系统', font = ('宋体', 20, 'bold'))
sys_title.pack(side = 'top')

#title
v1 = StringVar()
title_l = Label(window, text = '标题：', font = ('宋体', 13, 'bold')).place(x = 9, y = 40)
title_e = Entry(window, width = 60, textvariable = v1, font = ('宋体', 13, 'bold')).place(x = 10, y = 60)            #使用show = 'none'会有不正常显示

#标题
v2 = StringVar()
txt_l = Label(window, text = '正文：', font = ('宋体', 13, 'bold')).place(x = 9, y = 84)
#放弃使用scrolledtext因为无法直接获取文本
txt_t = scrolledtext.ScrolledText(window, width = 60, height = 39, font = ('宋体', 13, 'bold'))     # 滑动文本框
txt_t.pack(side = LEFT, padx = 10, pady = 72)

def title_error():
    if v1.get() != '':
        print(v1.get())

title_b = Button(window, text = '标题纠错', width = 15, height = 2, command = title_error)
title_b.pack(side = RIGHT)

def txt_error():
    txt = txt_t.get('1.0', END)
    print(txt)

txt_b = Button(window, text = '文章纠错', width = 15, height = 2, command = txt_error)
txt_b.pack(side = RIGHT)

mainloop()
