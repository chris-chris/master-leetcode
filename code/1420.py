class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        @functools.lru_cache(None)
        def dp(n, m, k, prevmax):
            """
            1) finishing condition
            if n == 0:
                if k == 0:
                    return 1
                else:
                    return 0
            2) i: 1 ~ m
            i > prevmax => k-1, prevmax => i
            else: k, prevmax => prevmax
            """
            if n == 0:
                if k == 0:
                    return 1
                else:
                    return 0
            cnt = 0
            for i in range(1, m+1): # 1 ~ m
                if i > prevmax:
                    cnt += dp(n-1, m, k-1, i)
                else:
                    cnt += dp(n-1, m, k, prevmax)
            return cnt % (10**9 + 7)
        return dp(n, m, k, 0)
