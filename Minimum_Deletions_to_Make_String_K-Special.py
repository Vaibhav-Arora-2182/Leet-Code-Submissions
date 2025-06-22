from collections import Counter


class Solution:
    """
    You are given a string word and an integer k.

    We consider word to be k-special if |freq(word[i]) - freq(word[j])| <= k for all indices i and j in the string.

    Here, freq(x) denotes the frequency of the character x in word, and |y| denotes the absolute value of y.

    Return the minimum number of characters you need to delete to make word k-special.

    """

    def minimumDeletions(self, word: str, k: int) -> int:
        freq = list(Counter(word).values())
        freq.sort()

        res = float("inf")
        n = len(freq)

        for i in range(n):
            # Target min frequency = freq[i]
            # Allow any character frequency in [freq[i], freq[i] + k]
            target_min = freq[i]
            target_max = target_min + k
            deletions = 0

            for f in freq:
                if f < target_min:
                    deletions += f  # remove entire character group
                elif f > target_max:
                    deletions += f - target_max  # reduce to max allowed

            res = min(res, deletions)

        return res
