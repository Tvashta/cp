from collections import defaultdict
def long(s,k,start,end):
        f=defaultdict(lambda: 0)
        for i in range(start,end):
            f[s[i]]+=1
        for i in range(start,end):
            if f[s[i]]<k:
                return max(long(s,k,start,i),long(s,k,i+1,end))
        return end-start

def longestSubstring(self, s: str, k: int) -> int:
    return long(s,k,0,len(s))
        