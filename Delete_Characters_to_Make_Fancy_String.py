import time


class Solution:
    """
    A fancy string is a string where no three consecutive characters are equal.

    Given a string s, delete the minimum possible number of characters from s to make it fancy.

    Return the final string after the deletion. It can be shown that the answer will always be unique.

    Example 1:
    Input: s = "leeetcode"
    Output: "leetcode"

    Example 2:
    Input: s = "aaabaaaa"
    Output: "aabaa"

    Example 3:
    Input: s = "aab"
    Output: "aab"
    """

    def makeFancyString(self, s: str) -> str:
        if len(s) < 3:
            return s

        res = [s[0], s[1]]  # Initialize with first two characters
        for i in range(2, len(s)):
            if s[i] == res[-1] and s[i] == res[-2]:
                continue  # Skip current char if last two are same as it
            res.append(s[i])
        return "".join(res)


# Test cases and runner
if __name__ == "__main__":
    testcases = {
        "Example 1": {
            "s": "leeetcode",
            "ans": "leetcode",
        },
        "Example 2": {
            "s": "aaabaaaa",
            "ans": "aabaa",
        },
        "Example 3": {
            "s": "aab",
            "ans": "aab",
        },
        "Long Sequence": {
            "s": "aaaabbbbccccddddeeeeffffgggghhhh",
            "ans": "aabbccddeeffgghh",
        },
        "No Deletion Needed": {
            "s": "abababab",
            "ans": "abababab",
        },
        "All Same": {
            "s": "aaaaaaaaaaa",
            "ans": "aa",
        },
    }

    solution = Solution()
    for name, tc in testcases.items():
        start = time.perf_counter()
        result = solution.makeFancyString(tc["s"])
        end = time.perf_counter()

        expected = tc["ans"]
        assert (
            result == expected
        ), f"{name} failed:\nExpected: {expected}\nGot: {result}"
        print(f"{name} passed in {(end - start) * 1000:.3f} ms.")
