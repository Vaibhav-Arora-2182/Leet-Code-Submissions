import time


class Solution:
    """
    There is a programming language with only four operations and one variable X:
        - ++X and X++ increment X by 1
        - --X and X-- decrement X by 1

    Initially, X = 0.

    Given an array of strings `operations`, return the final value of X after performing all operations.

    Example 1:
        Input: operations = ["--X", "X++", "X++"]
        Output: 1
        Explanation:
            X = 0
            --X → -1
            X++ → 0
            X++ → 1

    Example 2:
        Input: operations = ["++X", "++X", "X++"]
        Output: 3

    Example 3:
        Input: operations = ["X++", "++X", "--X", "X--"]
        Output: 0
    """

    def finalValueAfterOperations(self, operations: list[str]) -> int:
        """
        Approach:
        - Initialize X = 0
        - Iterate through each operation string.
        - If the operation contains '+', increment X by 1.
        - If the operation contains '-', decrement X by 1.
        - Return X after all operations.

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        X = 0
        for op in operations:
            if "+" in op:
                X += 1
            else:
                X -= 1
        return X


if __name__ == "__main__":

    sol = Solution()

    test_cases = [
        {"operations": ["--X", "X++", "X++"], "ans": 1},
        {"operations": ["++X", "++X", "X++"], "ans": 3},
        {"operations": ["X++", "++X", "--X", "X--"], "ans": 0},
        {"operations": ["++X"], "ans": 1},
        {"operations": ["--X", "--X", "--X"], "ans": -3},
    ]

    for ind, test_case in enumerate(test_cases):
        params = {k: v for k, v in test_case.items() if k != "ans"}
        start = time.time()
        ans = sol.finalValueAfterOperations(**params)
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
