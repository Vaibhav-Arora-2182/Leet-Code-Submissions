from typing import List


class Solution:
    """
    A string s can be partitioned into groups of size k using the following procedure:

    The first group consists of the first k characters of the string,
    the second group consists of the next k characters of the string, and so on.
    Each element can be a part of exactly one group.
    For the last group, if the string does not have k characters remaining,
    a character fill is used to complete the group.
    Note that the partition is done so that after removing
    the fill character from the last group (if it exists) and concatenating all the groups in order,
    the resultant string should be s.

    Given the string s, the size of each group k and the character fill,
    return a string array denoting the composition of every group s has been divided into,
    using the above procedure.
    """

    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            group = s[i : i + k]
            if len(group) < k:
                group += fill * (k - len(group))
            res.append(group)
            i += k
        return res
