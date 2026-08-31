class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        maxArea = 0
        
        def bfs(i, j):
            tmp = 1
            
            queue = deque()
            queue.append((i, j))

            while(len(queue) > 0):
                r, c = queue.popleft()
                directions = {(1, 0), (-1, 0), (0, 1), (0, -1)}

                for dr, dc in directions: 
                    row = dr + r
                    col = dc + c
                    if 0 <= row < len(grid) and 0 <= col < len(grid[0]) and (row, col) not in visited and grid[row][col] == 1:
                        visited.add((row, col))
                        tmp += 1
                        queue.append((row, col))
            
            return tmp

        

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j] == 1 and  (i, j) not in visited):
                    visited.add((i, j))
                    maxArea = max(maxArea, bfs(i, j))
                    
                    

        return maxArea
