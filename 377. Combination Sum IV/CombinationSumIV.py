class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        #dp approach basically the branches of the decision tree dp[4] = dp[4 - 1] + dp[4-2] + dp[4-3], dp[n] represents the number of possible ways to obtain n from nums array
        dp = {0 : 1}

        for i in range(1, target + 1):
            dp[i] = 0
            for n in nums:
                if n <= i:
                    dp[i] += dp[i - n]

        
        return dp[target]

    



        '''
        #Memoization O(N) time and space
        dp = {}
        def combo(tar):
            if tar < 0:
                return 0
            if tar == 0:
                return 1
            if tar in dp:
                return dp[tar]
            res = 0
            for n in nums:
                res += combo(tar - n)
            dp[tar] = res
            return res
        
        return combo(target)
        '''