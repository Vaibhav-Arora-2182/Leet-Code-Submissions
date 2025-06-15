class Solution:
    """
    You are given an integer num. You will apply the following steps to num two separate times:

      -  Pick a digit x (0 <= x <= 9).
      -  Pick another digit y (0 <= y <= 9). Note y can be equal to x.
      -  Replace all the occurrences of x in the decimal representation of num by y.
      -  Let a and b be the two results from applying the operation to num independently.

        Return the max difference between a and b.

    Note that neither a nor b may have any leading zeros, and must not be 0.
    """

    def maxDiff(self, num: int) -> int:
        s = str(num)

        for ch in s:
            if ch != "9":
                max_num = int(s.replace(ch, "9"))
                break
        else:
            max_num = num

        if s[0] != "1":
            min_num = int(s.replace(s[0], "1"))
        else:
            for ch in s[1:]:
                if ch not in ("0", "1"):
                    min_num = int(s.replace(ch, "0"))
                    break
            else:
                min_num = num

        return max_num - min_num
