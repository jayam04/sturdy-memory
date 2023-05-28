class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        num = int(num)
        while num % 10 == 0:
            num = num // 10
        return str(num)