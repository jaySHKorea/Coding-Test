'''
    SJF(shortest job first) 알고리즘

    현재 수행 가능한 업무 중 소요 시간이 가장 짧은 업무부터 처리한다.
'''
import heapq

def solution(jobs):
    answer = 0
    now,avg,cnt,j_idx = 0,0,0,-1
    start = -1
    heap = []

    # 요청 시점으로 정렬
    jobs = sorted(jobs, key=lambda x : x[0])
    
    while cnt < len(jobs):
        s = j_idx +1 # 다음 처리할 작업 idx

        # 마지막 작업 종료시점 ~ 현재 시간 사이의 요청들을 heap으로
        for i in range(s,len(jobs)):
            if start < jobs[i][0] <= now:
                heapq.heappush(heap,(jobs[i][1],jobs[i][0]))
                j_idx = i
        # 처리할 작업이 있을 때
        if len(heap) > 0:
            job = heapq.heappop(heap)
            start = now
            now += job[0]
            avg += now-job[1]
            cnt += 1
        # 없을 때 : 처리해야할 가장 최근 작업으로
        else:
            now = jobs[j_idx+1][0] 
    answer = int(avg/len(jobs))
    return answer

print(solution([[0,3],[1,9],[2,6]]))