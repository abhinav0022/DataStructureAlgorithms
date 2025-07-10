class Solution:
    def isValid(self, s: str) -> bool:
        close_to_open = {')': '(', '}': '{', ']': '['}
        stk = []
        for c in s:
            if c in close_to_open.values():
                stk.append(c)
            elif c in close_to_open:
                if not stk or close_to_open[c] != stk.pop() :
                    return False
        
        return not stk