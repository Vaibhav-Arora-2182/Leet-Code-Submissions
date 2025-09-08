import time
from typing import List


class Solution:
    """
    Given an integer n, return two No-Zero integers [a, b] such that:
    - a and b are positive integers with no '0' in their decimal representation.
    - a + b = n
    """

    def getNoZeroIntegers(self, n: int) -> List[int]:
        """
        Approach:
        - Iterate a from 1 to n-1.
        - Let b = n - a.
        - Check if both a and b do not contain '0' in their decimal representation.
        - Return [a, b] once found (guaranteed by problem constraints).
        """

        def is_no_zero(x: int) -> bool:
            return "0" not in str(x)

        for a in range(1, n):
            b = n - a
            if is_no_zero(a) and is_no_zero(b):
                return [a, b]
        return []


if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        {"n": 2, "ans": [1, 1]},
        {
            "n": 11,
            "ans": [2, 9],
        },
        {"n": 101, "ans": None},
        {"n": 9999, "ans": None},
    ]

    for ind, test_case in enumerate(test_cases):
        params = {k: v for k, v in test_case.items() if k != "ans"}
        start = time.time()
        ans = sol.getNoZeroIntegers(**params)
        end = time.time()
        elapsed_ms = (end - start) * 1000

        valid = (
            isinstance(ans, list)
            and len(ans) == 2
            and sum(ans) == test_case["n"]
            and "0" not in str(ans[0])
            and "0" not in str(ans[1])
        )

        if not valid:
            print(
                f"Test Case - {ind + 1} FAILED\n"
                f"Expected valid no-zero pair for {test_case['n']}, Got: {ans}\n"
                f"Test Case = {test_case} "
                f"(Time: {elapsed_ms:.4f} ms)\n"
            )
        else:
            print(f"Test Case - {ind + 1} PASSED (Time: {elapsed_ms:.4f} ms)")
