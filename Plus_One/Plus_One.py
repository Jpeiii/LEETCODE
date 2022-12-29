class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        length = len(digits)
        result = 0
        for i in range(length):
            decimal = pow(10, length-1-i)
            result += digits[i] * decimal
        return [int(i) for i in str(result+1)]
