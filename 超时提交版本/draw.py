# # coding=UTF-8
# import random
# import tool
# import screen
# from tool import person
# '''
# from baike_spider import url_manager, html_downloader, html_parser,html_outputer
#
# '''
#
# num = 50
#
# def draw2(winners,list1,list2):  #算法抽奖
#     Winner=[]
#     i = 1
#     pos = 0
#     while i <= winners:
#         if pos == len(list2):
#             break
#         person = list2[pos]
#         pos = pos + 1
#         flag = check(Winner,person,list1)  #判断用户是否被过滤、是否已获奖
#         if flag is 0:
#             Winner.append(person)
#             i = i + 1
#     return Winner
#
# def rand(total): #生成随机数
#     return random.randint(1,total)
#
#
# def check(Winner,num,list1): #判断用户是否被过滤、是否已获奖
#     num2 = list1.count(num)
#     if num2 == 0:
#         return 1
#     num2 = Winner.count(num)
#     if num2 != 0:
#         return 2
#     return 0
#
# def init(people,keyword,start_time,end_time):
#     list1 = screen.selectperson(keyword,start_time,end_time)
#     list2 = tool.workformath(num)
#     Winner=draw2(people,list1,list2)
#     return Winner
# coding=UTF-8
import random
import tool
import screen


# from tool import person

def draw(winners, list1, list2):  # 算法抽奖
    Winner = []
    i = 1
    pos = 0
    while i <= winners:
        if pos == len(list2):
            break
        person = list2[pos]
        pos = pos + 1
        flag = check(Winner, person, list1)  # 判断用户是否被过滤、是否已获奖
        if flag is 0:
            Winner.append(person)
            i = i + 1
    return Winner


def check(Winner, num, list1):  # 判断用户是否被过滤、是否已获奖
    num2 = list1.count(num)
    if num2 == 0:
        return 1
    num2 = Winner.count(num)
    if num2 != 0:
        return 2
    return 0


def init(people, keyword, start_time, end_time, num):
    list1 = screen.selectperson(keyword, start_time, end_time)
    if num == 1:
        list2 = tool.workformath(0)
    elif num == 2:
        list2 = tool.workformath(4)
    elif num == 3:
        list2 = tool.workformath(10)
    else:
        list2=[]

    Winner = draw(people, list1, list2)
    return Winner


