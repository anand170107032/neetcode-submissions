class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        freq = {}

        for x in s:
            if x in freq:
                freq[x] += 1
            else:
                freq[x] = 1

        for x in t:
            if x not in freq:
                return False
            else:
                freq[x] -= 1
        
        for x,y in freq.items():
            if y!=0:
                return False

        return True
