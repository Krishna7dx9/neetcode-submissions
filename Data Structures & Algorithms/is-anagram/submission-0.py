class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        freq1 = [0] * 26
        freq2 = [0] * 26

        for char in t:
            freq1[ord(char) -  ord('a')] += 1

        for char in s:
            freq2[ord(char) - ord('a')] += 1

        return freq1 == freq2

