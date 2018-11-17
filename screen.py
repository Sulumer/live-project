
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


def selectperson(keyword,start_time,deadline):
    list=[]
    with open("record.txt", "r", encoding="utf-8") as f:
        fg=0
        for yy in f.readlines():
            if(len(yy)>=23 and fg==0):
                idd=check(yy)
                if(idd!="#" and yy[4]=='-' and yy[7]=='-' and yy[13]==':' and yy[16]==':'):
                    name=yy
                    fg=1
            if(fg==1 and keyword in yy and checktime(start_time,deadline,name[:19])):
                if(idd not in list and idd!="80000000" and idd!="1000000" and idd!="10000"):
                    list.append(idd)
                fg=0
    return list


# def keyWords(key):
#     flag = 0
#     with open("record.txt", "r", encoding="utf-8") as f:
#         lines = f.readlines()
#        # print(lines)
#     with open("result.txt", "w", encoding="utf-8") as f_w:
#         for line in lines:
#             if flag == 0:
#                 temp = line
#                 flag = 1
#             if key in line:
#                 f_w.write(temp)
#                 temp ="\0"
#                 flag = 0
#     return

# keyWords("#我要换组#")
# test = open("result.txt","r+",encoding="utf-8")
# for xx in test.readlines():
#    print(xx)


person=selectperson("#我要换组#","2018-08-20 00:00:00","2018-12-30 00:00:00")

for name in person:
    print(name)