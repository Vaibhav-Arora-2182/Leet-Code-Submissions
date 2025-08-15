import time

class Solution:
    """
    Solution class for checking if a given integer is a power of four.

    A power of four is an integer of the form:
        n = 4^x
    where x is a non-negative integer (x >= 0).
    
    Constraints:
    - n can be positive, negative, or zero.
    - Returns True only for positive powers of four (including 1, since 4^0 = 1).

    Examples
    --------
    >>> sol = Solution()
    >>> sol.isPowerOfFour(16)
    True
    >>> sol.isPowerOfFour(5)
    False
    >>> sol.isPowerOfFour(1)
    True
    >>> sol.isPowerOfFour(64)
    True
    >>> sol.isPowerOfFour(0)
    False
    >>> sol.isPowerOfFour(-4)
    False
    """

    def isPowerOfFour(self, n: int) -> bool:
        """
        Check if the given integer is a power of four.

        Parameters
        ----------
        n : int
            The integer to check.

        Returns
        -------
        bool
            True if n is a power of four, otherwise False.
        """
        # A number is a power of four if:
        # 1. It's positive.
        # 2. It's a power of two (only one bit set in binary form).
        # 3. That '1' bit is at an even position in binary representation.
        return n > 0 and (n & (n - 1)) == 0 and (n & 0x55555555) != 0


if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        {"n": 16, "ans": True},   
        {"n": 5, "ans": False},   
        {"n": 1, "ans": True},    
        {"n": 64, "ans": True},   
        {"n": 0, "ans": False},   
        {"n": -4, "ans": False},  
    ]

    for ind, test_case in enumerate(test_cases):
        start = time.time()
        params = {k: v for k, v in test_case.items() if k != "ans"}
        ans = sol.isPowerOfFour(**params)
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
