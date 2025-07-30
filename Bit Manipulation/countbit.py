def countBits(n: int):
        # li = []

        # for i in range(n+1):
        #     binary = bin(i)
        #     count = 0
        #     for char in binary[2:]:
        #         print(char)
        #         if int(char) & 1:
        #             count += 1
        #     li.append(count)
        ans=[]
        for i in range(n+1):
            ans.append(i.bit_count())
        return ans

        return li
    
print(countBits(5))