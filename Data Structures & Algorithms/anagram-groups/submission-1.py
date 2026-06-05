class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for s in strs:
            count = [0]*26
            for ch in s:
                    count[ord(ch)-ord('a')] += 1
            
            if tuple(count) not in groups:
                groups[tuple(count)] = []

            groups[tuple(count)].append(s)

        return list(groups.values())