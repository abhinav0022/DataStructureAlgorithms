class Solution:
    def numSquares(self, n: int) -> int:
        dp = {i:i for i in range(n + 1)}
        if n < 2:
            return dp[n]
        for target in range(2, n + 1):
            for r in range(1, target + 1):
                square = r*r
                if target < square:
                    break
                dp[target] = min(dp[target], 1 + dp[target - square])
        
        return dp[n]

        
        '''
        #Memoization O(N*N^0.5) time and O(N) space
        cache = {}
        def countSq(n):
            if n == 0:
                return 0
            if n in cache:
                return cache[n]
            
            res = n
            for i in range(1, n + 1):
                if n < i*i:
                    break
                res = min(1 + countSq(n - i*i), res)
            
            cache[n] = res
            return res
        
        return countSq(n)
        '''
            

            
