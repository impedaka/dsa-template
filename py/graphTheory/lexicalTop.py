import heapq as hq
import sys
input=sys.stdin.readline
adj =[[],[7,4],[1],[4,5],[],[],[],[]]

while True:
    x = int(input())
    y=int(input())
    if x ==0 and y == 0:
        break
    adj[x].append(y)

def Task(adj):
    V = 8
    in_degree = [0] * V

    for u in range(V):
        for x in adj[u]:
            in_degree[x] += 1

    s = []
    for i in range(V):
        if in_degree[i] == 0:
            hq.heappush(s, i)

    cnt = 0
    top_order = []
 
    while s:

        u = hq.heappop(s)
        top_order.append(u)

        for x in adj[u]:
            in_degree[x] -= 1
            if in_degree[x] == 0:
                hq.heappush(s, x)
 
        cnt += 1

    if cnt != V:
        print("Cannot complete these tasks. Going to bed.")
        return

    for i in range(1,len(top_order)):
        print(top_order[i], end=" ")
 
Task(adj)
