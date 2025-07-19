class Solution:
    def removeSubfolders(self, folder):
        
        folder.sort()
        res = []
        for path in folder:
            if not res or not path.startswith(res[-1] + '/'):
                res.append(path)
        return res
    
solution = Solution()
print(solution.removeSubfolders(["/a","/a/b","/c/d","/c/d/e","/c/f"]))

