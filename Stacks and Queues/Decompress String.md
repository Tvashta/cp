# Decompress a String
## Question
Given a string with brackets, numbers and characters decompress it to a proper string format, removing all numbers and brackets by multiplying the substring by the number before it.

#### Input: 
3[ab]4[acd]
#### Output: 
abababacdacdacd

## Logic
It can be solved pretty easily using either a stack or recursion. Maintain 2 stacks, one for integers and one for characters. 
Start traversing the string till a closing bracket is reached and pushing the values read into either of the stacks. 
Once a closing bracket is encountered, pop the contents of the character stack till an opening bracket is found and perform the multiplication.
Push the string back to the character stack and repeat till you reach the end of the list.

## Corner cases
* Multiple digit integers
* Not repeated chunks of string
* No openening or closing bracket and just a single string

## Code
```python3
s=list(input())
i=0
op=[]
integer=[]
while i<len(s):
    if s[i].isnumeric():
        c=0
        while s[i].isnumeric():
            c=c*10+int(s[i])
            i+=1
        integer.append(c)
    if s[i]==']':
        t=""
        while len(op)>0 and op[-1]!='[':
            t+=op[-1][::-1]
            op.pop()
        t=t[::-1]
        if len(op)>0 and op[-1]=='[':
            op.pop()
        if len(integer)>0:
            t=t*integer[-1]
            integer.pop()
        op.append(t)
    if s[i]=='[' or s[i].isalpha():
        op.append(s[i])
    
    i+=1
print(''.join(map(str,op)))
```
