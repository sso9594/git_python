import random
##2019038073 신승용##
roof=0
con=0
dice=list(range(6))
##2019038073 신승용##
while True:
    roof+=1
    
    for i in range(0,6):
        dice[i]=random.randint(1,6)
    if (dice[0]==1 or dice[1]==1 or dice[2]==1 or dice[3]==1 or dice[4]==1 or dice[5]==1)and\
       (dice[0]==2 or dice[1]==2 or dice[2]==2 or dice[3]==2 or dice[4]==2 or dice[5]==2) and \
       (dice[0]==3 or dice[1]==3 or dice[2]==3 or dice[3]==3 or dice[4]==3 or dice[5]==3) and\
       (dice[0]==4 or dice[1]==4 or dice[2]==4 or dice[3]==4 or dice[4]==4 or dice[5]==4) and \
       (dice[0]==5 or dice[1]==5 or dice[2]==5 or dice[3]==5 or dice[4]==5 or dice[5]==5) and \
       (dice[0]==6 or dice[1]==6 or dice[2]==6 or dice[3]==6 or dice[4]==6 or dice[5]==6):
        con+=1
    elif dice[0]==dice[1]==dice[2]==dice[3]==dice[4]==dice[5]:
        print(dice[0])
        break
print('6개 주사위가 모두 동일한 숫자가 나옴 --> ',dice[0],dice[1],dice[2],dice[3],dice[4],dice[5])
print('6개가 동일한 숫자가 나올 때까지 주사위를 던진 횟수 --> ',roof)
print('6개가 동일한 숫자가 나올 때까지 1~6의 연속번호가 나온 횟수 --> ',con)
