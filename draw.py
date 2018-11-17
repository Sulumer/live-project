# coding=UTF-8
import random
'''
from baike_spider import url_manager, html_downloader, html_parser,html_outputer

'''
def draw(total,number):  # 初始化
    i = 1
    randNum = 0
    while i <= number:
        randNum = rand(total)
        #print(randNum)
        flag = check(randNum)  #判断用户是否被过滤、是否已获奖
        #print("flag: %d", flag)
        if flag is 1:
            #print("len1: %d", len(Winner))
            Winner.append(randNum)
            #print("len2: %d", len(Winner))
        i = i + 1
    i = 1
    while i <= len(Winner) :
        print(Winner[i-1])
        i = i + 1
    
def __init__():  # 初始化
    random()
        
    
def rand(total):
    return random.randint(1,total)

def check(num):
    if num not in lists:
        return 2
    '''
    if Winner.index(num) != -1:
        return 3
        '''
    return 1
    
if __name__ == '__main__':
    
    listFile = 'record.txt'
    lists = [1,2,3,4,5,6,7,8,9,10]
    Winner = []
    total = 10
    first = 1
    draw(total,first)