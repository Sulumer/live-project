def workforperson():
    person = {}
    with open('record.txt', encoding='utf-8') as f:
        #line = 0
        for yy in f.readlines():
            name = yy[20:]
            if(name[0:4]==" 系统消息"  or len(name)==0):
                print("yes")
            if len(name)>1:
                if(name[-2]==')'or name[-2]=='>'):
                    print(name)
                    if(name in person.keys()):
                        val=person.get(name)
                        val+=1
                        person[name]=val
                    else:
                        val=0
                        person[name]=1
                    val=person.get(name)
                    print(val)
    return person

if __name__ == '__main__':
    workforperson()