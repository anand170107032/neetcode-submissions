class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""

        sizes = [str(len(strs[i])) for i in range(len(strs))]
        print(",".join(sizes)+"#"+"".join(strs))
        return ",".join(sizes)+"#"+"".join(strs)


    def decode(self, s: str) -> List[str]:
        if len(s) == 0:
            return []

        s1, s2 = s.split("#", 1)
        sizes = [int(x) for x in s1.split(",")]

        strs =[]
        l=0
        for i in range(len(sizes)):
            strs.append(s2[l:l+sizes[i]])
            l+=sizes[i]

        return strs
