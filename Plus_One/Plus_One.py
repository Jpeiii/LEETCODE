class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        length = len(digits)
        result = 0
        for i in range(length):
            decimal = pow(10, length-1-i)
            result += digits[i] * decimal
        return [int(i) for i in str(result+1)]


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)-1, -1, -1):
            digits[i] += 1
            if (digits[i] >= 10):
                digits[i] = 0
            else:
                return digits

        digits.insert(0, 1)
        return digits
