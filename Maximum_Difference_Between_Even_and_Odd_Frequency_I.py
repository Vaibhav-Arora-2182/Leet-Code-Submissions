from collections import Counter


class Solution:
    """
    You are given a string s consisting of lowercase English letters.

    Your task is to find the maximum difference diff = freq(a1) - freq(a2) between the frequency of characters a1 and a2 in the string such that:

    a1 has an odd frequency in the string.
    a2 has an even frequency in the string.
    Return this maximum difference.
    """

    def maxDifference(self, s: str) -> int:
        freq = Counter(s)
        odd_freq = []
        even_freq = []
        for count in freq.values():
            if count % 2 == 1:
                odd_freq.append(count)
            else:
                even_freq.append(count)
        if not odd_freq or not even_freq:
            return 0
        return max(odd_freq) - min(even_freq)
