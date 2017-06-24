class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split()
        rwords = []
        for i in range(0, len(words)):
            rwords.append(words[i][::-1])
        return " ".join(rwords)
        
