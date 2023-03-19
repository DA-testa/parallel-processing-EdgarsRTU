import heapq
 
def parallel_processing(n, m, data):
    output = []
    W = [(0, i) for i in range(n)]
    heapq.heapify(W)
    for i in range(m):
        laiks = data[i]
        a_laiks, W = heapq.heappop(W)
        if output:
            b_laiks = max(a_laiks, output[-1][1])
        else:
            b_laiks = a_laiks
        a_time = b_laiks + laiks
        output.append((W, b_laiks))
        heapq.heappush(W, (a_laiks, W))
    return output
 
 
def main():
    n, m = map(int, input().split())
    data = list(map(int, input().split()))
 
    result = parallel_processing(n, m, data)
 
    for W, b_laiks in result:
        print(W, b_laiks)
 
 
if __name__ == "__main__":
    main()
