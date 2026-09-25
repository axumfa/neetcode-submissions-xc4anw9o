class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time, fresh = 0, 0
        q = deque()
        ROWS, COLS = len(grid), len(grid[0])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))
        
        directions = {(-1, 0), (1, 0), (0, 1), (0, -1)}
        while q and fresh > 0:

            for i in range(len(q)):
                row, col = q.popleft()

                for dr, dc in directions:
                    r = row + dr
                    c = col + dc

                    if( 0 > c or c >= COLS or 0 > r or r >= ROWS or grid[r][c] == 2 or grid[r][c] == 0):
                        continue

                    fresh -= 1
                    grid[r][c] = 2
                    q.append((r, c))
            time += 1
        
        return time if not fresh else -1
