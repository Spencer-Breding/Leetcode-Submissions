class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product = 1
        numSum = 0
        for digit in str(n):
            product *= int(digit)
            numSum += int(digit)
        return product - numSum
