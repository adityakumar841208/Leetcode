def arrayRankTransform(arr):
        
    sorted_unique = sorted(set(arr))
    rank = {}
    for i, num in enumerate(sorted_unique, 1):
        rank[num] = i


    return [rank[num] for num in arr]

print(arrayRankTransform([40,10,20,30]))