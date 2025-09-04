class Solution:
    def numberOfPairs(self, points):
        n = len(points)
        count = 0
        

        for i in range(n):
            for j in range(n):
                if i == j:
                    continue

                xi, yi = points[i]
                xj, yj = points[j]

                if xi <= xj and yi >= yj and (xi, yi) != (xj, yj):
                    is_unobstructed = True

                    for k in range(n):
                        if k == i or k == j:
                            continue
                        
                        xk, yk = points[k]


                        if xi <= xk <= xj and yj <= yk <= yi:
                            is_unobstructed = False
                            break

                    if is_unobstructed:
                        count += 1
        return count