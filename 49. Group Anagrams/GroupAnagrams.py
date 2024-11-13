class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}

        for w in strs:
            lis = [0]*26
            for c in w:
                lis[ord(c) - ord('a')] += 1
            tup = tuple(lis)
            if tup not in res:
                res[tup] = list()
            res[tup].append(w)
    
        return list(res.values())