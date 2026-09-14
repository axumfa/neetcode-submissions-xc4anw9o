class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        visits = set()
        queue  = deque()

        def addRooms(r, c):
            if (r < 0 or r ==ROWS or c < 0 or c == COLS or (r, c)  in visits or grid[r][c] == -1):
                return
            queue.append([r, c])
            visits.add((r, c))
            
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    queue.append([r, c])
                    visits.add((r, c))
        
        
        dist = 0
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                grid[r][c] = dist
                addRooms(r + 1, c)
                addRooms(r - 1, c)
                addRooms(r, c + 1)
                addRooms(r, c- 1)
            dist += 1

