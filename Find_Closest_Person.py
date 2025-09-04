import time


class Solution:
    """
    You are given three integers x, y, and z, representing the positions of three people on a number line:
    - x is the position of Person 1
    - y is the position of Person 2
    - z is the position of Person 3 (stationary)

    Both Person 1 and Person 2 move toward Person 3 at the same speed.

    Task:
    - Return 1 if Person 1 reaches Person 3 first.
    - Return 2 if Person 2 reaches Person 3 first.
    - Return 0 if both reach at the same time.
    """

    def findClosest(self, x: int, y: int, z: int) -> int:
        """
        Approach:
        - Compute distance of Person 1 from Person 3: abs(x - z)
        - Compute distance of Person 2 from Person 3: abs(y - z)
        - Compare:
          * If Person 1 closer → return 1
          * If Person 2 closer → return 2
          * If equal → return 0

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        dist1 = abs(x - z)
        dist2 = abs(y - z)
        if dist1 > dist2:
            return 2
        elif dist2 > dist1:
            return 1
        else:
            return 0


if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        {"x": 2, "y": 7, "z": 4, "ans": 1},
        {"x": 2, "y": 5, "z": 6, "ans": 2},
        {"x": 1, "y": 5, "z": 3, "ans": 0},
        {"x": 10, "y": 1, "z": 5, "ans": 2},
        {"x": 8, "y": 12, "z": 10, "ans": 0},
    ]

    for ind, test_case in enumerate(test_cases):
        params = {k: v for k, v in test_case.items() if k != "ans"}

        start = time.time()
        ans = sol.findClosest(**params)
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
