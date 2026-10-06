class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        sorted_s = "".join(sorted(s))
        sorted_t = "".join(sorted(t))

        return sorted_s == sorted_t

        # if len(s) != len(t):
        #     return False
            
        # count_s = {}
        # count_t = {}

        # for char in s:
        #     if char in count_s:
        #         count_s[char] += 1
        #     else:
        #         count_s[char] = 1

        # for char in t:
        #     if char in count_t:
        #         count_t[char] += 1
        #     else:
        #         count_t[char] = 1

        # return count_s == count_t