class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        word = ''
        for i in range(len(s2)):
            word += s2[i]

            if len(word) == len(s1):
                if sorted(word) == sorted(s1):
                    return True
                word = word[1:]
        return False