from collections import Counter 
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for s in strs:
            count = Counter(s)
            key = tuple(sorted(count.items()))
            if key in res:
                res[key].append(s)
            else:
                res[key] = [s]
        return list(res.values())