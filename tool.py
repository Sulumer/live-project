# -*- coding: UTF-8 -*-

import random
random.random()
person = {}
#将得到的名字进行提取他们的qq号或者邮箱
def check(name):
    ln=len(name)
    #print("=======")
    fg=0
    resid=""
    for i in range(ln-2,-1,-1):
        if(fg==0 and name[i]==')'):
            fg=1
            continue
        if(fg==1 and name[i]!='('):
            resid=resid+name[i]
        if(fg==1 and name[i]=='('):
            fg=2
            break
    if fg==2:
        return resid[::-1]
    fg = 0
    resid = ""
    for i in range(ln - 2, -1, -1):
        if (fg == 0 and name[i] == '>'):
            fg = 1
            continue
        if (fg == 1 and name[i] != '<'):
            resid = resid + name[i]
        if (fg == 1 and name[i] == '<'):
            fg = 2
            break
    if fg==2:
        return resid[::-1]
    return "#"


#根据聊天程度判断每个人的权重
#根据num筛选掉小于num的名单
def workforperson(num):
    
    list=[]
    with open('record.txt', encoding='utf-8') as f:
        line =0
        for yy in f.readlines():
            if("系统消息"in yy):
                continue
            if (len(yy) >= 23):
                idd = check(yy)
                if (idd != "#" and yy[4] == '-' and yy[7] == '-' and yy[13] == ':' and yy[16] == ':'):
#                     print(idd)
                    if(idd in person.keys()):
                        val=person.get(idd)
                        val+=1
                        person[idd]=val
                    else:
                        val=0
                        person[idd]=1
    f.close()
    for key in person.keys():
        if person[key]>=num:
            list.append(key)
    return list


#判断是否符合抽奖时间
# start_time 抽奖开始时间
# dealine 截止时间
# now_time 当前时间
# return 0 表示 不符合 ， 1 表示符合
def checktime(start_time, deadline , now_time):
    indx=0
    for t in now_time:
        if(t=='-' or t==':'):
            indx+=1
            continue
        if(t==start_time[indx] and t==deadline[indx]):
            indx+=1
            continue
        if(t>=start_time[indx] and t<deadline[indx]):
            return 1
        if(t<start_time[indx] or t>deadline[indx]):
            return 0
        if (t > start_time[indx] and t < deadline[indx]):
            return 1
    return 0

#计算抽奖的math值
def workformath(num):
    workforperson(num)
    totalval=0
    T_value=0
    KeyCount = len(person)
    p_values=0
    maths={}
    for key in person.keys():
        totalval+=person[key]
    cnt=0
    Random = random.random()
#     print(Random)
    for key in person.keys():
        T_value=person[key]/totalval
        p_values=T_value*(KeyCount*0.02)
        maths[key]=Random*(1-p_values)
        cnt+=1
#     print(maths)
    maths = sorted(maths.items(),key = lambda item:item[1])
#     print(maths)
    list = []
    for i in maths:
        list.append(i[0])
#         print(i[0])
#         print(i[1])
#     print(list)
    return list

#分一二三等奖的名单-qq号
def prizes1():
    prize1=[]
    prize2=[]
    prize3=[]
    maths=workformath()
    for key in maths.keys():
        if maths[key]<=0.1:
            print(maths[key])
            prize1.append(key)
            print(key)
        if maths[key]<= 0.3 and maths[key]>0.1:
            prize2.append(key)
        if maths[key]<= 0.6 and maths[key]>0.3:
            prize3.append(key)

# list=workforperson(1)
# print(list)