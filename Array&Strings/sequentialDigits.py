def sequentialDigits(low, high):
    sequenceStr = '123456789'

    minLen = len(str(low))
    maxLen = len(str(high))
    ans = []

    for length in range(minLen, maxLen + 1):

        # Possible starting positions
        for start in range(10 - length):

            num = int(sequenceStr[start:start + length])

            if low <= num <= high:
                ans.append(num)

    return ans

print(sequentialDigits(low = 10, high = 1000000000))