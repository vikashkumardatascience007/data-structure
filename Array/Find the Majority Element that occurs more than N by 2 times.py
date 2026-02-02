from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        n = len(nums)
        
        mp = {}
        
        for num in nums:
            if num in mp:
                mp[num] += 1
            else:
                mp[num] = 1
        
       
        for num, count in mp.items():
            if count > n // 2:
                return num
        
        return -1

if __name__ == "__main__":
    arr = [2, 2, 1, 1, 1, 2, 2]
    
    sol = Solution()
 
    ans = sol.majorityElement(arr)
    
    print("The majority element is:", ans)
