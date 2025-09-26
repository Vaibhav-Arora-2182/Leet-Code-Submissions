import time
from typing import List


class Solution:
    """
    Given an integer array nums, return the number of triplets (i,j,k)
    that can form a valid triangle. A triangle is valid if:
        nums[i] + nums[j] > nums[k]
    after sorting the array (with i < j < k).
    """

    def triangleNumber(self, nums: List[int]) -> int:
        """
        Approach:
        - Sort the array.
        - Fix the largest side nums[k], and use two pointers (i, j) to find
          how many pairs nums[i] + nums[j] > nums[k].
        - If nums[i] + nums[j] > nums[k], then all pairs from i..j-1 with j are valid.
          Add (j - i) to count, then decrement j.
        - Otherwise, increment i.

        Time Complexity: O(n^2)
        Space Complexity: O(1)
        """
        nums.sort()
        n = len(nums)
        count = 0

        for k in range(n - 1, 1, -1):
            i, j = 0, k - 1
            while i < j:
                if nums[i] + nums[j] > nums[k]:
                    count += j - i
                    j -= 1
                else:
                    i += 1

        return count


if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        {"nums": [2, 2, 3, 4], "ans": 3},
        {"nums": [4, 2, 3, 4], "ans": 4},
        {"nums": [1, 1, 1, 1], "ans": 4},
        {"nums": [0, 1, 1, 1], "ans": 1},
        {"nums": [10, 21, 22, 100, 101, 200, 300], "ans": 6},
    ]

    for ind, test_case in enumerate(test_cases):
        params = {k: v for k, v in test_case.items() if k != "ans"}
        start = time.time()
        ans = sol.triangleNumber(**params)
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
