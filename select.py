# -*- coding: UTF-8 -*-
import  jieba
from jieba.analyse import  *
f =open("record.txt", "r+", encoding="utf-8")
result = open("result.txt","w",encoding="utf-8")
for yy in f.readlines():
  if yy[0:4] == "2018":
    temp = yy[:11]+yy[19:]
    result.write(temp)
f.close()
result.close()
#test = open("result.txt","r+",encoding="utf-8")
#for xx in test.readlines():
 # print(xx)

#test.close()
with open("result.txt", "r", encoding="utf-8") as f:
 lines = f.readlines()
 #print(lines)
with open("result.txt","w",encoding="utf-8") as f_w:
   for line in lines:
     if "系统消息" in line:
      continue
     elif "80000000" in line:
       continue
     else:
        f_w.write(line)
test = open("result.txt","r+",encoding="utf-8")
for xx in test.readlines():
   print(xx)