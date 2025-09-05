import time


class Solution:
    """
    You are given two integers num1 and num2.

    In one operation, you can choose an integer i in [0, 60] and subtract (2^i + num2) from num1.

    Task:
    - Find the minimum number of operations required to make num1 = 0.
    - If it's impossible, return -1.

    Approach:
    - After k operations:
        num1 - k * num2 must equal the sum of k powers of two.
    - Let diff = num1 - k * num2.
    - Conditions for feasibility:
        1. diff >= k   (we need at least k ones in binary to represent diff)
        2. popcount(diff) <= k   (binary representation must fit within k terms)
    - Loop k from 1 to 60, check feasibility.
    - Return the first valid k, else -1.

    Time Complexity: O(60) ≈ O(1)
    Space Complexity: O(1)
    """

    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        for k in range(1, 61):  # max 60 steps
            diff = num1 - k * num2
            if diff < k:
                continue
            if bin(diff).count("1") <= k:
                return k
        return -1


if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        {"num1": 3, "num2": -2, "ans": 3},
        {"num1": 5, "num2": 7, "ans": -1},
    ]

    for ind, test_case in enumerate(test_cases):
        params = {k: v for k, v in test_case.items() if k != "ans"}

        start = time.time()
        ans = sol.makeTheIntegerZero(**params)
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
