import heapq
 
def parallel_processing(n, m, data):
    output = []
    pavedieni = [(0, i) for i in range(n)]
    heapq.heapify(pavedieni)
    for i in range(m):
        time = data[i]
        a_time, pavediens = heapq.heappop(pavedieni)
        if output:
            b_time = max(a_time, output[-1][1])
        else:
            b_time = a_time
        b_time = b_time + time
        output.append((pavediens, b_time))
        heapq.heappush(pavedieni, (a_time, pavediens))
    return output
 
 
def main():
    n, m = map(int, input().split())
    data = list(map(int, input().split()))
 
    result = parallel_processing(n, m, data)
 
    for pavediens, b_time in result:
        print(pavediens, b_time)
 
 
if __name__ == "__main__":
    main()
  #Edgars Miklaševičs
