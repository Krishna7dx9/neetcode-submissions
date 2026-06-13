class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        seen = {}

        for i in range(n):
            complementary = target - nums[i]
            
            if complementary in seen:
                return [seen[complementary], i]

            seen[nums[i]] = i