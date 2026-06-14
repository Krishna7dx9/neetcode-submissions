from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        freq = defaultdict(list)

        for strr in strs:
            key = str(sorted(strr))
            freq[key].append(strr)

        return list(freq.values())