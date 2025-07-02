import time


class Solution:
    """
    Alice is attempting to type a specific string on her computer.
    However, she tends to be clumsy and may press a key for too long, resulting in a character being typed multiple times.

    You are given a string word, which represents the final output displayed on Alice's screen.
    You are also given a positive integer k.

    Return the total number of possible original strings that Alice might have intended to type,
        if she was trying to type a string of size at least k.

    Since the answer may be very large, return it modulo 10**9 + 7.
    """

    MOD = 10**9 + 7

    def possibleStringCount(self, word: str, k: int) -> int:
        n = len(word)
        if n < k:
            return 0  # edge case
        if n == k:
            return 1

        seg = [1]
        for i in range(1, n):
            if word[i] == word[i - 1]:
                seg[-1] += 1
            else:
                seg.append(1)
        m = len(seg)

        total = 1
        take_mod = False
        for x in seg:
            total *= x
            if total >= self.MOD:
                total %= self.MOD
                take_mod = True

        if total == 1 and not take_mod:
            return 1
        if k <= m:
            return total
        maxT = k - m - 1
        dp = [[0] * (maxT + 1) for _ in range(2)]
        prefix = [0] * (maxT + 2)
        dp[0][0] = 1

        for j in range(m):
            s = seg[j]

            prefix[0] = 0
            for i in range(maxT + 1):
                prefix[i + 1] = (prefix[i] + dp[j & 1][i]) % self.MOD

            for i in range(maxT + 1):
                L = max(0, i - (s - 1))
                R = i
                dp[(j + 1) & 1][i] = (prefix[R + 1] - prefix[L]) % self.MOD

        lessK = sum(dp[m & 1]) % self.MOD

        return (total - lessK + self.MOD) % self.MOD


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        {"word": "aabbccdd", "k": 7, "ans": 5},
        {"word": "aabbccdd", "k": 8, "ans": 1},
        {"word": "aaabbb", "k": 3, "ans": 8},
        {
            "word": "vvvvvvvvvvvvvvvvvvvpppppppppppppppppppppuuuuuuuuuuuuuujjjjjjjjjjjjjjjjjjjjkkkkkgggggggggggggggffffflllllllllllllllllllllcccccccccccccccccccccaaaaaaaaaaaavvvvvvvvvvvvvvaaaaaaaaaaaaaaaaaaaaaaeeeeeeeeeeeeeeeeeevvvvvvvvvvvvvvuuuuuuuuuuuuuuuuuuuxxxxxxxxxxxxfffffffffffffiiiiiiiiiiiggggggggggssssssssssssssssssssllllllllllllaaaaaaaaaaaaaaeeeeeeeeeeeeeeeeeeeeeeooooooooooooooooooqqqqqqqqqqqeecccccccccccccffffffffffffffffffffftnnnnnnnnnnnnnnnnooooooovvvvvvvvvvvvvvvvvvvvvvmmmmmmmmmmmqqqqqqqqqqqqqqqcccccccppppppppaaaaaaaaaaaaaaaaekkkzzzzzzzzzzzzzvvvvvvvvvvvveeeeeeeeeqqqqqqqqqqqqqqqqqquuuuuuuuooooooooooooorrrrrrrrrrrrrrrrrrrrggggggggggggggggggggggggwwwwwwwwwwyyyyyyyyyyyyycccccllllllllllllccccccccccccgggqqllllllllllllllnnnnnnnnnnnnnnnnnnnnzzzzzzzzzzzzzzxxxxxxxxxxxxxxxxxqqqqqqnnrrrrrrrrrrrrrrrrrrrwwwwwwxxxxxxxxxvvvvvvvvvvvvvvvvvvvccccccccccrrrrrrrrrrrrrrrrrxxxxxxxxxvvvvvvvaaaaaqqquuuuuuuuuuuuuuuuuuiiiiiiiiiiiiiccccccccccccccwwwwwwwwwwwwbbbbbbbbbbbbbbbbbbbhhhhhhhhhhhhhddddddddddddddddddddddyyyyyyyyhhhhhhhhhhhhhhhhhxxxxxxxxxxxxffffffffffffrrrrrrrrkkkjjjjjjjjfffffffffffffvvvvvvvvvvvvvvvvvvvvvffffffffffffffffffqqqqqqoooooooyyyyyhhhhhhhhhhhhhdddddddddddddddddddbbbbbbbbbbbbbbbbbbpppppyyyyyttttttttttttttssssszzzzzzzzzzzmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmssssssssssssstttttttiiiiiiiiillllllllllxxxxxxxxoooooommmmmmmmmmmmmmmmmmmmmyyyyyyyyyyyyyggppppppppppaaaaaaaaaaaqqqqqqqqqqqqqqqqqqqqqqhhhhhhhhhhhhhhhhhhhhhhhhhiiiiiiiiiiiiiiiiuuuuuuuummmmmmmmmmmmmmmmmmmmmtttttttttttttttttttttttttttttttttllllllllllllllllllllllluuuuuuuuuzzzzzzzzzzzzzzzzzzzzzppppppppppppppppppppprrrrrrrrreeiiiiiiiiiiiiiiiiiiiiiiiqqqqqqqqqqqqqqqiiuuuuuuuuuuuuuuummttttttttttttttttffffffffffffffffffeeeeeeeeeeeeeeeellllllllllllhhhhhhttttttiiiiiiiiiiiiiieooooooooooooooooooqqqqqqqqqqqqqqqqqqqqqqqlllllllllllllllllllzzzzzzzzzzzzzzzzqqqqggggggggggggggaaaaaaeeeeekkkkkkkkkkkkkkkkkkkkkfffpppvvvvvvvvvvvvvvvvvvvvvmmmmmmmmmmmmmmmmmmmuuuuuuuusssssssssssssnnnfffffeeeeeeeettttwwwwwwwwwwwwwwwwwwssssssssskkkkkkkkkkkkkkkkkkssssssssskkkkkkkkkkkkkkkkkktttttttttttttwwwwwwwwwwwwwweeeeeeeeeeeeeelllllluuuuuuuuuuuqqqqqqqqqqqqqqkkkkkkkkkkkkiiiiiiiiiiiiiiiiiiffffffffffffffffffffffccccccctttgggggggggggggggggtttbbbbbaaaaaaaaaaaavvvvvvvvvvvvoooooooooqqqqqqqqqqqqqqqssssssssssssssffffffffppppppppppppppppzzzzzzzzzzzzzzzzrrrrrrrrrrrrhhhhhhhrkooooolllwwwwwwwwwwwwwwwwwwfffffffffffffffffffffffffffffffzzzzzhhhhhhmmmmmmmxxxxxxxxxxxxxxxxxxxooooooooooooooooooooofffffffffffffffwwwwwwdddddddddzzzzzzzzqxxxxxxxxxxxllllllllllllllllyyyyyyyyyyyyyyyyyyyyyyyeeeeeeeeeeeeeeeeeeddddddddddddddddxxxxxxxxxxxxllllllllllllllllllllooxxxxxxxxxxxxxxxxpppppppppppppnddddddddddddeeeeeeeeeeeeeeeeeeeeeeennnnnnnnnnnnneeeeeeeeeeeeeeeevvvvvvvvvvzzjjjjjjjjjjjjjjjjjjjjjjsssssssssssssssssssmmmmmmmmmmmmmmmmmmmfffggggguuuuuuuuuuuuuuuuuuutttiiiiyyyyyyyyyyyyyyyuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuaaaaaaaaaaaaaaaaaaggnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnkkkkkkkkkkkkkkkkkkkkkyyyyyyyyyyyyyyyyyyyyyywwccccllllllllllllllllllcccccccccccccccccccssssssssssssssssskkkkkkkkkkkkktttttteeeeeeeeeeeeeeeeeeeeooopppppppppppppppppppppjjjjjjjjjjjjjjjjjjjjwwwwwwwwwwwwwwwwwwwwxxxxxxxxxxxdddddddddddddddddddooottttttttttttttttxxxxaaaaaaqqqqqqqqqqqqqqqqqkkkkkkkkkkkkkkkkkkkkkbbbbbbbbbbbbbbbbbbiiiiiiiikkkkkkkkkkkkkkkkkkkoooooooooooooooovvvvyyyyyyyyyyaaaaaaaaaaaaaaattttttttttttttttttttoouuuuuuuuuuuuuuuuuuuuuhhhhhhhhhhhhhhhhhuuuuuuukkkkkkkkkkkkkkkiwgggggggggggggggggggggbbbbbbbbbbbwwwwwwwwwwwwwwwwwwwwwwwlllllllllllyyyyyyyyyyyyyyyyyyyddddddddddddddddnnnnnnnnnnnnxxxxxxpppppiiiiiiiiieeeeeeemmmmmmmmmmmmmmmmmeeeegggcccccccccccccccccccuuuuuuuuuuuuuuubbbbbbbbbbbbmmmmmmmmhhhhhhhaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaajjjjjjjjjjjjjjjjjbbbbbbbbzzzzzzzzzzzzzzzzzzzzzzzxxxxxxxxxxuuuuuqqqkkkkkkkkkkkkkkkkkkuuuuuuuuuuuuuuuuuuuuuyyyyyyyyyyyyaaaaaavvvvvvvvvvvvvccccccccccccccccccqqqqqqqqqtttttttttmmmmmmmmmmmmmmmmyyyyyyyyyyyyyyyyyyzzzzzzzzzzzzzzzzziiiiiiiiiiiiiiizzzzzzzzzziiiiiiiiiiiiitttccccccjjjjjjjjjjjjqqqqmmmmmrrrrrrrrrrrrrrrrrrrvvvvvvvvvvvvvvvvvvvxddddddddddddddddzzzzzzzzziiiiiiiiiiiiiiiiiieeeeeeeeeeeqqqqqqqqqqqqqqqqqqqqqqiiiiiiiiilllllllllllllllllllbbbwwwwwwwwwwwwwwwwwwwwwwwzzzzzzzzzzzzzzzzzhhhhhhhhhhbbbbbbbbqqqqqqqqqwwuuuuuuuuuuuuuuuyyyyyyyyyyyyyyyyyyyvvvvvhhhhhhhfffffffffffffqqqqqqqqqqqqqqqqqqqqeeeeeeeeeeeeeeeeeeeeeeezzzzzzzzzzzzzzzzzzzzbbbyyyffffffffbbbbbbbbbnnnnnnffffkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkrrrrrrrrrrrrrrrrraaaaaaaaaaaaaaaaaaaaaaazzwwwwwwwwwwwwwwwwwwwwhhhhhhhhhhhuuuuuuuuujjjjjjjjjjjjjhhhhhhhhhhhhhhhhhhhhhhuuuuuuuuuuuuuuuuuuuuuuqqqqqqqqqqqqqqqaasssssssssssssssssssssqqqqqqqqqqqqqqaaaaaaaaaaaaaaaaaaaaaaazzzzzzzzzzzzzzzztggggggggggbbbbbbbbbggggfffffffffppppppppppprrrrrrrrrrrrrrrrrrrrrrrnnnyyyyyyyyyyyyyyyyyyyyyyyjjjjjjjjjjjjjjjwwwwwwwwwwwwwwwwwwwwwwuurrrrrrrrrrrrrrrrrrraaaaaaaaaaaaaaaaaawwwwwwwwwwwwwwwwiiiiiiillllkkkkkkkkkkkkkkkkkkkkkkzzzzzzllllllllllllllllllllliiiiiiiiiiiiiiiiiiiioooooooooooooooooooooooooooooooooooooooooooojjjjjjjjjjjjcccchhsssssssssssssssssssssssjjjjjjjjjjjjjjjjjjjjjjjgggggggggggggsssssssssssttttttxxxxxxxxxllllllllllllllllllliiiiiiiiiiieeeemmmmmmmmmmmmmmmhhhhhhhhhhhhhhhhhhhhhhhxxxxxxxxxxxxoooooooooooooohhhhhhhtttttttvvvvvvvvvvvooooiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiinnnnnnnnnnnnnnnniiiiiiiiiiiiiiiiiiiiiiiggggggggggggggggggguuuuuuuuuuuuueeeeeeeeeeeeeqqqqqqqqqqqqqqqqqqxiiiiiiiiiicccccccccccccccccccccccdddppppppooooooooooooooooooooooodddddddddddddddccjjjjjjjjjjjjjjjjjjjjjpppppppplllllllllllttttttttttttttttaaaaaaaaaaaaaaarrrgggggggggggozzzbbbbbbbbbbbvvvvvvvvvvvvxxxxxxxxxxxxxxdddddddddbbbbbbbbbbbbbbbbbbbbbbqqqqqqqcccccccccpppppppppppppppppppppppppppppbbbbbbbbbbbpppppppppppppppyyyyyyyyyyyyyyyyyyyyyyymccccccccellllllllllllllllllllvvvvvvvvsssssssssssssssssyyyyyyyyyyyyyyyyyyyyyyyvvvvvvvvvvvvvvvvvvvvssssssssssseeeeeeeeeeeeeeeeeeeeellllllllllllllllllhhhhhhhhhhhhhhhhhhnnnnnnnbbbbbbbbbbbbbbbbbbbbbbbtttttttttttttvvvvvvvvvffffffffffffffffffffeeeeeeeeeeeeeeeeeeepppppppppppppqqqqqqqqqqqqqqxxxxxxxxxbbbbbbvvvvvuuummmmmmmmmbbbbbbbbbbbbbbbbqqqqqqqqqqqqqqqqqqqvvvvvvvvvvvvvvvvhhhhhhhhhhhhhhhccccccccccccccccccccccffffffffffffffffffffiiiiiiiiiiiiiiiiiiijuuuuuubbbbbbbbbbbbkkkkkkkkkkkkkkkkkkkkkttttbbbbbbbbbbbbbbbbbbbbbbvvvvvvvvvvvvvvvvvvuubuuuuuuuuuuuuuuuuuuuuuuunnnnnnnnjjjjjjjjjjjjjjjjjjjjddddddddddddddddddddoooooooooooooooohhhyyyyyyyyyyyyyyyyyyyyyffffffffffffffffffffffzzzzzzzztttttttttttttpppkkkkkkkkkkkkkkkkkkkvvvvvvvvvvvvvvvvvvvvvvkkkkkkkkkkkkkkkkkkkkkmmmmmmmmmmmmggggggggggggggggggggggddddddddddddddddddddxxxxxxxxxxxxxxxxxhhhhhhhhhhhhhnnnnnnnnnnnnnnnnnnniiiiuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuhhhhhhhiiikppppppppppppppppppffffffffffffffffffffnnnnnnnnnnnnnnnnnnnnnnkkkkkknnnnnjjjjjjjdddddddddddrrrrrrrrrrrrrrrrrrrrrrrllllaaaaaaaaaaaaalllllldddddddddddddddddddddddyyyyyyyyyyyyyyypppppxxxxxxxxxxxxxxxxxxxxxxwwwwwwwwwwwwwwwwwwwwwkkkkkkkkaaaaaaaaaaaaaaaaatttttttttttttttffffffffpppppppppppwwwwwwwwwwwwwwwwwwwwwbbbbtttttoooookksssssssssxxxxxxxxxxfffffccccccccccoooooooooooooqqqqnnnnnnnnnnnnnnnnnnnniiiiiiiiiizzzzzzoooaaaaaaaaaaaaaaaaaaaaeeeeeeeeeeeeelllbbbbwwwwrrrrrjjjsssssssssssssssssssssssfffffffwwwwwwwwwwwwwwwwwwqqttttttttteeeeeeeeeggggwwwwwwwwwwwwwwwwwffffffffffffffffffffffqqqqqqqqqqqqqqqqqqqqqqqllllllllllllllllnnnnnnnnnnnnnnnnnnoaaaaaaaaaaaaaaaaaaaaccggggggggggggggggggrrrrrrrrrrrrbbbbbbbbbbbbbbbbbiihhhhhhhhhhhhiiiiiiiiiiiiiiiiiiiilllllllllllllllllllllllwwwwwwwwwwwwwwwcccccccccciissssssssssbbbbbffffffffffnnnnnnnnnnnnnnnnoocccccccccccccccccccccllllllllllllqqqqqqqqrrrrrrrrrrrrrrsshhhhhhhhhhhxxxxxxxxxxxxxxxxxssssssssssssssssvvvvjjjjjjjjjiiiiiiiiiiiiiiiiiiggggggggggggggggggggggggggffffffffffffffffbbbbbbbbbbbbbbbbbbbbbbjjjjjjjjjjjjjjjjjjjjjjjaaaaaawwwwwwwwwwwwwddddddddddddddddddnnnnnnnnnnnnnnpppppppppppjjjjjjjjjjjjjjjjjjjjjjjxxxxxxxxxxxxxxxxxxxbbbbbbbbbbbbbllllllllllllllllllllllkkkkkkkkkkkkkkkkkjjuuaaaaaaaaaaccccccccccccccccccuuuuiiiiiiiiiiiiiiinnnnnnzzzzzzzzzzzzzzzzzzzzwwwwwwwwwwwwwwwwwwwwhhhhhhhhhhhiiiiiiirrrrrrrrrrrrcccccccccccccccccccmmmmhhhhhhhhhhhhiiiiiiiiiiiiiiiiiiiccccccccctttqqqqqqeeeeeeeeeeeoooooooohhhjjjjjjhhhhhhxxxxxxxxxxxxxxxxxxxxuuuunnnnnnnnnnnnnnnnnnnnnooooooooooooouuuuubbbbbbbbbbbbbbbaaaaaaaaaaaaagggggggggggqqqqqqqqqqqqqqqqqqqqaaazzzzzzzzzzzzzzqqqqqqqqqqqqooooooooooollllllxxxxxxxxhhhhhhhhhhhhhhhhhhhhhhhvvvvvvvvvvvvvvhhhhhhhhhhhhppphhhhhhhhhhhhhhhhhiiiiiiiiiiisssssyyyyyyyccccchhhhhhhhhhhhhhhhhoooooooooooooooooooooqqqqqqqqqqqqqqqqqqqqfffrrrrrrrrrrrrrcccccccccccccccccccuubbbbbbbbbbbbbbbbbbbbbbbeeeeeeeeeeeeeeeeeeeegggggggggggggggnnnnnnnnnnnnnnnnnnnejjjjjjjjjjgggggggqqqqqqqvvvvvvvvvvbbbbbbbbbbbbbbbbuuuuuuuuuuuddddddddddddddddddddllllllllllllllltttccofffffffffffffffvvvvvvvvvvvvvvvvvvvvbbbbbbbbbbbbbbbbnnnnnnnnnnnnnnnnnnnnneeeeeeeeeeeeeeeeeeeeeeewwwwwggggggggggggggjjjjjjjjjdddddddddddddddddbbbbbbbbbxxxxxxxxxxxxxxxxxxxxxxpppwwwwwwwwwwwwwwwwwwwwwwwzzzzzzzzzzzzzzzzzzhhhhhhhhhhhhhhhhhhhhhhoooooooooooooooooooonnnnnnnnnnsssssssdddddddddddddddddddttttttttttttttttttddddddddddooooooooooooooooooooooollllllllllllllllhhhhhhhhhhhhhhhhhhuuuuuuuuuuuuuuuuuuuuuuoooooooooppppppppppppppppkrrrrrrrrrrrrrrrrrrffffffffffffffffffffffxxxxxxxxxxxxxjjjjjjjjjjjjjjjjjjjggggggggggggggggggggggccccccccccccccccccccccccccccccqqqqqqqqqqqqqggggggggggggggggbbbbbbbbbbbbwwwwwwwwwwwwwwwhhhhhhhhhhhhhhhhhhhhhaaaaaaaaaiiiiiiiiiiiiiiiiiiiiiiiwwwxxxxxxxxxxxxxxxrrrrrrrrrrrrrrraaaaaaaaaaaaaaaaooooooobbbbiiiiiiiiiidddddddddwwwwwwwonnnnnnnnnnnnnnmgggggggggqqqqqqqqqqqhhhhhhhhhhhxxxxxxxxxsssssssssssssssssyyyyyyyyyyyyyyyyyyyyiiiiiiiiiiiiiiiioooooooooooooooooooooiiiiiiiiiiiiiiiixxxxxxxkkkkkkkkkkzzzzzzzzzpppppppppppppphhhiiiiiiiirrrrrrrrrrrooxxxxxxxxxxxxxxxxxxxxxxiiiiiiiiiiiiiiiiipppppppppppppppppppppyyyyyyyyyyyyyyddddddddddddddddxxxxxhhhhhhhhhhhhhhdddddddddddddddddgggyyyyyyddddddddddddddddqqqtyyyyyyyyyyyyyyynnnnnnnnnnnnnnnnttttttttttttttttttttttttttttttttttttbttttttttttttttiiiiiiiiiiiiiiiiiibbbbbbbbbbbcccccccccccccccggxxxxxxxxxxxxxxxxxxxooooooooooooooiiiiiiiiiiiiiiiiiiiiiiizzzzzzzzzzzzzzzzzzzzzzzqqqqqqqqqqqqqqqqqqqsssssskkkkkkkkkkkkkkjjjvvvvvvvvvvvhhhhhhhhhhhhhhhhhhhheeeeeeeeeeeeeeeeccccccccccccccccvvvhhhhhhhhhhhhhhhhettttttaaaaappppppppppppppppppppnnnnnnnnnnnnnneeeecccccccccpppppmtttttttttttttttttttllllllaaaaaaaaaaaaaa",
            "k": 833,
            "ans": 726690876,
        },
    ]
    for i, t in enumerate(test_cases):
        start = time.time()
        out = sol.possibleStringCount(t["word"], t["k"])
        end = time.time()
        elapsed_ms = (end - start) * 1000
        if out != t["ans"]:
            print(
                f"Test case {i+1} failed: Expected {t['ans']}, Got {out} (Time: {elapsed_ms:.2f} ms)"
            )
        else:
            print(f"Test case {i+1} passed (Time: {elapsed_ms:.2f} ms)")