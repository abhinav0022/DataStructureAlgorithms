class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        # [1,3,2,3,4,5]
        max_num = max(nums)
        curr_freq = 0
        res = 0
        left = 0
        for right in range(len(nums)):
            curr_freq += nums[right] == max_num
            while curr_freq >= k:
                curr_freq -= nums[left] == max_num
                left += 1
            res += left #it is res += left outside of the while not res+=1 within the while, draw a picture, you will realize left pointer represents all the valid subarrays from the left side
        return res