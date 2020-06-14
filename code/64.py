class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # dp(y, x) = grid[y][x] + min(dp(y+1, x), dp(y, x+1))
        R, C = len(grid), len(grid) and len(grid[0])
        @functools.lru_cache(None)
        def dp(y, x):
            if y < 0 or y >= R or x < 0 or x >= C:
                return float('inf')
            if y == R-1 and x == C-1:
                return grid[y][x]
            return grid[y][x] + min(dp(y+1, x), dp(y, x+1))
        return dp(0, 0)
