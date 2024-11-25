class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def charCount(w):
            mapC = {}
            for c in w:
                if c not in mapC:
                    mapC[c] = 0
                mapC[c] += 1
            return mapC
        t_map, s_map = charCount(t), charCount(s)
        
        if len(t_map) != len(s_map):
            return False
        for c in t_map:
            if c not in s_map:
                return False
            if t_map[c] != s_map[c]:
                return False
        return True