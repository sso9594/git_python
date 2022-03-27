import operator

trainlist=[('토마스',5),('헨리',8),('에드워드',9),

           ('에밀리',5),('토마스',4),('헨리',7),('토마스',3),('에밀리',8),('퍼시',5),('고든',13)]
##2019038073신승용##
 

traindic={}

train2list=[]

traintup=None

totalrank,currentrank=1,1
##2019038073신승용##
 

if __name__=="__main__":

    for traintup in trainlist:

        tName=traintup[0]

        tWeight=traintup[1]

        if tName in traindic:

            traindic[tName]+=tWeight

        else:

            traindic[tName]=tWeight

 
##2019038073신승용##
    print('기차 수송량 목록 =>', trainlist)

    print('------------------------')

    train2list=sorted(traindic.items(),key=operator.itemgetter(1),reverse=True)

 



    print('   기차\t\t총수송량 순위')

    print('------------------------')

    print(train2list[0][0].rjust(5),'\t',train2list[0][1],'\t',currentrank)

    for i in range (1,len(train2list)):

        totalrank+=1

        if train2list[i][1]==train2list[i-1][1]:

            pass

        else:

            currentrank=totalrank

        print(train2list[i][0].rjust(5),'\t',train2list[i][1],'\t',currentrank)
##2019038073신승용##
