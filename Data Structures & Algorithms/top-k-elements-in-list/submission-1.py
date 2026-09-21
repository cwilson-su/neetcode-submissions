from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # This replaces your entire first loop
        seen = Counter(nums) 
        
        # This replaces your second loop. 
        # It returns a list of tuples like [(num, frequency), ...]
        top_k_tuples = seen.most_common(k)
        
        # Extract just the numbers from the tuples
        output = []
        for num, freq in top_k_tuples:
            output.append(num)
            
        return output
