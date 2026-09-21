class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, num in enumerate(nums): # enumerate being a function splitting each element of the array into its position and value
            complement = target - num

            if complement in seen:
                return [seen[complement], i] # [] used to create a list in pyhton

            seen[num] = i


