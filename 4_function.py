#랜덤 로또 숫자 추출 프로그램
import random
def lotto():
    a=[]
    for i in range(0,6):
        a.insert(i,random.randrange(1,45))
    print((str)(sorted(a)).replace("[",""), end=' ')
    del(a)
lotto()
