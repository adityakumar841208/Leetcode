from itertools import groupby

class Solution:
    def longestBalanced(self, s: str) -> int:
        max_len = 0

        for char, group in groupby(s):
            max_len = max(max_len, len(list(group)))

        # -------- Case B: Two-character balance --------
        def helper(c1, c2):
            mp = {0: -1} 
            x = y = 0
            best = 0
            last1 = last2 = -1

            for i, ch in enumerate(s):
                if ch != c1 and ch != c2:
                    mp = {0: i} # Reset boundary
                    x = y = 0
                    last1 = last2 = -1
                    continue

                if ch == c1:
                    x += 1
                    last1 = i
                else:
                    y += 1
                    last2 = i

                diff = x - y
                if diff in mp:
                    start = mp[diff]
                    # Substring (start, i] must contain at least one of each
                    if last1 > start and last2 > start:
                        best = max(best, i - start)
                else:
                    mp[diff] = i
            return best

        # -------- Case C: Three-character balance --------
        def helperABC():
            mp = {(0, 0): -1}
            a = b = c = 0
            best = 0
            la = lb = lc = -1 

            for i, ch in enumerate(s):
                if ch not in "abc":
                    mp = {(0, 0): i}
                    a = b = c = 0
                    la = lb = lc = -1
                    continue

                if ch == 'a': 
                    a += 1
                    la = i
                elif ch == 'b': 
                    b += 1
                    lb = i
                else: 
                    c += 1
                    lc = i

                key = (a - b, a - c)
                if key in mp:
                    start = mp[key]
                    if la > start and lb > start and lc > start:
                        best = max(best, i - start)
                else:
                    mp[key] = i
            return best

        # Execute all cases
        max_len = max(max_len, helper('a', 'b'))
        max_len = max(max_len, helper('b', 'c'))
        max_len = max(max_len, helper('a', 'c'))
        max_len = max(max_len, helperABC())

        return max_len