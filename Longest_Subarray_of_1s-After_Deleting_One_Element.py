import time
from typing import List


class Solution:
    """
    Given a binary array nums, you must delete one element from it.
    Return the size of the longest non-empty subarray containing only 1's
    in the resulting array. Return 0 if no such subarray exists.

    Constraints:
    - 1 <= nums.length <= 1e5
    - nums[i] is either 0 or 1
    """

    def longestSubarray(self, nums: List[int]) -> int:
        """
        Approach:
        - Use sliding window with at most one zero allowed inside.
        - Keep track of number of zeros in the current window.
        - If more than one zero, shrink the left side until only one zero remains.
        - Track max window length.
        - Since we must delete one element, the answer is max_len - 1.

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        left = 0
        zero_count = 0
        max_len = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1

            while zero_count > 1:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len - 1


if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        {"nums": [1, 1, 0, 1], "ans": 3},
        {"nums": [0, 1, 1, 1, 0, 1, 1, 0, 1], "ans": 5},
        {"nums": [1, 1, 1], "ans": 2},
        {"nums": [0, 0, 0], "ans": 0},
        {"nums": [1, 0, 1, 1, 0, 1], "ans": 3},
    ]

    for ind, test_case in enumerate(test_cases):
        params = {k: v for k, v in test_case.items() if k != "ans"}
        start = time.time()
        ans = sol.longestSubarray(**params)
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
