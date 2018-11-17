from tkinter import *
import tkinter.messagebox


def submit():
    print(keyword_input.get())
    print("恭喜XXXX中奖~~")


# 创建一个主窗口，用于容纳整个GUI程序
root = Tk()
root.geometry('720x512')
# 设置主窗口对象的标题栏
root.title("抽奖系统")

frm = Frame(root)
frm_1 = Frame(frm, width=500, height=80)
frm_2 = Frame(frm, width=550, height=80)
frm_3 = Frame(frm, width=500, height=80)
frm_4 = Frame(frm, width=600, height=100)

frm_ok = Frame(frm, width=500, height=80)

# 添加一个Label组件
keyword_title = Label(frm_1, text="抽奖关键词:", font=('', 15))
keyword_title.place(x=0, y=50)
# keyword_title.pack(side=LEFT)
keyword_input = Entry(frm_1)
# keyword_input.pack(side=RIGHT)
keyword_input.place(x=200, y=50)
frm_1.pack()

# 添加一个Label组件
time_title = Label(frm_2, text="抽奖发言时间:", font=('', 15))
# time_title.pack(side=LEFT)
time_title.place(x=0, y=0)

time_start_title = Label(frm_2, text="起始:", font=('', 15))
# time_start_title.pack(side=LEFT)
time_start_title.place(x=150, y=0)

time_start_input = Entry(frm_2, width=10)
# time_start_input.pack(side=LEFT)
time_start_input.place(x=220, y=0)

time_end_title = Label(frm_2, text="截止:", font=('', 15))
# time_end_title.pack(side=LEFT)
time_end_title.place(x=300, y=0)

time_end_input = Entry(frm_2, width=10)
# time_end_input.pack(side=LEFT)
time_end_input.place(x=370, y=0)

frm_2.pack()

# 添加一个Label组件
label1_title = Label(frm_3, text="抽奖过滤规则", font=('', 25), bg="#DC143C")
label1_title.place(x=0, y=0)
frm_3.pack()

# 添加一个Label组件
publish_time_title = Label(frm_4, text="抽奖公布时间:", font=('', 15))
# publish_time_title.pack(side=LEFT)
publish_time_title.place(x=100, y=0)
publish_time_input = Entry(frm_4)
# publish_time_input.pack(side=RIGHT)
publish_time_input.place(x=300, y=0)

# 添加一个Label组件
people_num_title = Label(frm_4, text="抽奖人数:", font=('', 15))
people_num_title.place(x=100, y=30)
people_num_input = Entry(frm_4)
people_num_input.place(x=300, y=30)


# 添加一个Label组件
thing_list_title = Label(frm_4, text="奖品列表:", font=('', 15))
thing_list_title.place(x=100, y=60)
thing_list_input = Entry(frm_4)
thing_list_input.place(x=300, y=60)
frm_4.pack()

# 提交抽奖
button = Button(frm_ok, text="抽奖", font=('', 15), command=submit)
button.pack(side=TOP)
frm_ok.pack()
frm.pack(side=TOP)



def main():

    mainloop()

if __name__ == "__main__":
    main()