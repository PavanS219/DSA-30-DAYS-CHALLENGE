class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Method 1 : Using Set Property :
        # a = set(nums)
        # if len(a) != len(nums):
        #     return True
        # else:
        #     return False
            
        # Method 2 : Using dictionary:
        freq = {}
        for n in nums:
            if n in freq:    
                return True
            freq[n] = 1
        return False


        
