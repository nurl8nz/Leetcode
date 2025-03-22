class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = int(str(abs(x))[::-1]) * sign
        return x if -(2**31) <= x <= (2**31 - 1) else 0
