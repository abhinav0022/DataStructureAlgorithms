class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        freq = [0]*10

        for i in digits:
            freq[i] += 1
        
        res = []
        for h in range(1, 10):
            if freq[h] == 0:
                continue
            freq[h] -= 1
            for t in range(10):
                if freq[t] == 0:
                    continue
                freq[t] -= 1
                for u in range(0, 10, 2):
                    if freq[u] == 0:
                        continue
                    res.append(h*100 + t*10 + u)
                freq[t] += 1
            freq[h] += 1

        return res