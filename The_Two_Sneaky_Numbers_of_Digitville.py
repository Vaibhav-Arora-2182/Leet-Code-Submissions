import time
from typing import List


class Solution:
    """
    Problem:
    --------
    In the town of Digitville, there was a list of numbers called `nums` containing
    integers from 0 to n - 1. Each number was supposed to appear exactly once,
    but two numbers appeared twice, making the list longer than usual.

    Your task is to find these two duplicate numbers.

    Return:
        A list of size two containing the two repeated numbers (in any order).

    Examples:
    ----------
    Input: nums = [0,1,1,0]
    Output: [0,1]

    Input: nums = [0,3,2,1,3,2]
    Output: [2,3]

    Input: nums = [7,1,5,4,3,4,6,0,9,5,8,2]
    Output: [4,5]

    Constraints:
    ------------
    2 <= n <= 100
    nums.length == n + 2
    0 <= nums[i] < n
    The input contains exactly two repeated elements.
    """

    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        """
        Approach:
        ----------
        - Use a frequency count to track occurrences of each number.
        - Iterate through `nums` and find which numbers appear twice.

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        freq = [0] * (max(nums) + 1)
        res = []
        for num in nums:
            freq[num] += 1
            if freq[num] == 2:
                res.append(num)
        return res


if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        {"nums": [0, 1, 1, 0], "ans": [0, 1]},
        {"nums": [0, 3, 2, 1, 3, 2], "ans": [2, 3]},
        {"nums": [7, 1, 5, 4, 3, 4, 6, 0, 9, 5, 8, 2], "ans": [4, 5]},
        {"nums": [0, 0, 1, 2], "ans": [0, 0]},
        {"nums": [4, 2, 1, 3, 0, 2, 4], "ans": [2, 4]},
    ]

    for ind, test_case in enumerate(test_cases):
        params = {k: v for k, v in test_case.items() if k != "ans"}
        start = time.time()
        ans = sol.getSneakyNumbers(**params)
        end = time.time()
        elapsed_ms = (end - start) * 1000

        if sorted(ans) != sorted(test_case["ans"]):
            print(
                f"Test Case - {ind + 1} FAILED\n"
                f"Expected: {test_case['ans']}, Got: {ans}\n"
                f"Test Case = {test_case} "
                f"(Time: {elapsed_ms:.4f} ms)\n"
            )
        else:
            print(f"Test Case - {ind + 1} PASSED (Time: {elapsed_ms:.4f} ms)")
