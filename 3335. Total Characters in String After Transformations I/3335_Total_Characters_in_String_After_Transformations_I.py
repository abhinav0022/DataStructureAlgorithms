class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        mod = 10**9 + 7
        nums = [0]*26

        for c in s:
            nums[ord(c) - 97] += 1
        
        for i in range(t):
            cur = [0]*26
            z = nums[25]
            if z:
                cur[0] = (cur[0] + z) % mod
                cur[1] = (cur[1] + z) % mod
            
            for j in range(25):
                v = nums[j]
                if v:
                    cur[j + 1] = (cur[j + 1] + v) % mod
            nums = cur
        res = 0
        for v in nums:
            res = (res + v) % mod

        return res 


        """Naive Solution"""
        # for i in range(t):
        #     res = []
        #     for c in s:
        #         if c == 'z':
        #             res.append('a')
        #             res.append('b')
        #         else:
        #             res.append(chr(ord(c) + 1))
        #     s = "".join(res)
        
        # return len(s)%(10**9 + 7)
