# lc 50. Pow(x, n)
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n

        result = 1
        while n > 0:
            # if we are currently raising to odd power
            # then multiply by x
            if n % 2 == 1:
                result *= x
            # square current_prd current running product
            x *= x

            n = n//2
        return result
            