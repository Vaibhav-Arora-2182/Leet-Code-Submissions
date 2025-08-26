import time
from typing import List


class Solution:
    """
    You are given a 2D array dimensions where:
    - dimensions[i][0] = length of rectangle i
    - dimensions[i][1] = width of rectangle i

    Task:
    - Find the rectangle with the longest diagonal.
    - If multiple rectangles have same diagonal length, pick the one with maximum area.
    - Return its area.
    """

    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        """
        Approach:
       - Use max() with a custom key.
        - Key is a tuple: (l*l + w*w, l*w)
          → ensures max diagonal, and max area on tie.
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        l, w = max(dimensions, key=lambda x: (x[0]**2 + x[1]**2, x[0]*x[1]))
        return l * w



if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        {"dimensions": [[9, 3], [8, 6]], "ans": 48},
        {"dimensions": [[3, 4], [4, 3]], "ans": 12},
        
    ]

    for ind, test_case in enumerate(test_cases):
        params = {k: v for k, v in test_case.items() if k != "ans"}
        start = time.time()
        ans = sol.areaOfMaxDiagonal(**params)
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
