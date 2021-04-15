a=[]
nn=0
total=0
for i in range (0, 4, 1):
    nn=int(input("값을 입력하세요 : "))
    a.append(nn)
for i in range (0, 4, 1):
    total+=a[i]
print(total)

aa=[10,20,30,40]
aa[0:3]
aa[:2]
aa[1:2]
aa*3

#LIFO 자동차 구현
parking=[]
top=0
carName='A'
outCar=''
select=0
while(select!=3):
    select=int(input("<1> 자동차 넣기 <2> 자동차 빼기 <3> 종료 : "))
    if (select==1):
        if(top>=5):
            input("더이상 들어갈 수 없습니다.")
        else:
            parking.append(carName)
            print("현 주차장 상태: %s 가 맨 앞에. 전체 %s"%(parking[top], parking))
            top+=1
            carName=chr(ord(carName)+1)
    elif (select==2):
        if(top==0):
            print("뺄 차가 없습니다.")
        else:
            outCar=parking.pop()
            print("%s 나감. 전체 %s" % (outCar, parking))
            top-=1
            carName=chr(ord(carName)-1)
    elif (select==3):
        break
    else:
        print("다시 입력하세요")

print("현 주차장 상태 : %s, %d 대가 있음" % (parking, top))
