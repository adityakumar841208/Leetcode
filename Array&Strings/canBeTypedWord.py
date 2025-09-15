def canBeTypedWords(text, brokenLetters):
        
        words = text.split(" ")
        letters = list(brokenLetters)
        count = 0

        for word in words:
            flag = 0
            for char in letters:
                if char in word:
                    flag = 1
                    break

            if flag != 1:
                count += 1

        return count
    
print(canBeTypedWords("hello world", "ad"))