class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        def devowel(word):
            return ''.join('*' if c in 'aeiou' else c for c in word)
        
        exact_words = set(wordlist)
        case_insensitive = {}
        vowel_error = {}
        
        for word in wordlist:
            lower_word = word.lower()
            if lower_word not in case_insensitive:
                case_insensitive[lower_word] = word
            devoweled_word = devowel(lower_word)
            if devoweled_word not in vowel_error:
                vowel_error[devoweled_word] = word
        
        result = []
        for query in queries:
            if query in exact_words:
                result.append(query)
            else:
                lower_query = query.lower()
                if lower_query in case_insensitive:
                    result.append(case_insensitive[lower_query])
                else:
                    devoweled_query = devowel(lower_query)
                    if devoweled_query in vowel_error:
                        result.append(vowel_error[devoweled_query])
                    else:
                        result.append("")
        
        return result
    
    
solution = Solution()
print(solution.spellchecker(["hello", "world"], ["Hello", "WORLD", "word"]))
