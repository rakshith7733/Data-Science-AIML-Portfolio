#### Time Complexity
- It measures the number of operations performed.

Ex: Looking for shirt in unordered clothes.
- You check one by one.

operations increases linearly
Time complexity = O(n)

#### Space complexity
- It is the amount of the memory that some code used.

Ex:
x = 10, y = 20
z = x+y

only few variables are used.
space complexity = O(1)     # Constant Space.

        One bag pack - o(1)
        one extra bagpack person - o(n)

#### What is Big O?
- Big O is the language and metric we use to describe the efficiency of algorithm.

- *It describes the worst-case growth rate of an algorithm.*

##### O(1) - constant Time  (Fastest)
- No matter how much the size increases, it has to perform only one operation.

Ex: creating a function for square root, it can go upto higer value but the result remain constant in terms of operation of squaring the number.

Ex: 10 >> 100 >> 1000 >> 10000

##### O(log n) - Logarthimic Time (Extremely efficient)
- Every step removes half of the data.

##### O(n) - Linear Time Complexity
- Time complexity grows in direct proportion to the size of the input data. Means if input grows, the number of the operations that is performing is going to grow.
- Need to check every element once.

Ex: looping for n values, if n = 5 it will loop 5 times and n=100 it will loop for 100 times as n increases values increase gradually.

```py
def loop(n):
    for i in range(n):
        print(i)
    
    for j in range(n):
        print(j)
```

Drop Constants is comes into picture if you have the same loop(take above example with J loop) is present with other purpose which is of same O(n). So, n+n=2n; O(2n) but we can drop the constant and consider it as O(n).


O(n log n) - (Efficient for Large datasets)
- Used in Merge Sort, Quick Sort, Heap sort

##### O(n^2) - Quadratic Time (Slow for large datasets)
- Used in  Bubble sort, Selection sort.

```py
def loop(n):
    for i in range(n):
        for j in range(n):
            print(i,j)
```
- In the above code for two loops, for each iteration of first loop loops over the second loop, where first loop is O(n) and second loop is O(n) so we are iterating one over other so it will be n*n = O(n^2)

O(2^n) - Exponential Time (Very slow)

O(n!) - Generating all Permutations (Extremely expensive)

        Complexity Chart
        Excellent: O(1), O(log n)
        Good: O(n)
        Bad: O(n log n)
        Horrible: O(n^2), O(2^n), O(n!)

#### Big O notations:
- This describe how the algorithm behave according to different condition.

They are three types of notations:
1. Best case (Omega)
2. Average case (Theta)
3. Worst case (Omicron)

Ex: Taking a array of 10,

>> If you search for a number like 1 it is selected in first iteration without being looped the array fully so this will be our best case denoted by Omega.

>> If you need to look for 8 then we have to loop the array fully to fetch the value which take more time consuming so this is our worst case denoted by Omicorn.

>> Suppose if we need to look for 3 then it is fetched with few itreation with average time so this is called average case denoted by theta.























