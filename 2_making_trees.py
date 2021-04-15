
#while 트리만들기 1-1
i,j=0,0
num=int(input("값 입력: "))
while j<num:
    j=j+1
    i=0
    while j>i:
        print('*',end='')
        i=i+1
    print()        

print()


#while 역 트리만들기 1-2
i,j, k=0,0,0
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
print()


#대칭 트리 2-1
for j in range(num, 0, -1):
    for k in range(j, 0, -1):
        print('*',end='')
    print()
print()

#대칭 역 트리 2-2
for j in range(0, num, 1):
    for i in range(0, j, 1):
        print(end=' ')
    for k in range(num-j, 0, -1):
        print('*',end='')
    print()
print()

#대칭 트리1 1-3
for j in range(0, num*2, 1):
    if(j>num):
        for i in range(num*2-j, 0, -1):
            print('*',end='')
    else:
        for k in range(0, j, 1):
            print('*',end='')
    print()
print()

#대칭 트리2 2-3
for j in range(0, num*2, 1):
    if(j>num):
        for i in range(0, j-num, 1):
            print(end=' ')
        for i in range(num*2-j, 0, -1):
            print('*',end='')
    else:
        for i in range(num-j, 0, -1):
            print(end=' ')
        for k in range(0, j, 1):
            print('*',end='')
    print()
print()

#트리 만들기 1-4
i,j, k=0,0,0
while j<num/2:
    i=1
    while num/2-j>i:
        print(end=' ')
        i=i+1
    j=j+1
    i=0
    while 2*j-1>i:
        print('*',end='')
        i=i+1
    print()
print()

#거꾸로 트리 만들기 2-4
n=0
if(num%2==0):
    n=num-1
else:
    n=num
for i in range(0, (int)(n/2)+1, 1):
    for k in range(0,i, 1):
         print(end=' ')
    for j in range(n-i*2,0, -1):
         print('*',end='')
    print()
print()


#1-5
for i in range(0, num, 1):
    if i<num/2:
        for k in range((int)(num/2)-i,0, -1):
            print(end=' ')
        for j in range(0,i*2+1,1):
            print('*',end='')
    elif i>num/2:
        for k in range(0,i-(int)(num/2+1)+1, 1):
            print(end=' ')
        for j in range((num-i)*2-1,0, -1):
            print('*',end='')
    print()
print()



#2-5 ing
for i in range(0, num, 1):
    if i<num/2:
        
        for j in range(0,i*2+1,1):
            print('*',end='')
        for k in range((int)(num/2)-i,0, -1):
            print(end=' ')
    elif i>num/2:
        for j in range((num-i)*2-1,0, -1):
            print('*',end='')
        for k in range(0,i-(int)(num/2+1)+1, 1):
            print(end=' ')
    print()
print()
