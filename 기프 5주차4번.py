import random

##2019038073신승용##
def num(strdata):

    numstr = ""

    for ch in strdata:

        if ch.isdigit():

            numstr+= ch

    return int(numstr)
##2019038073신승용##
data = []

i,k = 0,0

for i in range(0,10):

    tmp = hex(random.randrange(0,10000))

    tmp = tmp[2:]

    data.append(tmp)
##2019038073신승용##
 

print("정렬 전 데이터:",end = '')

[print(num,end='')for num in data]

 

##2019038073신승용## 

for i in range(0,len(data)-1):

    for k in range(i+1,len(data)):

        if num(data[i])>num(data[k]):

            tmp = data[i]

            data[i] = data[k]

            data[k] = tmp

##2019038073신승용## 

print("\n정렬 후 데이터: ", end = "")

[print(num, end= ' ')for num in data]
