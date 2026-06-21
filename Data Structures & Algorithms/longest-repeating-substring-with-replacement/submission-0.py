class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        longest = 0
        left = 0
        freq = {} 
        max_freq = 0

        for right in range(left, len(s)):
                
            ch = s[right]
            freq[ch] = freq.get(ch, 0) + 1

            max_freq = max(max_freq, freq[ch])

            replacement_needed = (right - left + 1) - max_freq

            while replacement_needed > k:
                freq[s[left]] -= 1
                left += 1

                replacement_needed = (right - left + 1) - max_freq

            if replacement_needed <= k:
                longest = max(longest, right - left + 1)

        return longest