# Day 1 Solving Neetcode Problem
#  concatenation of array
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums*2
# Day 2 
# Contains Duplicate
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset=set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False
# two Sum
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j]==target:
                    return [i,j]
        return False


        
       
                 
