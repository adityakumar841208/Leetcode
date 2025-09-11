class Solution:
    def sortVowels(s: str) -> str:
        vowel_counts = {}
        vowel_set = "AEIOUaeiou"
        
        # 1. Count the vowels in one pass
        for char in s:
            if char in vowel_set:
                vowel_counts[char] = vowel_counts.get(char, 0) + 1
                
        # 2. Build a string of vowels, already sorted
        # We iterate through "AEIOUaeiou" to ensure the order is correct
        sorted_vowels = []
        for vowel in "AEIOUaeiou":
            if vowel in vowel_counts:
                sorted_vowels.append(vowel * vowel_counts[vowel])
        sorted_vowels = "".join(sorted_vowels)
        
        # 3. Rebuild the string by replacing vowels in order
        result = list(s)
        vowel_idx = 0
        for i in range(len(result)):
            if result[i] in vowel_set:
                result[i] = sorted_vowels[vowel_idx]
                vowel_idx += 1
                
        return "".join(result)

    
solution = Solution()
print(solution.sortVowels("lEetcOde"))  # Output: "lEOtcede"