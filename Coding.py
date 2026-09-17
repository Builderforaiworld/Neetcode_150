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
# group anagram
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=defaultdict(list)
        for s in strs:
            count=[0]*26
            for c in s:
                count[ord(c)-ord("a")]+=1
            res[tuple(count)].append(s)
        return list(res.values())

# day 3 
top k frequent problem
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        for n in nums:
            count[n]=1+count.get(n,0)
        freq=[[] for i in range(len(nums)+1)]
        for n,c in count.items():
            freq[c].append(n)
        res=[]
        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                res.append(n)
                if len(res)==k:
                     return res
# day 4
valid palindrome
class Solution:
    def isPalindrome(self, s: str) -> bool:
        i=0
        j=len(s)-1
        while i<j:
         while i<j and not s[i].isalnum():
            i+=1
         while i<j and not s[j].isalnum():
            j-=1
         if s[i].lower()!=s[j].lower():
            return False
         i+=1
         j-=1
        return True

        

        

                


        
       
                 
