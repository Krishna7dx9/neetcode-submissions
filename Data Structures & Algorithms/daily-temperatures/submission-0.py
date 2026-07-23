class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        result = [0] * len(temperatures)
        unresolved = []

        for right in range(len(temperatures)):

            while len(unresolved) > 0 and unresolved[-1][0] < temperatures[right]:
                temp, left = unresolved.pop()
                result[left] = right - left 

            unresolved.append((temperatures[right], right))

        return result