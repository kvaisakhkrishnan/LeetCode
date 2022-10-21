class Solution {
public:
    bool isAnagram(string s, string t) {
        int hash1[26] = {0};
        int hash2[26] = {0};
        int i = 0;
        while (i < s.length())
        {
            int pos = (s[i]-'a')%26;
            hash1[pos]++;
            i+=1;
        }
        i=0;
        while (i < t.length())
        {
            int pos = (t[i]-'a')%26;
            hash2[pos]++;
            i+=1;
        }
        
        for(i = 0; i<26;i++)
        {
            if (hash1[i] != hash2[i])
            {
                return false;
            }
        }
        
        return true;
    }
};