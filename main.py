mport heapq
 
def parallel_processing(n, m, data):
    output = []
    pavedieni = [(0, i) for i in range(n)]
    heapq.heapify(pavedieni)
    for i in range(m):
        time = data[i]
        g_time, pavediens = heapq.heappop(pavedieni)
        if output:
            y_time = max(g_time, output[-1][1])
        else:
            y_time = g_time
        g_time = y_time + time
        output.append((pavediens, y_time))
        heapq.heappush(pavedieni, (g_time, pavediens))
    return output
 
 
def main():
    n, m = map(int, input().split())
    data = list(map(int, input().split()))
 
    result = parallel_processing(n, m, data)
 
    for pavediens, y_time in result:
        print(pavediens, y_time)
 
 
if name == "main":
    main()

  #Edgars Miklaševičs
