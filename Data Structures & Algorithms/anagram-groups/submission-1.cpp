class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, int> seen;
        int lookup_index = 0;
        vector<vector<string>> output;
        
        for (int i = 0; i < strs.size(); i++) {
            string sorted_word = strs[i];
            
            sort(sorted_word.begin(), sorted_word.end());
            
            if (!seen.count(sorted_word)) {
                output.push_back({strs[i]}); // push_back instead of append
                seen[sorted_word] = lookup_index;
                lookup_index += 1;
            } else {
                int insert_sublist_index = seen[sorted_word]; // [] instead of get()
                output[insert_sublist_index].push_back(strs[i]); 
            }
        }
        
        return output;
    }
};
