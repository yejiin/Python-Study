import heapq

def solution(food_times, k):

    # 전체 음식을 먹는 시간보다 K가 크거나 같다면 -1
    if sum(food_times) <= k:
        return -1
    
    # 우선순위 큐 
    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i + 1))
    
    sum_value = 0  # 먹기 위해 사용한 시간
    previous = 0  # 직전에 다 먹은 음식 시간

    length = len(food_times)

    while sum_value + ((q[0][0] - previous) * length) <= k:
        now = heapq.heappop(q)[0]  # 음식 시간
        sum_value += (now - previous) * length 
        length -= 1
        previous = now
    
    # 남은 음식 중에서 몇 번째 음식인지 확인하여 출력
    result = sorted(q, key = lambda x: x[1])
    return result[(k - sum_value) % length][1]