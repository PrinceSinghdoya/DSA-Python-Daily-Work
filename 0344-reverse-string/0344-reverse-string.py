class Solution(object):
    def reverseString(self, s):

        def rev(l,r):
            if l<r:
                s[l],s[r]=s[r],s[l]
                rev(l+1,r-1)
        rev(0,len(s)-1)

        