class Solution:    
    def findUnion(self, a, b):
        # code here
        c=set(a)
        d=set(b)
        e=c.union(b)
        return(len(e))
