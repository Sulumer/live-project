# coding=UTF-8
import random
import tool
import screen
from tool import person
'''
from baike_spider import url_manager, html_downloader, html_parser,html_outputer

'''
# list1 = []
# list2 = []
num = 50
Winner = []
# def draw(total,number):  # 随机抽奖
#     i = 1
#     randNum = 0
#     while i <= number:
#         randNum = rand(total)
#         print(randNum)
#         person = list1[randNum-1]
#         flag = check(person)  #判断用户是否被过滤、是否已获奖
# #         print("flag: %d", flag)
#         if flag is 0:
# #             print("len1: %d", len(Winner))
#             Winner.append(person)
# #             print("len2: %d", len(Winner))
#         i = i + 1
#     print_winner()

def draw2(winners,list1,list2):  #算法抽奖
    
    i = 1
    pos = 0
#     print(list2)
    while i <= winners:
        if pos == len(list2):
            break
        person = list2[pos]
        pos = pos + 1
        flag = check(person,list1)  #判断用户是否被过滤、是否已获奖
#         print("flag: %d", flag)
        if flag is 0:
#             print("len1: %d", len(Winner))
            Winner.append(person)
            i = i + 1
#             print("len2: %d", len(Winner))
#     print_winner()
    
def rand(total): #生成随机数
    return random.randint(1,total)

# def print_winner():
#     i = 1
#     while i <= len(Winner) :
#         print(Winner[i-1])
#         i = i + 1
    
def check(num,list1): #判断用户是否被过滤、是否已获奖
    num2 = list1.count(num)
    if num2 == 0:
        return 1
    num2 = Winner.count(num)
    if num2 != 0:
        return 2
    return 0

def init(people,keyword,start_time,end_time):
    list1 = screen.selectperson(keyword,start_time,end_time)
#     print(list1)
#     list2 = tool.workforperson(5000)
#     print(list2)
    list2 = tool.workformath(num)
#     print(list2)
#     total = len(list1)
    draw2(people,list1,list2)
    return Winner

# print(init(4, "我要换组", "2018-08-20 00:00:00", "2018-09-10 00:00:00"))
