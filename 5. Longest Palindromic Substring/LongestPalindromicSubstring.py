class Solution:
    def longestPalindrome(self, s: str) -> str:
        def getPal(left, right):
            l = left
            r = right
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return (l + 1, r - 1)
        
        oddLen = ""
        maxLen = 0
        for i in range(len(s)):
            l, r = getPal(i, i)
            if r - l + 1 > maxLen:
                oddLen = s[l: r + 1]
                maxLen = r - l + 1
        
        evenLen = ""
        maxLen = 0
        for i in range(len(s) - 1):
            if s[i] != s[i + 1]:
                continue
            l, r = getPal(i, i + 1)
            if r - l + 1 > maxLen:
                evenLen = s[l: r + 1]
                maxLen = r - l + 1
        
        return evenLen if len(evenLen) > len(oddLen) else oddLen