import heapq
 
def parallel_processing(n, m, data):
    output = []
    pabi = [(0, i) for i in range(n)]
    heapq.heapify(pabi)
    for i in range(m):
        time = data[i]
        a_time, pabs = heapq.heappop(pabi)
        if output:
            b_time = max(a_time, output[-1][1])
        else:
            b_time = a_time
        a_time = b_time + time
        output.append((pabs, b_time))
        heapq.heappush(pabi, (a_time, pabs))
    return output
 
 
def main():
    n, m = map(int, input().split())
    data = list(map(int, input().split()))
 
    result = parallel_processing(n, m, data)
 
    for pabs, b_time in result:
        print(pabs, b_time)
 
 
if __name__ == "__main__":
    main()
  #Edgars Miklaševičs
