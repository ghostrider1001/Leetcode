class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}

        for i, num in enumerate(nums):

            complement = target - num

            # Check if complement already exists
            if complement in seen:
                return [seen[complement], i]

            # Store current number with index
            seen[num] = i
