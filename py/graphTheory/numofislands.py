import sys
input=sys.stdin.readline

from collections import deque

def Recur(i,j,visited):
    q=deque()
    visited[i][j]=True
    q.append((i,j))
    while q:
        rol, col=q.popleft()
        direct=[[0, 1], [0, -1], [1, 0], [-1, 0]]
        for dr,dc in direct:
            r,c=rol+dr, col+dc
            if(r in range(R) and c in range(C) and maze[r][c]=="." and visited[r][c]==False):
               q.append((r, c))
               visited[r][c]=True
               
def solveMazeWithPath(maze,R,C):

    visited = [[False for j in range(C)]for i in range(R)]
    count=0
    
    for i in range(R):
        for j in range(C):
            if visited[i][j] == False and maze[i][j] == ".":
                Recur(i,j,visited)
                count+=1
    return count

    

R,C=map(int,input().split())
maze=[input()for i in range(R)]
print(solveMazeWithPath(maze, R,C))
