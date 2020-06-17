class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = newInterval
        res = []
        for index, interval in enumerate(intervals):
            if interval[1] < n[0]:
                res.append(interval)
            elif n[1] < interval[0]:
                res.append(n)
                return res + intervals[index:]
            else:
                n[0] = min(interval[0], n[0])
                n[1] = max(interval[1], n[1])
        res.append(n)
        return res