import time


class Solution:
    """
    Given an integer n, return true if it is a power of two. Otherwise, return false.

    An integer n is a power of two, if there exists an integer x such that n == 2^x.


    """

    def isPowerOfTwo(self, n: int) -> bool:
        # A power of two must be > 0 and have exactly one bit set in binary form
        return n > 0 and (n & (n - 1)) == 0


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        {"n": 1, "ans": True},  # 2^0
        {"n": 16, "ans": True},  # 2^4
        {"n": 3, "ans": False},  # Not a power of two
        {"n": 1024, "ans": True},  # 2^10
        {"n": 0, "ans": False},  # Zero is not a power of two
        {"n": -2, "ans": False},  # Negative numbers not allowed
        {"n": 2**30, "ans": True},  # Large power of two
        {"n": 2**31 - 1, "ans": False},  # Max 32-bit int but not a power of two
    ]

    for ind, test_case in enumerate(test_cases):
        start = time.time()
        params = {k: v for k, v in test_case.items() if k != "ans"}
        ans = sol.isPowerOfTwo(**params)
        end = time.time()
        elapsed_ms = (end - start) * 1000
        if ans != test_case["ans"]:
            print(
                f"Test Case - {ind + 1} failed\nExpected: {test_case['ans']}, Got: {ans}\nTest Case = {test_case} (Time: {elapsed_ms:.4f} ms)"
            )
        else:
            print(f"Test Case - {ind + 1} passed (Time: {elapsed_ms:.4f} ms)")
