class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0 
        right = 0
        char_dict = {}
        res = 0

        while right < len(s):
            if s[right] not in char_dict:
                char_dict[s[right]] = 1
            else:
                char_dict[s[right]] += 1
            
            while left < len(s) and right - left + 1 - max(char_dict.values()) > k:
                char_dict[s[left]] -= 1
                left += 1

            res = max(res,right - left + 1)
            right += 1
        return res