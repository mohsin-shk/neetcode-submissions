from queue import Queue
class Solution:
    def bfs(self,row,col,vis,grid):
        n = len(grid)
        m = len(grid[0])
        vis[row][col]=1
        Q = Queue()
        Q.put((row,col))
        drow = [-1,0,1,0]
        dcol = [0,1,0,-1]

        while not Q.empty():
            cur_row,cur_col = Q.get()
            for i in range(4):
                nRow = cur_row + drow[i]
                nCol = cur_col + dcol[i]
                if 0<=nRow<n and 0<=nCol<m  and not vis[nRow][nCol] and grid[nRow][nCol]=='1':
                    vis[nRow][nCol] = 1
                    Q.put((nRow,nCol))


    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])

        vis = [[0 for _ in range(m)]for _ in range(n)]

        cnt = 0
        for i in range(n):
            for  j in range(m):
                if not vis[i][j] and grid[i][j]=='1':
                    cnt+=1
                    self.bfs(i,j,vis,grid)
        return cnt