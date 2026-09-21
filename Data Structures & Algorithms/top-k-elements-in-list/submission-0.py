class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen={}
        for n in nums:
            if n in seen:
                seen[n]+=1
            else:
                seen[n]=1
        
        output=[]
        for i in range(0,k):
            # temp_max=max(seen.values()) # max value
            temp_max=max(seen, key=seen.get) # key corresponding to max value
            output.append(temp_max)
            seen.pop(temp_max)

        return output


