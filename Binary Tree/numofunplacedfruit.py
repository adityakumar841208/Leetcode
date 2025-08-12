class Solution:
    
    def numOfUnplacedFruits(self, fruits, baskets):
        n = len(baskets)
        size = 4 * n
        tree = [0] * size

        def build(node, l, r):
            if l == r:
                tree[node] = baskets[l]
                return
            mid = (l + r) // 2
            build(2 * node + 1, l, mid)
            build(2 * node + 2, mid + 1, r)
            tree[node] = max(tree[2 * node + 1], tree[2 * node + 2])

        def update(node, l, r, idx, value):
            if l == r:
                tree[node] = value
                return
            mid = (l + r) // 2
            if idx <= mid:
                update(2 * node + 1, l, mid, idx, value)
            else:
                update(2 * node + 2, mid + 1, r, idx, value)
            tree[node] = max(tree[2 * node + 1], tree[2 * node + 2])

        def find_index(node, l, r, value):
            if tree[node] < value:
                return -1
            if l == r:
                return l
            mid = (l + r) // 2
            left = find_index(2 * node + 1, l, mid, value)
            if left != -1:
                return left
            return find_index(2 * node + 2, mid + 1, r, value)

        build(0, 0, n - 1)
        unplaced = 0

        for fruit in fruits:
            if tree[0] < fruit:
                unplaced += 1
                continue
            idx = find_index(0, 0, n - 1, fruit)
            if idx == -1:
                unplaced += 1
            else:
                update(0, 0, n - 1, idx, float('-inf'))

        return unplaced
    
solution = Solution()
print(solution.numOfUnplacedFruits([4,2,5], [3,5,4]))
        