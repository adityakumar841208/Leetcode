class Solution:
    def clearStars(self, s: str) -> str:
        buckets = [[] for _ in range(26)]  # Buckets for 'a' to 'z'
        to_remove = [False] * len(s)       # Marks for removal

        for i, ch in enumerate(s):
            if ch == '*':
                to_remove[i] = True  # Mark '*' for removal
                # Find the smallest character bucket with entries
                for idx in range(26):
                    if buckets[idx]:
                        remove_idx = buckets[idx].pop()
                        to_remove[remove_idx] = True  # Mark the character for removal
                        break
            else:
                buckets[ord(ch) - ord('a')].append(i)  # Add index to corresponding bucket

        # Build the result string excluding marked characters
        result = ''.join(s[i] for i in range(len(s)) if not to_remove[i])
        return result
    
solution = Solution()
print(solution.clearStars(s = "cb*a*b"))