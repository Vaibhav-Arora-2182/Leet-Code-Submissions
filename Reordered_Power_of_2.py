import time


class Solution:
    """
    Problem:
    --------
    Given an integer n, we reorder its digits in any order (including the original order) such that the leading digit is not zero.

    Return True if and only if we can do this so that the resulting number is a power of two.

    A power of two is a number of the form 2^x for some integer x >= 0.

    Examples:
    ---------
    Input: n = 1
    Output: True
    Explanation: 1 is 2^0.

    Input: n = 10
    Output: False
    Explanation: The possible permutations are 10 and 01, neither of which is a power of two.

    Constraints:
    ------------
    1 <= n <= 10^9
    """

    def reorderedPowerOf2(self, n: int) -> bool:
        """
        Checks if the digits of n can be reordered to form a power of two.

        Approach:
        ---------
        - Precompute all powers of two up to 2^30 (since 2^30 = 1,073,741,824 > 10^9).
        - Store their sorted digit strings in a set.
        - Compare the sorted digit string of n to the set.

        Time Complexity: O(1) for practical purposes (small constant size precomputation).
        """

        def sorted_str(x):
            return "".join(sorted(str(x)))

        # Precompute powers of 2 as sorted strings
        power_set = set({sorted_str(1 << i) for i in range(31)})

        return sorted_str(n) in power_set


test_cases = [
    {"n": 1, "ans": True},
    {"n": 10, "ans": False},
    {"n": 16, "ans": True},  # 2^4
    {"n": 24, "ans": False},
    {"n": 46, "ans": True},  # reorder to 64 = 2^6
    {"n": 218, "ans": True},  # reorder to 128 = 2^7
    {"n": 821, "ans": True},  # reorder to 128
    {"n": 123, "ans": False},
]

if __name__ == "__main__":
    sol = Solution()

    for ind, test_case in enumerate(test_cases):
        start = time.time()
        params = {k: v for k, v in test_case.items() if k != "ans"}
        ans = sol.reorderedPowerOf2(**params)
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
