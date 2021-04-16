#https://programmers.co.kr/learn/courses/30/lessons/42748
#코딩테스트 K번째 수
def solution(array, commands):
    answer = []
    for i in range(0, len(commands)):
        aa=[]
        for k in range(commands[i][0]-1, commands[i][1]):
            aa.insert(k-commands[i][0],array[k])
        aa.sort()
        answer.append(aa[commands[i][2]-1])
        del(aa)
    return answer


#lambda는 함수 선언 대신 사용, map은 list 속 값을 commands로 매핑해줌
def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))
