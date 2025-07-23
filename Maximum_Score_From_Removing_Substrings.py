import time


class Solution:
    """
    You are given a string s and two integers x and y. You can perform two types of operations:

    - Remove substring "ab" and gain x points.
    - Remove substring "ba" and gain y points.

    You can perform these operations in any order and any number of times.

    Return the maximum points you can gain after applying the operations on s.

    Example 1:
    Input: s = "cdbcbbaaabab", x = 4, y = 5
    Output: 19

    Example 2:
    Input: s = "aabbaaxybbaabb", x = 5, y = 4
    Output: 20
    """

    def maximumGain(self, s: str, x: int, y: int) -> int:
        def remove_pattern(s, first, second, score):
            stack = []
            total = 0
            for ch in s:
                if stack and stack[-1] == first and ch == second:
                    stack.pop()
                    total += score
                else:
                    stack.append(ch)
            return "".join(stack), total

        # Prioritize higher scoring pattern
        if x >= y:
            s, score1 = remove_pattern(s, "a", "b", x)
            _, score2 = remove_pattern(s, "b", "a", y)
        else:
            s, score1 = remove_pattern(s, "b", "a", y)
            _, score2 = remove_pattern(s, "a", "b", x)

        return score1 + score2


# Test cases and runner
if __name__ == "__main__":
    testcases = {
        "Example 1": {
            "s": "cdbcbbaaabab",
            "x": 4,
            "y": 5,
            "ans": 19,
        },
        "Example 2": {
            "s": "aabbaaxybbaabb",
            "x": 5,
            "y": 4,
            "ans": 20,
        },
        "Only AB": {
            "s": "ababababab",
            "x": 3,
            "y": 2,
            "ans": 15,  # 5 "ab"s worth 3 each
        },
        "Only BA": {
            "s": "babababa",
            "x": 1,
            "y": 5,
            "ans": 20,  # 4 "ba"s worth 5 each
        },
        "Equal Scores": {
            "s": "abbaabba",
            "x": 3,
            "y": 3,
            "ans": 12,
        },
        "No Matches": {
            "s": "cccccc",
            "x": 10,
            "y": 10,
            "ans": 0,
        },
    }

    solution = Solution()
    for name, tc in testcases.items():
        start = time.perf_counter()
        params = {k: v for k, v in tc.items() if k != "ans"}
        result = solution.maximumGain(**params)
        end = time.perf_counter()

        expected = tc["ans"]
        assert (
            result == expected
        ), f"{name} failed:\nExpected: {expected}\nGot: {result}"
        print(f"{name} passed in {(end - start) * 1000:.3f} ms.")
