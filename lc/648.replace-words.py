class Solution:
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
       	ls = sentence.split(' ');
        trie = {}
        for root in dict:
            cur = trie            
            for c in root:
                if c not in cur:
                    cur[c] = {}
                cur = cur[c]
            cur["isWord"] = 1
            
        print(trie) 
        
        for w in sentence:
                        
for c in w:
                            


