import itertools
class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        start = tuple(itertools.chain(*board))
        target = (1,2,3,4,5,0)
        #BFS
        Q = deque()
        Q.append((start, 0))
        visited = set()
        while Q:
            node, step = Q.popleft()
            visited.add(node)
            # finish condition
            if node == target:
                return step
            nlist = list(node)
            zi = -1
            for i, n in enumerate(nlist):
                if n == 0:
                    zi = i
            for di in [-1, 1, -3, 3]:
                nlist = list(node)
                i2 = zi + di
                if i2 < 0 or i2 >= 6:
                    continue
                if not (abs(i2%3 - zi%3) == 1 or abs(i2-zi) == 3):
                    continue
                
                nlist[i2], nlist[zi] = nlist[zi], nlist[i2]
                nextnode = tuple(nlist)
                if nextnode in visited:
                    continue
                Q.append((nextnode, step+1))
            
        return -1
                
