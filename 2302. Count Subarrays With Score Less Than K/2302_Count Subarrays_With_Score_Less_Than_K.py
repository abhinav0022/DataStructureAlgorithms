class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        left, count, right = 0, 0, 0
        sub_sum = nums[0]

        while left < len(nums) and right < len(nums):
            if sub_sum*(right - left + 1) >= k:
                sub_sum -= nums[left]
                left += 1
            else:
                count += right - left + 1
                if right + 1 < len(nums):
                    right += 1 
                else:
                    break;
                sub_sum += nums[right]
        
        return count