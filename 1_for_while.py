print("test")
print("100,200")
print(100,200)
print("100","200")
a=0
b=10
print(a)
print(a,b)

a=int(input())
b=int(input())
res=a+b
print(a,"+",b,"=",a+b)
print(a,"/",b,"=",int(a/b))
print(a,"-",b,"=",a-b)
print(a,"*",b,"=",a*b)
print("%d"%res)

a=int(input())
ch=input()
b=int(input())
if(ch=="+"):
    print(a,"+",b,"=",a+b)
elif(ch=="-"):
    print(a,"-",b,"=",a-b)
elif(ch=="*"):
    print(a,"*",b,"=",a*b)
elif(ch=="/"):
    print(a,"/",b,"=",a/b)
else:
    print("wrong")


if(a>10):
    if(a>5):
        print("hi")

a=int(input("시작값: "))
b=int(input("횟수(+1) 조건식(a<b): "))
c=int(input("증가값: "))
d=0
for i in range(a, b, c):
    d=d+a
print(d)

#구구단

i, num=0,0
num=int(input("무슨 단?: "))
for i in range(1, 10, 1):
    print("%d X %d = %d" % (num, i, num*i))

#트리만들기
i,j=0,0
num=int(input("값 입력: "))
for j in range(1, num+1, 1):
    for i in range(0, j, 1):
        print('*',end='')
    print()        

#역 트리만들기
i,j, k=0,0,0
num=int(input("값 입력: "))
for j in range(1, num+1, 1):
    for i in range(num-j, 0, -1):
        print(end=' ')
    for k in range(0, j, 1):
        print('*',end='')
    print()

#while 계산기
ch=""
a,b,c,d=0,0,0,0
while True:
    a=int(input("첫 번째 수 : "))
    b=int(input("두 번째 수 : "))
    ch=input("연산자: ")
    print("%d %s %d = " % (a,ch, b), end="")
    if(ch=='+'):
        print("%d" % (a+b))
    elif(ch=='-'):
        print("%d" % (a-b))
    elif(ch=='*'):
        print("%d" % (a*b))
    elif(ch=='/'):
        print("%d" % (a/b))
    elif(ch=='//'):
        print("%d" % (a//b))
    elif(ch=='**'):
        print("%d" % (a**b))
    else:
        print("연산자가 틀렸습니다")


#while 트리만들기
i,j=0,0
num=int(input("값 입력: "))
while j<num:
    j=j+1
    i=0
    while j>i:
        print('*',end='')
        i=i+1
    print()        

#while 역 트리만들기
i,j, k=0,0,0
num=int(input("값 입력: "))
while j<num:
    i=1
    while num-j>i:
        print(end=' ')
        i=i+1
    j=j+1
    i=0
    while j>i:
        print('*',end='')
        i=i+1
    print()

#트리 만들기
i,j, k=0,0,0
num=int(input("값 입력: "))
while j<num:
    i=1
    while num-j>i:
        print(end=' ')
        i=i+1
    j=j+1
    i=0
    while 2*j-1>i:
        print('*',end='')
        i=i+1
    print()

#거꾸로 트리 만들기
i,j, k=0,0,0
num=int(input("값 입력: "))
j=num-1
while j>1:
    i=0
    while num-j+1>i:
        print(end=' ')
        i=i+1
    j=j-1
    i=0
    while 2*j-1>i:
        print('*',end='')
        i=i+1
    print()

