class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        #Dynamic programming solution
        dp = triangle[len(triangle) - 1]

        for i in range(len(triangle) - 2, -1 , -1):
            newDP = [0 for k in range(len(triangle[i]))]
            for j in range(len(triangle[i]) - 1, -1, -1):
                newDP[j] = triangle[i][j] + min(dp[j], dp[j + 1])
            dp = newDP
        
        return dp[0]


        '''
        #top-down
        #Memoization and O(n^2) space and O(N) N-> total number of points in the triangle n-> is total number of rows in triangle
        dp = {}

        def minSum(level, i):
            if level >= len(triangle):
                return 0
            if (level, i) in dp:
                return dp[(level, i)]
            
            res = triangle[level][i] + min(minSum(level + 1, i), minSum(level + 1, i + 1))
            dp[(level, i)] = res
            return res
        
        return minSum(0, 0)
        '''