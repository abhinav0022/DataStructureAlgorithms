class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for i in range(len(nums) + 1)]
        countMap = Counter(nums)
        numSet = set(nums)
        for n in numSet:
            freq[countMap[n]].append(n)
        res = []
        while k > 0:
            for i in range(len(freq) - 1, 0, -1):
                for n in freq[i]:
                    res.append(n)
                    k -= 1
                    if k == 0:
                        return res
        return res
        