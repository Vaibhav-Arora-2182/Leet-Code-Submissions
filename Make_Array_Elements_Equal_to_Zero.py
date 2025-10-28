import time
from typing import List


class Solution:
    """
    Hercy-style simulation problem:

    Given an integer array `nums`, you start from any index `curr` such that `nums[curr] == 0`
    and choose a movement direction (left or right). You then simulate:
      - If out of bounds → stop.
      - If nums[curr] == 0 → move one step in the same direction.
      - Else if nums[curr] > 0:
            - Decrement nums[curr] by 1.
            - Reverse direction.
            - Move one step in the new direction.

    A selection (curr, direction) is valid if, by the end, all elements become zero.

    Return the number of valid (curr, direction) selections.
    """

    def countValidSelections(self, nums: List[int]) -> int:
        """
        Approach:
        - For every index i where nums[i] == 0:
            - Try simulating movement in both directions.
            - Check if all elements become zero by the end.
        - Simulation rules as per description.
        - Return total number of valid selections.

        Complexity:
        O(n^2) worst case (since n ≤ 100, this is fine).
        """

        def simulate(start: int, direction: int) -> bool:
            arr = nums[:]  # copy
            curr = start
            while 0 <= curr < len(arr):
                if arr[curr] == 0:
                    curr += direction
                else:
                    arr[curr] -= 1
                    direction *= -1
                    curr += direction
            return all(x == 0 for x in arr)

        total = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                if simulate(i, 1):
                    total += 1
                if simulate(i, -1):
                    total += 1
        return total


if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        {"nums": [1, 0, 2, 0, 3], "ans": 2},
        {"nums": [2, 3, 4, 0, 4, 1, 0], "ans": 0},
        {"nums": [0], "ans": 2},
        {"nums": [1, 0, 1], "ans": 2},
    ]

    for ind, test_case in enumerate(test_cases):
        params = {k: v for k, v in test_case.items() if k != "ans"}
        start = time.time()
        ans = sol.countValidSelections(**params)
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
