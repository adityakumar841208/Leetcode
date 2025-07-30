from collections import defaultdict

class Solution:
    def deleteDuplicateFolder(self, paths):
        res = []
        hash_map = defaultdict(list)

        # Step 1: Build the map of parent -> list of subfolders
        for item in paths:
            key = item[0]
            for i in range(1, len(item)):
                hash_map[key] = hash_map.get(key, []) + [item[i]]

        # Step 2: Reverse the map to find duplicate subfolder structures
        structure_count = defaultdict(int)
        structure_map = {}

        for key, values in hash_map.items():
            folder_signature = tuple(sorted(values))  # deterministic signature
            structure_map[key] = folder_signature
            structure_count[folder_signature] += 1

        # Step 3: Collect only unique folders and their paths
        for path in paths:
            parent = path[0]
            if len(path) == 1:  # top-level folder
                if parent not in structure_map or structure_count[structure_map[parent]] == 1:
                    res.append(path)
            else:
                if structure_count.get(structure_map.get(parent), 0) == 1:
                    res.append(path)

        return res

# Test
solution = Solution()
print(solution.deleteDuplicateFolder([["a"],["c"],["d"],["a","b"],["c","b"],["d","a"]]))

     