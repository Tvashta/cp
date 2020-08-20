# Constant Range Updations in an Array

## Question

Given an array and Q queries [l,r,k], add k to the array elements in the range l to r and finally display the array.

## Logic

Naive method would take linear time for each query, but using prefix array can process each query in constant time.
First convert the array to prefix sum array. Now for each query add that value to index l and subtract it from index r+1. Finally constructing a prefix array from this will give our answer. It is amazing how this works. Basically, when we add that value to l, in a prefix array all elements after l also get updated with value. But the subtraction at r+1, neutralizes this effect for every element out of the range. Pretty nifty!

## Code

```python3
def prefix(a):
    for i in range(1,len(a)):
        a[i]+=a[i-1]

def add(a,l,r,v):
    a[l]+=v
    if r<n-1:
        a[r]+1-=v
```
