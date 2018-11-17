# -*- coding: UTF-8 -*-

import random
random.random()

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
def workforperson():
    person = {}
    with open('record.txt', encoding='utf-8') as f:
        line =0
        for yy in f.readlines():
            name = yy[20:]
            if("系统消息(10000)"in name):
                continue
            if len(name)>1:
                idd=check(name)
                if idd=="#":
                    continue
                else:
                    print(idd)
                    if(idd in person.keys()):
                        val=person.get(idd)
                        val+=1
                        person[idd]=val
                    else:
                        val=0
                        person[idd]=1
    return person


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
def workformath():
    person = workforperson()
    totalval=0
    T_value=0
    KeyCount = len(person)
    p_values=0
    maths={}
    for key in person.keys():
        totalval+=person[key]
    cnt=0
    Random = random.random()
    print(Random)
    for key in person.keys():
        T_value=person[key]/totalval
        p_values=T_value*(KeyCount*0.02)
        maths[key]=Random*(1-p_values)
        cnt+=1
    return maths

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

#print(checktime("2018-10-09 23:00","2018-12-30 20:00","2018-11-01 08:00"))