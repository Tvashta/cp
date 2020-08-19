# Longest Substring without Repeating Characters
## Logic
A very naive solution would be to traverse all the substrings and check for the ones without repeated characters. That would take a time of O(n^3). We could use a map for visited characters and slide from one window to the other, updating the map when a repeated char occurs in O(n^2). But a better optimization would help us do all of this in linear time. Use a set to hold the latest index of each character. Whenever some character repeats, our substring would start from the next position of the last known index of that character. If we loop through all possible end indices [0,n], update start index on repetition, the length would be end - start +1. Having a variable to keep track of max length throughout would do the trick

## Code
```python3
from collections import defaultdict
def SubsequenceLength(s):
    v=defaultdict(lambda: -1)
    l=0
    st=0
    for i in range(len(s)):
        if v[s[i]]!=-1:
            st=max(st, v[s[i]]+1)
        v[s[i]]=i
        l=max(l,i-st+1)
    return l

```