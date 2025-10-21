import time
from typing import List


class Solution:
    """
    You are given an integer array nums and two integers k and numOperations.

    You can perform `numOperations` operations on nums. In each operation:
    - Select an index i (not selected before)
    - Add an integer x in the range [-k, k] to nums[i]

    Return the maximum possible frequency of any element in nums
    after performing all operations.

    Example:
    --------
    Input: nums = [1,4,5], k = 1, numOperations = 2
    Output: 2
    Explanation:
      - Add 0 to nums[1] → [1, 4, 5]
      - Add -1 to nums[2] → [1, 4, 4]
      → Max frequency = 2
    """

    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        """
        Approach:
        ----------
        1. We can add any value in [-k, k] to selected indices.
        2. For each possible integer value, compute how many elements can be
           converted into that value within the allowed ±k range.
        3. Maintain prefix sums for efficient range counting.
        4. For each value i, compute total elements within [i - k, i + k].
           The potential frequency = freq(i) + min(numOperations, total - freq(i)).
        5. Track the maximum possible frequency.

        Time Complexity: O(max(nums) + k)
        Space Complexity: O(max(nums) + k)
        """
        maxVal = max(nums) + k + 2
        count = [0] * maxVal

        for v in nums:
            count[v] += 1

        for i in range(1, maxVal):
            count[i] += count[i - 1]

        res = 0
        for i in range(maxVal):
            left = max(0, i - k)
            right = min(maxVal - 1, i + k)
            total = count[right] - (count[left - 1] if left else 0)
            freq = count[i] - (count[i - 1] if i else 0)
            res = max(res, freq + min(numOperations, total - freq))

        return res


if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        {"nums": [1, 4, 5], "k": 1, "numOperations": 2, "ans": 2},
        {"nums": [5, 11, 20, 20], "k": 5, "numOperations": 1, "ans": 2},
        {"nums": [1, 2, 3, 4], "k": 2, "numOperations": 2, "ans": 3},
    ]

    for ind, test_case in enumerate(test_cases):
        params = {k: v for k, v in test_case.items() if k != "ans"}
        start = time.time()
        ans = sol.maxFrequency(**params)
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
