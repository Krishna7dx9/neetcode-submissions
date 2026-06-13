from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        freq_t = defaultdict(int)
        freq_s = defaultdict(int)

        for char in t:
            freq_t[char] += 1

        for char in s:
            freq_s[char] += 1

        if freq_t == freq_s:
            return True
        return False