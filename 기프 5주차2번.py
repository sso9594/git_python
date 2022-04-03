import operator

 

string='원문\n 내가 그의 이름을 불러주기 전에는 그는 다만 하나의 몸짓에 지나지 \
않았다.\n내가 그의 이름을 불러주었을 때, 그는 내게로 와 꽃이 되었다.\n내가 그의 \
이름을 불러준 것처럼 나의 이 빛깔과 향기에 알맞는 누가 나의 이름을 불러다오.\n\
그에게로 가서 나도 그의 꽃이 되고 싶다.\n우리들은 모두 무엇이 되고 싶다.\n\
나는 너에게 너는 나에게 잊혀지지 않는 하나의 눈짓이 되고 싶다.\n'

##2019038073신승용##
strdic={}

strlist=[]
##2019038073신승용##

if __name__=="__main__":
    
    print(string)

    print('--------------------------\n')

    print('문자\t빈도수\n')

    print('--------------------------\n')
##2019038073신승용##
 

    for ch in string:
        if "ㄱ"<=ch and ch <="힣":

            if ch in strdic:
                strdic[ch]+=1

            else:
                strdic[ch]=1
    strlist = sorted(strdic.items(),key=operator.itemgetter(1),reverse=True)


    for i in range(0,len(strlist)):
        print(strlist[i][0],'\t',strlist[i][1])
        
##2019038073신승용## 
