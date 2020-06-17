class Solution:
    def minWindow(self, S: str, T: str) -> str:
        def dfs(si, ti):
            if ti == len(T):
                return si
            idx = S.find(T[ti], si+1)
            if idx == -1:
                return float('inf')
            else:
                return dfs(idx, ti+1)
        res = ''
        l = float('inf')
        for si, c in enumerate(S):
            if c == T[0]:
                sj = dfs(si, 1)
                if sj - si < l:
                    l = sj - si
                    res = S[si:sj+1]
        return res
    