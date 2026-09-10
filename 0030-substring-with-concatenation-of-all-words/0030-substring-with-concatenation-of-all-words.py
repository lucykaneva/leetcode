class Solution(object):
    

    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        answer=[]
        lengthOfOneWord = len(words[0])
        lengthOfPermutation = lengthOfOneWord*len(words)
        word_counts = Counter(words)
        for i in range(0, lengthOfOneWord):
            right = i
            left = i
            seen_counts = {}
            while right < len(s): 
                word_slice = s[right:right+lengthOfOneWord]
                right+=lengthOfOneWord
                if word_slice in word_counts:
                    seen_counts[word_slice] = seen_counts.get(word_slice, 0) + 1
                    while seen_counts[word_slice]>word_counts[word_slice]:
                        left_word = s[left:left+lengthOfOneWord]
                        seen_counts[left_word]-=1
                        left += lengthOfOneWord
                    if right - left == lengthOfPermutation:
                            answer.append(left)
                else:
                    left=right
                    seen_counts.clear()

        return answer


    

        