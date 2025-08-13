import time


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        """
        Determine whether a given integer is a power of three.

        An integer n is a power of three if there exists an integer x such that:
            n == 3 ** x

        This function uses the mathematical property that the maximum power of
        three within the range of signed 32-bit integers is 3^19 = 1162261467.
        If n is a positive divisor of 3^19, it must be a power of three.

        Args:
            n (int): The integer to check.

        Returns:
            bool: True if n is a power of three, False otherwise.

        Example:
            >>> sol = Solution()
            >>> sol.isPowerOfThree(27)
            True
            >>> sol.isPowerOfThree(0)
            False
            >>> sol.isPowerOfThree(-1)
            False
        """
        if n <= 0:
            return False
        while n > 1:
            if n % 3 == 0:
                n = n // 3
            else:
                return False
        return True


if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        {"n": 27, "ans": True},  # 3^3
        {"n": 0, "ans": False},  # Zero cannot be a power of three
        {"n": -1, "ans": False},  # Negative numbers not allowed
        {"n": 1, "ans": True},  # 3^0
        {"n": 9, "ans": True},  # 3^2
        {"n": 45, "ans": False},  # Not a power of three
    ]

    for ind, test_case in enumerate(test_cases):
        start = time.time()
        params = {k: v for k, v in test_case.items() if k != "ans"}
        ans = sol.isPowerOfThree(**params)
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
