class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0: return True
        i = 0
        for char in t:
            if s[i] == char:
                if i==len(s)-1:
                    return True
                i+=1
        return False
