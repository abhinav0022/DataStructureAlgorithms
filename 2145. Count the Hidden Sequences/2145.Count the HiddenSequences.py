class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        min_val = max_val = curr = 0

        for d in differences:
            curr += d
            min_val = min(min_val, curr)
            max_val = max(max_val, curr)
        
        return max(0, (upper - lower) - (max_val - min_val) + 1)
        '''
        res = 0

        for i in range(lower, upper + 1):
            one = i
            for j, d in enumerate(differences):
                two = d + one
                if not (lower <= two <= upper):
                    break
                if j == len(differences) - 1:
                    res += 1
                one = two
                
        
        
        return res
        '''