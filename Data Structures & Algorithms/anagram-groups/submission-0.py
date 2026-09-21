class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen=set()
        output=[]
        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word not in seen:
                seen.add(sorted_word)
                output.append([word])
            else:
                for l in output:
                    for w in l:
                        sorted_w = ''.join(sorted(w))
                        if sorted_w == sorted_word:
                            l.append(word)
                            break           
            
        return output

