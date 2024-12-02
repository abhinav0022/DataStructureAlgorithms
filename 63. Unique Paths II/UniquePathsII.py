class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        #dp solution
        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])
        dp = [0 for i in range(COLS)]
        dp[COLS - 1] = 1

        for r in range(ROWS - 1, -1, -1):
            for c in range(COLS - 1, -1, -1):
                if obstacleGrid[r][c] == 1:
                    dp[c] = 0
                elif c + 1 < COLS:
                    dp[c] = dp[c] + dp[c + 1]
        
        return dp[0]
        
        
        '''
        # memoization O(MN) time and space
        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0]) 
        dp = {} #key cordinates i,j and value is the unique path from that position

        def numPaths(i, j):
            if i >= ROWS or j >= COLS or obstacleGrid[i][j] == 1:
                return 0
            if i == ROWS - 1 and j == COLS - 1:
                return 1
            if (i, j) in dp:
                return dp[(i, j)]
            
            res = numPaths(i + 1, j) + numPaths(i, j + 1)
            dp[(i, j)] = res
            return res
        
        return numPaths(0, 0)
        '''
        