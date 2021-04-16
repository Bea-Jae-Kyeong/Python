#https://programmers.co.kr/learn/courses/30/lessons/42748
#코딩테스트 K번째 수
def solution(array, commands):
    answer = []
    aa=[]
    for i in range(0, len(commands)):
        aa=[]
        for k in range(commands[i][0]-1, commands[i][1]):
            aa.insert(k-commands[i][0],array[k])
        aa.sort()
        answer.append(aa[commands[i][2]-1])
        del(aa)
    return answer
