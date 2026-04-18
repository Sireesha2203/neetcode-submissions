class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        for i in range(len(numbers)):
            d=target-numbers[i]
            if d in numbers and numbers.index(d)!=i :
                return [i+1,numbers.index(d)+1]
            
