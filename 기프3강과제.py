import random
if __name__ == "__main__" :
##2019038073 신승용##
    roof=0
    con=0
    dice=list(range(6))
##2019038073 신승용##
    while True:
        roof+=1
        for i in range(0,5):
            dice[i]=random.randint(1,6)
        if dice[0]==1 and dice[1]==2 and dice[2]==3 and dice[3]==4 and dice[4]==5 and dice[5]==6:
            con=con+1
        if dice[0]==dice[1]==dice[2]==dice[3]==dice[4]==dice[5]:
            print('6개 주사위가 모두 동일한 숫자가 나옴 --> ',dice[0],dice[1],dice[2],dice[3],dice[4],dice[5])
            print('6개가 동일한 숫자가 나올 때까지 주사위를 던진 횟수 --> ',roof)
            print('6개가 동일한 숫자가 나올 때까지 1~6의 연속번호가 나온 횟수 --> ',con)
            break
##2019038073 신승용##
