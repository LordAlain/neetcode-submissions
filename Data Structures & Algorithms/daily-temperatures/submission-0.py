class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        length = len(temperatures)
        result = [0] * length
        
        for l, val in enumerate(temperatures):
            r = l + 1
            result[l] = 0
            while r < length:
                if val < temperatures[r]:
                    result[l] = r - l
                    break
                else:
                    r += 1
        
        return result