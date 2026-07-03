class Solution:
    def addBinary(self, a: str, b: str) -> str:

        res = ""

        l = len(a) - 1
        r = len(b) - 1
        carry = 0

        while l >= 0 or r >= 0 or carry:
            x = int(a[l]) if l >= 0 else 0
            y = int(b[r]) if r >= 0 else 0

            total = x + y + carry
            carry = total // 2

            res += str(total % 2)

            l -= 1
            r -= 1

        return res[::-1]