class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        num = 0
        string = ""
        
        for char in s:
            if char.isdigit():
                num = num*10 + int(char)
            elif char == "[":
                stack.append(string)
                stack.append(num)
                string = ""
                num = 0
            elif char == "]":
                num = stack.pop()
                prev_string = stack.pop()
                string = prev_string + num*string
                num = 0
            else:
                string += char
                 
        return string
        
solution = Solution()
print(solution.decodeString("3[a]2[bc]"))