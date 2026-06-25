class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        while left < right:
            current = numbers[left] + numbers[right]
            if current == target:
                return [left + 1, right + 1]
            elif current < target:
                left += 1
            else:
                right -= 1
        return []


# numbers = [2, 7, 11, 15], target = 9
# left=0, right=3 -> 2 + 15 = 17 -> too big   -> right becomes 2
# left=0, right=2 -> 2 + 11 = 13 -> too big   -> right becomes 1
# left=0, right=1 -> 2 + 7  = 9  -> match     -> return [1, 2]