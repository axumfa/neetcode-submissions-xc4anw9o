class Solution:
    def longestPalindrome(self, s: str) -> str:
        def palindrome(left, right):
            while(left >= 0 and right < len(s) and s[left] == s[right]):
                left -= 1
                right += 1
            
            return right - left - 1
        
        max1 = 0
        start = 0
        for i in range(len(s)):
            even = palindrome(i, i + 1)
            odd = palindrome(i, i)
            curMax = max(odd, even)

            if curMax > max1:
                max1 = curMax
                start = i - (curMax - 1) // 2
            
        return s[start: max1 + start]