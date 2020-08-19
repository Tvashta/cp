# Count Inversions
## Question
Given an array an inversion is a pair of numbers such that the greater number occurs before the smaller one. Count the total inversions in the array.

#### Input: 
8 4 2 1
#### Output: 
6
Pairs are:
    1. 8,4
    2. 8,2
    3. 8,1
    4. 4,2
    5. 4,1
    6. 2,1

## Logic
The naive solution would be to traverse all pairs and count the inversions. That would give us a time complexity of O(n^2).
If we split our array into 2, we will have to traverse each of those and count the pairs in (N^2)/2 and then once merged, check for pairs in O(n). So our complexity reduces when we divide the array. Following that logic, if we keep on dividing the array as in Merge Sort at some random step, say our left and right arrays are l and r. When we perform the Merge Operation, we will check if l[i]< r[j] for some i,j. If r[j] < l[i], we have an inversion. But since our left and right arrays are sorted, if l[i] > r[j], every element in l after index i would also be greater than r[j]. In this way our inversion count can be found in O(nlogn).

## Code
C++ code is given as the Euron Problem