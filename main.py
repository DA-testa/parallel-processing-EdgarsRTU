import heapq
 
def parallel_processing(n, m, data):
    output = []
    W = [(0, i) for i in range(n)]
    heapq.heapify(W)
    for i in range(m):
        time = data[i]
        a_time, W = heapq.heappop(W)
        if output:
            b_time = max(a_time, output[-1][1])
        else:
            b_time = a_time
        a_time = b_time + time
        output.append((W, b_time))
        heapq.heappush(W, (a_time, W))
    return output
 
 
def main():
    n, m = map(int, input().split())
    data = list(map(int, input().split()))
 
    result = parallel_processing(n, m, data)
 
    for W, b_time in result:
        print(W, b_time)
 
 
if __name__ == "__main__":
    main()
#Edgars Miklaševičs
