class Solution:
    def getSkyline(self, buildings: 'List[List[int]]') -> 'List[List[int]]':
        
        events = [[L, -H, R] for L, R, H in buildings]
        events += [[R, 0, 0] for _, R, _ in buildings]
        events.sort()
        
        # res: result, [x, height]
        # live: heapq, (-height, x)
        res = [[0, 0]]
        live = [(0, float('inf'))]
        for pos, negH, R in events:
            # step1. remove outdated height
            while live[0][1] <= pos:
                heappop(live)
            # step2. if event is starting point, insert into heapq
            if negH:
                heappush(live, (negH, R))
            # step3. if prev height != highest height => insert into result
            if res[-1][1] != -live[0][0]:
                res.append([pos, -live[0][0]])
        return res[1:]
