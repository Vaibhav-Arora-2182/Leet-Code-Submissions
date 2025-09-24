import time


class Solution:
    """
    Given two integers numerator and denominator, return the fraction in string format.

    - If the fractional part is repeating, enclose the repeating part in parentheses.
    - If multiple answers are possible, return any of them.
    - Guaranteed that the answer length < 10^4.

    Example 1:
    Input: numerator = 1, denominator = 2
    Output: "0.5"

    Example 2:
    Input: numerator = 2, denominator = 1
    Output: "2"

    Example 3:
    Input: numerator = 4, denominator = 333
    Output: "0.(012)"
    """

    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        """
        Approach:
        - Handle signs separately (result is negative if exactly one of numerator/denominator is negative).
        - Perform integer division for the integral part.
        - Use remainder to simulate long division for the fractional part:
            - Keep a hashmap: remainder -> index in result string.
            - If remainder repeats, we found the repeating cycle.
        - Insert parentheses around repeating part.

        Time Complexity: O(n) where n is length of repeating sequence (≤ denominator).
        Space Complexity: O(n) for hashmap to track remainders.
        """
        if numerator == 0:
            return "0"

        res = []

        if (numerator < 0) ^ (denominator < 0):
            res.append("-")

        numerator, denominator = abs(numerator), abs(denominator)

        res.append(str(numerator // denominator))
        remainder = numerator % denominator

        if remainder == 0:
            return "".join(res)

        res.append(".")
        remainder_map = {}

        while remainder != 0:
            if remainder in remainder_map:
                idx = remainder_map[remainder]
                res.insert(idx, "(")
                res.append(")")
                break

            remainder_map[remainder] = len(res)
            remainder *= 10
            res.append(str(remainder // denominator))
            remainder %= denominator

        return "".join(res)


if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        {"numerator": 1, "denominator": 2, "ans": "0.5"},
        {"numerator": 2, "denominator": 1, "ans": "2"},
        {"numerator": 4, "denominator": 333, "ans": "0.(012)"},
        {"numerator": 1, "denominator": 6, "ans": "0.1(6)"},  # repeating
        {"numerator": -50, "denominator": 8, "ans": "-6.25"},
        {"numerator": 7, "denominator": -12, "ans": "-0.58(3)"},
    ]

    for ind, test_case in enumerate(test_cases):
        params = {k: v for k, v in test_case.items() if k != "ans"}
        start = time.time()
        ans = sol.fractionToDecimal(**params)
        end = time.time()
        elapsed_ms = (end - start) * 1000

        if ans != test_case["ans"]:
            print(
                f"Test Case - {ind + 1} FAILED\n"
                f"Expected: {test_case['ans']}, Got: {ans}\n"
                f"Test Case = {test_case} "
                f"(Time: {elapsed_ms:.4f} ms)\n"
            )
        else:
            print(f"Test Case - {ind + 1} PASSED (Time: {elapsed_ms:.4f} ms)")
