// should move cur then set true!, learn sth!!!

class TNode 
{
public:
    bool isWord{};
    TNode* nl[26]{};
};

class Trie {
public:
    TNode* root = new TNode();
    
    /** Initialize your data structure here. */
    Trie() {
        
    }
    
    /** Inserts a word into the trie. */
    void insert(string word) {
        TNode* curn = root;
        for (auto i=0; i<word.size(); ++i)
        {
            char& c = word[i];
            if (!curn->nl[c-97])
                curn->nl[c-97] = new TNode();
            curn = curn->nl[c-97];
            if (i == word.size()-1)
                curn->isWord = true;
        }
    }
    
    /** Returns if the word is in the trie. */
    bool search(string word) {
        TNode* curn = root;
        for (auto i=0; i<word.size(); ++i)
        {
            auto& c = word[i];
            if (!curn->nl[c-97])
                return false;
            curn = curn->nl[c-97];
            if (i == word.size()-1)
                if (curn->isWord)
                    return true;
                else
                    return false;
        }
    }
    
    /** Returns if there is any word in the trie that starts with the given prefix. */
    bool startsWith(string prefix) {
        TNode* curn = root;
        for (auto& c : prefix)
        {
            if (!curn->nl[c-97])
                return false;
            curn = curn->nl[c-97];
        }
        return true;
    }
};

/**
 * Your Trie object will be instantiated and called as such:
 * Trie obj = new Trie();
 * obj.insert(word);
 * bool param_2 = obj.search(word);
 * bool param_3 = obj.startsWith(prefix);
 */