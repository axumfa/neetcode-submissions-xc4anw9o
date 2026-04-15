class Solution:
    def isPalindrome(self, s: str) -> bool:
        i , j = 0, len(s) - 1

        while i < j:
            
            if not s[j].isalnum():
                j -= 1
                continue
            if not s[i].isalnum():
                i += 1 
                continue
            if s[j].lower() == s[i].lower():
                j -= 1
                i +=1 
            else:
                return False
        return True