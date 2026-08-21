from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # count umber of islands
        num_islands = 0
        # directions needed for traversing
        directions = [(0, 1), (1, 0), (0, -1), (-1,0)]
        num_rows, num_cols = len(grid), len(grid[0])

        def bfs(r, c):
            q = deque()
            q.append((r, c))
            grid[r][c] = "0"
            while q:
                i, j = q.popleft()
                for (dr, dc) in directions:
                    new_i = i + dr
                    new_j = j + dc
                    
                    if new_i < 0 or new_j < 0 or new_i >= num_rows or new_j >= num_cols:
                        continue
                    if grid[new_i][new_j] == "0":
                        continue
                    q.append((new_i, new_j))
                    grid[new_i][new_j] = "0"

        for r in range(num_rows):
            for c in range(num_cols):
                if grid[r][c] == "1":
                    bfs(r, c)
                    num_islands += 1
                
        return num_islands
        
                
                


        