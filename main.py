import heapq
 
def parallel_processing(n, m, data):
    output = []
    pabi = [(0, i) for i in range(n)]
    heapq.heapify(pabi)
    for i in range(m):
        laiks = data[i]
        a_laiks, pabs = heapq.heappop(pabi)
        if output:
            b_laiks = max(a_laiks, output[-1][1])
        else:
            b_laiks = a_laiks
        a_laiks = b_laiks + laiks
        output.append((pabs, b_laiks))
        heapq.heappush(pabi, (a_laiks, pabs))
    return output
 
 
def main():
    n, m = map(int, input().split())
    data = list(map(int, input().split()))
 
    result = parallel_processing(n, m, data)
 
    for pabs, b_laiks in result:
        print(pabs, b_laiks)
 
 
if __name__ == "__main__":
    main()

  #Edgars Miklaševičs
