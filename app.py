from tkinter import *
from PIL import Image, ImageTk
import tkinter.messagebox
import re
import draw


def submit():

    # 获取参数
    # 关键词
    keyword = keyword_input.get()
    # 人数
    if people_num_input.get() == "":
        tkinter.messagebox.showerror("提示", "人数不得为空！")
        return
    people_num = int(people_num_input.get())
    # 起始时间
    # 用正则表达式匹配
    pattern = re.compile(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})')
    time_start = time_start_input.get()
    match = pattern.match(time_start)
    if match == None:
        tkinter.messagebox.showerror("提示", "起始时间格式不对！")
        return

    time_end = time_end_input.get()
    match = pattern.match(time_end)
    if match == None:
        tkinter.messagebox.showerror("提示", "结束时间格式不对！")
        return

    # 公布时间
    publish_time = publish_time_input.get()

    #奖品列表
    gift_list = thing_list_input.get()

    if people_num < 1 or people_num > 8:
        tkinter.messagebox.showerror("提示","人数错误！")
        return
    
    people_list = draw.init(people_num, keyword, time_start, time_end)
    
    if len(people_list) == 0:
        tkinter.messagebox.showerror("提示","没有用户满足抽奖条件！")
        return
    
    # 展示页面
    top1 = Toplevel()
    image = Image.open('mdbg.jpg')
    img = ImageTk.PhotoImage(image)
    canvas = Canvas(top1, width=image.width, height=image.height, bg='white')
    canvas.create_image(0, 0, image=img, anchor="nw")
    canvas.create_text(image.width / 2, 50, text="抽奖话题:"+keyword, font=('黑体', 20))
    canvas.create_text(image.width / 2, 100, text="获奖名单", font=('黑体', 20))
    height = 150
    for i in range(0, len(people_list)):
        canvas.create_text(image.width / 2-100, height + i * 50, text="获奖用户", font=('黑体', 15))
        canvas.create_text(image.width / 2 + 100, height + i * 50, text=people_list[i], font=('黑体', 15))

    # 结尾
    canvas.create_text(100, height + (people_num+2) * 50, text="奖品:"+gift_list, font=('黑体', 17))
    canvas.create_text(100, height + (people_num+3) * 50, text="日期:"+publish_time, font=('黑体', 17))
    canvas.create_text(image.width - 100, image.height-50, text="拖鞋旅游队", font=('黑体', 15))
    canvas.pack()
    top1.mainloop()

# 创建一个主窗口，用于容纳整个GUI程序
root = Tk()
root.geometry('720x512')
# 设置主窗口对象的标题栏
root.title("抽奖系统")
bg = PhotoImage(file="bg.png")

frm = Frame(root, bg='white')

imgLabel = Label(frm, image=bg, compound=CENTER)
imgLabel.pack()

# 添加一个Label组件
keyword_title = Label(frm, text="抽奖关键词:", font=('', 15))
keyword_title.place(x=150, y=100)
keyword_input = Entry(frm)
keyword_input.place(x=350, y=100)


# 添加一个Label组件
time_title = Label(frm, text="抽奖发言时间:", font=('', 15))
time_title.place(x=150, y=150)
time = StringVar()
time_start_title = Label(frm, text="起始:", font=('', 15))
time_start_title.place(x=350, y=150)

time_start_input = Entry(frm, width=20)
time_start_input.place(x=420, y=150)

notice_label = Label(frm, text="格式: 2018-11-17 20:00:00", font=('', 10), bg="pink")
notice_label.place(x=150, y=175)

time_end_title = Label(frm, text="截止:", font=('', 15))
time_end_title.place(x=350, y=200)

time_end_input = Entry(frm, width=20)
time_end_input.place(x=420, y=200)


# 添加一个Label组件
publish_time_title = Label(frm, text="抽奖公布时间:", font=('', 15))
publish_time_title.place(x=150, y=250)
publish_time_input = Entry(frm)
publish_time_input.place(x=350, y=250)

# 添加一个Label组件
people_num_title = Label(frm, text="获奖人数(1-9):", font=('', 15))
people_num_title.place(x=150, y=300)
people_num_input = Entry(frm)
people_num_input.place(x=350, y=300)


# 添加一个Label组件
thing_list_title = Label(frm, text="奖品列表:", font=('', 15))
thing_list_title.place(x=150, y=350)
thing_list_input = Entry(frm)
thing_list_input.place(x=350, y=350)


# 提交抽奖
button = Button(frm, text="抽奖", font=('', 15), command=submit)
button.place(x=350, y=400)
frm.pack(side=TOP)




def main():

    mainloop()

if __name__ == "__main__":
    main()
