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
art_t_l = Label(window, text = '标题：', font = ('宋体', 13, 'bold')).place(x = 10, y = 50)
art_t_e = Entry(window, width = 50, font = ('宋体', 13, 'bold')).place(x = 10, y = 70)            #使用show = 'none'会有不正常显示

#content
art_c_l = Label(window, text = '正文：', font = ('宋体', 13, 'bold')).place(x = 10, y = 100)
art_c_t = scrolledtext.ScrolledText(window, font = ('宋体', 13, 'bold'), width = 50, height = 35).place(x = 10, y = 120)      # 滑动文本框

mainloop()
