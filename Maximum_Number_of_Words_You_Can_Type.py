import time
from typing import List


class Solution:
    """

    There is a malfunctioning keyboard where some letter keys do not work.
    All other keys on the keyboard work properly.

    Given:
    - `text`: a string of words separated by spaces
    - `brokenLetters`: a string of distinct broken keys

    Return:
    - The number of words in `text` that can be fully typed without using any broken key.

    Constraints:
    - 1 <= text.length <= 10^4
    - 0 <= brokenLetters.length <= 26
    - text consists only of lowercase English letters and spaces (no leading/trailing spaces).
    - brokenLetters consists of distinct lowercase English letters.
    """

    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        """
        Approach:
        - Convert brokenLetters into a set for O(1) lookup.
        - Split text into words.
        - For each word, check if it contains any broken letter.
        - Count only words that do NOT contain broken letters.
        Time Complexity: O(N * L) where N = number of words, L = average word length.
        """

        broken = set(brokenLetters)
        words = text.split()

        count = 0
        for word in words:
            if all(ch not in broken for ch in word):
                count += 1

        return count


if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        {"text": "hello world", "brokenLetters": "ad", "ans": 1},
        {"text": "leet code", "brokenLetters": "lt", "ans": 1},
        {"text": "leet code", "brokenLetters": "e", "ans": 0},
        {"text": "a b c", "brokenLetters": "z", "ans": 3},
        {"text": "keyboard test", "brokenLetters": "", "ans": 2},
    ]

    for ind, test_case in enumerate(test_cases):
        params = {k: v for k, v in test_case.items() if k != "ans"}
        start = time.time()
        ans = sol.canBeTypedWords(**params)
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
