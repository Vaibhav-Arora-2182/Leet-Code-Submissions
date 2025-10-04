import time


class Solution:
    """
    Container With Most Water

    You are given an integer array `height` where `height[i]` represents the height
    of the ith vertical line. Find two lines that form a container with the x-axis,
    such that the container holds the maximum possible water.

    Approach:
    - Use two pointers, one at the start and one at the end.
    - At each step, calculate the area formed by these two lines.
    - Move the pointer corresponding to the shorter line inward,
      because moving the taller line cannot improve the area.
    - Continue until both pointers meet.

    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    def maxArea(self, height: list[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0

        while left < right:
            h = min(height[left], height[right])
            width = right - left
            area = h * width
            max_area = max(max_area, area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area


if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        {"height": [1, 8, 6, 2, 5, 4, 8, 3, 7], "ans": 49},
        {"height": [1, 1], "ans": 1},
        {"height": [4, 3, 2, 1, 4], "ans": 16},
        {"height": [1, 2, 1], "ans": 2},
    ]

    for ind, test_case in enumerate(test_cases):
        params = {k: v for k, v in test_case.items() if k != "ans"}
        start = time.time()
        ans = sol.maxArea(**params)
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
