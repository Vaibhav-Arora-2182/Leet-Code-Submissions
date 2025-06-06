class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        MAX_VALUE = 2**31 - 1
        MIN_VALUE = -(2**31)
        if abs(divisor) > abs(dividend):
            return 0
        if divisor == 1:
            return dividend
        if dividend == MIN_VALUE and divisor == -1:
            return MAX_VALUE

        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1

        ans = 0
        dividend, divisor = abs(dividend), abs(divisor)

        powers = []
        power = 0
        while (divisor << power) <= dividend:
            powers += [(divisor << power, 1 << power)]
            power += 1

        for value, multiple in reversed(powers):
            if dividend >= value:
                dividend -= value
                ans += multiple

        return min(max(sign * ans, MIN_VALUE), MAX_VALUE)
