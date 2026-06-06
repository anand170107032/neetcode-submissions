class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)

        preProd = []
        left = 1

        for i in range(n):
            preProd.append(left)
            left*=nums[i]            

        postProd = [1]*n
        right = 1

        for i in range(n-1, -1, -1):
            postProd[i] = right
            right*=nums[i] 

        out = []
        for i in range(n):
            out.append(preProd[i]*postProd[i])

        return out
