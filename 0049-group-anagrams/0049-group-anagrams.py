from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = defaultdict(list)
        
        for s in strs:
            # Sort the string and use it as the key
            key = ''.join(sorted(s))
            # Append the original string to the list corresponding to this sorted key
            anagram_dict[key].append(s)
        
        # Return the grouped anagrams as a list of lists
        return list(anagram_dict.values())