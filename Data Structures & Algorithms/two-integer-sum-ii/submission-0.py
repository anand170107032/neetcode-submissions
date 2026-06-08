class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        l, r = 0, n-1

        while l < r:
            currSum = numbers[l]+numbers[r]
            if currSum == target:
                return [l+1, r+1]
            while l<r and numbers[l]==numbers[l+1]:
                l+=1
            while l<r and numbers[r]==numbers[r-1]:
                r-=1
            
            if currSum < target:
                l+=1
            else:
                r-=1
        return