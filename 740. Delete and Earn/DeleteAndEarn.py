class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        count = Counter(nums)
        nums = sorted(list(set(nums)))

        e1, e2 = 0, 0

        for i in range(len(nums)):
            temp = e2
            if i > 0 and nums[i] == nums[i - 1] + 1:
                e2 = max(nums[i]*count[nums[i]] + e1, temp)
                e1 = temp
            else: 
                e2 = nums[i]*count[nums[i]] + temp
                e1 = temp

        return e2