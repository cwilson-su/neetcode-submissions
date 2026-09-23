class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> anagram_map;
        
        // Group all anagrams directly in the map
        for (int i = 0; i < strs.size(); i++) {
            string sorted_word = strs[i];
            sort(sorted_word.begin(), sorted_word.end());
            
            // This adds the original word to the vector inside the map
            anagram_map[sorted_word].push_back(strs[i]);
        }
        
        // Transfer the grouped vectors from the map to our output
        vector<vector<string>> output;
        for (auto& pair : anagram_map) {
            output.push_back(pair.second); // pair.second is the vector of strings
        }
        
        return output;
    }
};
