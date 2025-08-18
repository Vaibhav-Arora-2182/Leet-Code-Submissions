import time
from typing import List


class Solution:
    """
    You are given 4 numbers (each 1–9).
    Determine if you can form 24 using +, -, *, / and parentheses.
    """

    def judgePoint24(self, cards: List[int]) -> bool:
        """
        Optimised Backtracking Approach:
        - Use recursion to combine numbers step by step.
        - Avoid duplicate permutations by skipping symmetric cases.
        - Only apply valid operations (no div by zero).

        Complexity:
        - Worst case still exponential, but heavy pruning reduces calls drastically.
        - Space: O(n) recursion depth.
        """
        EPSILON = 1e-6

        def solve(nums):
            if len(nums) == 1:
                return abs(nums[0] - 24) < EPSILON

            for i in range(len(nums)):
                for j in range(i + 1, len(nums)):  # i < j to avoid duplicates
                    a, b = nums[i], nums[j]
                    next_nums = [nums[k] for k in range(len(nums)) if k != i and k != j]

                    results = {a + b, a * b, a - b, b - a}
                    if abs(b) > EPSILON:
                        results.add(a / b)
                    if abs(a) > EPSILON:
                        results.add(b / a)

                    for res in results:
                        if solve(next_nums + [res]):
                            return True
            return False

        return solve([float(x) for x in cards])


if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        {"cards": [4, 1, 8, 7], "ans": True},  # (8-4)*(7-1)=24
        {"cards": [1, 2, 1, 2], "ans": False},
        {"cards": [3, 3, 8, 8], "ans": True},  # 8/(3-(8/3))=24
        {"cards": [1, 5, 5, 5], "ans": True},  # 5*(5-(1/5))=24
        {"cards": [9, 9, 9, 9], "ans": False},
    ]

    for ind, test_case in enumerate(test_cases):
        params = {k: v for k, v in test_case.items() if k != "ans"}
        start = time.time()
        ans = sol.judgePoint24(**params)
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
