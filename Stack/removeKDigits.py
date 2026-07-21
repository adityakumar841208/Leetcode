class Solution:
    def removeKdigits(self, num, k):
        
        if len(num) == k:
            return "0"

        stack = [num[0]]
        dup_k = k
        n = len(num)
        ans_len = len(num) - k

        for i in range(1, len(num)):
            
            while k > 0 and stack and int(stack[-1]) > int(num[i]) and ans_len < len(stack) + n - i:
                stack.pop()
                k -= 1

            if n - dup_k > len(stack):
                stack.append(num[i])

        ans = ''.join(stack).lstrip('0')
        return ans if ans else '0'

solution = Solution()
print(solution.removeKdigits("33526221184202197273", 19))