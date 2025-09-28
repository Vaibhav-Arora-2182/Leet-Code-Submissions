import time
from typing import List


class Solution:
    """
    Given an integer array nums, return the largest perimeter of a triangle with a non-zero area,
    formed from three of these lengths. If it is impossible to form any triangle of a non-zero area,
    return 0.

    Example:
    Input: nums = [2,1,2]
    Output: 5
    Explanation: You can form a triangle with side lengths 1, 2, and 2.

    Approach:
    - Sort the array in descending order.
    - Iterate over consecutive triples (nums[i], nums[i+1], nums[i+2]).
    - The first valid triple satisfying triangle inequality (a < b + c) gives the largest perimeter.
    - If no valid triple exists, return 0.

    Time Complexity: O(n log n) (due to sorting)
    Space Complexity: O(1)
    """

    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        for i in range(len(nums) - 2):
            if nums[i] < nums[i + 1] + nums[i + 2]:
                return nums[i] + nums[i + 1] + nums[i + 2]
        return 0


if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        {"nums": [2, 1, 2], "ans": 5},
        {"nums": [1, 2, 1, 10], "ans": 0},
        {"nums": [3, 6, 2, 3], "ans": 8},
        {"nums": [1, 1, 1, 1], "ans": 3},
    ]

    for ind, test_case in enumerate(test_cases):
        params = {k: v for k, v in test_case.items() if k != "ans"}
        start = time.time()
        ans = sol.largestPerimeter(**params)
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
