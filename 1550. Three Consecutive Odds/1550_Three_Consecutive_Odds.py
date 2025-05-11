class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        
        one, two = arr[0], arr[1]
        for i in range(2, len(arr)):
            three = arr[i]
            if one % 2 == 1 and two % 2 == 1 and three % 2 == 1:
                return True
            one, two = two, three
        
        return False