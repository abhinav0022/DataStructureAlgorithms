class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        minHeap = [(0, (0,0), True)]
        visited = set()
        ROWS, COLS = len(moveTime), len(moveTime[0])

        while minHeap:
            time, node, isOneSec = heapq.heappop(minHeap)
            if (node, isOneSec) in visited:
                continue
            visited.add((node, isOneSec))
            cr, cc = node
            if cr == ROWS - 1 and cc == COLS - 1:
                return time
            dir = [[1, 0], [0, 1], [-1, 0], [0, -1]]
            for dr, dc in dir:
                nr, nc = cr + dr, cc + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS:
                    movT = moveTime[nr][nc]
                    curTime = 0
                    if time >= movT:
                        curTime = time + 1
                    else:
                        curTime = movT + 1
                    if not isOneSec:
                        curTime += 1
                    heapq.heappush(minHeap, (curTime, (nr, nc), not isOneSec))