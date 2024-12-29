# Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.


class Solution:
    def uniqueOccurrences(self, arr) -> bool:
        count = {}
        for i in arr:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
        return len(count.values()) == len(set(count.values()))


solution = Solution()
print(solution.uniqueOccurrences([-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]))  # True
print(solution.uniqueOccurrences([1, 2]))  # False
