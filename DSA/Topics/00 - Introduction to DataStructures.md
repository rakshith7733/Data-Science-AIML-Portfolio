### Data Structures & Algorithms [DSA]

##### What is Datastructures?

- The different ways of organizing, processing, storing and retrieving data in computer memory, which that can be used efficiently.

###### Example:
- When we fold the clothes we bring them as a bunch and dump them in cupboard, and later when we need any item it is hard to pick suppose black shirt it would be difficuilt from the bunch, as we need to check one by one. But, if our clothes are categorised then we can go directly to that section and pick the one we required this would cause less time and efforts.

##### What is an Algorithms?
- A step-by-step of rules/instructions to solve a problem or a task.

    - Ex:1 Step-by-step procedure

    > Check the occasion
    > Check the dress category
    > Look for suitable combination
    > Select the best outfit
    > Wear it.

    Ex:2
    Cooking a dish (procedures and steps followed)


```
<!> Data Structures : How data is organized
<!> Algorithms: How we use the data to solve a problem
```
##### Why Data structures and Algorithms are important?

- Taking a library management if the library is not organized it would be difficult to find the book you need and it might take huge time and efforts.
- But if the library is organized then we can directly go to specified section and choose the book we want.
- Here, books are the data, Section/Selves are the Data Structures and "Process of finding the book: is the algorithm.


Using Data Structures it make the computer to choose less memory more efficiently and accurately.

```
Data Structures and Algorithms are important because they help organize data efficiently and process it effectively. Data structures determine how data is stored, while Algorithms determine how operations are performed on that data. Together they help reduce execution time, optimize memory usage, and improve the overall performance of software applications.
```

##### Types of Data Structures:

- The Data structures are classififed into Primtive and Non-Primitive


###### Primitive:
- These are basic data types which cannot be broken down into smaller/simpler datatypes.
- They have fix size
- The data is stored in memory.

Ex: Int, Float, Bool, Char, String

###### Non-Primitive:
- These can be broken into smaller datatypes
- Larger in size can grow dynamically.
- The data is stored with references with pointer in different memory locations.


These are sub divided into two types:

1. Linear: The way in which data is stored in sequential order and each element is connected to its adjacent element, order of them is important.

Ex: List, Tuple, Array, Linked List, Stack, Queue.

2. Non-Linear: The way in which data is stored in Non-sequential way and hierarchical manner where one element is connected to one or more element.

Ex: Sets, Dictionary, Graphs, Tree


##### Types of Algorithms:


1. Searching Algorithms: Used to find an element in a collection of data.

        1.1. Linear Search:
            - Checks each element one by one
            - works on unsorted data

        1.2. Binary Search:
            - Works only on sorted data
            - Repeatedly divides the search space into half.
      
2. Sorting Algorithms: Used to arrange data in a specific order.

        2.1. Bubble Sort:
            - Compares adjacent elements and swaps them
            - Easy to understand but slow
        2.2. Selection Sort:
            - Repeatedly selects minimum elements
        2.3. Insertion Sort:
            - Inserts elements into their correct position
        2.4. Merge Sort:
            - Divide and conquer algorithm
            - Efficient and stable
        2.5. Heap Sort:
            - Uses Heap data structures
        2.6. Quick Sort:
            - Uses pivot element
            - very fast in practice

3. Divide and Conquer Algorithms: Break a large problem into smaller sub-problem.

        Ex: Merge Sort, Quick Sort, Binary search

        Workflow: Divde >> solve >> combine

4. Recursion: An Algorithm that calls itself until a base condition is met.

>> Ex: Factorial, Fibonacci series, Tree Traversal

5. Dynamic Programming (DP): Used when the same sub-problem occurs multiple times.

        Idea: Store previously calculated results.
            Avoid repeated calculations

        Ex: Fibonacci
            Knapsack problem
            Longest common subsequence

        Real world usecases:
        - Route Optimization
        - Resource planning
        - stock market analysis

6. Greedy Algorithms: Makes the best choice at each step hoping for global optimum.

        Ex:
        - Dijkstra's Algorithm
        - Huffman Coding
        - Activity Selection

        Real world usecases:
        - Network routing
        - Data compression
        - Scheduling tasks

7. Backtracking Algorithms: Try a solution and it it fails, go back and try another.

        Ex:
        - Suduko solver
        - N-Queen problem
        - Maze solving

        Real world usaecases:
        - Puzzle solving
        - constraint satisfaction problems

8. Graph Algorithms: Used when data is represented as nodes and connections

        Ex:
        Breadth First Search (BFS)
        - Visits nodes level by level.
        - uses Queue.

        Depth First Search (DFS)
        - Goes deep first
        - Uses stack or Recursion.

        Dijkstra's Algorithm
        - Finds shortest path

        Floyd-Warshall
        - Finds shortest path among all nodes.

        Real world usecases:
        - Google Maps
        - Social networks
        - Flight routes.

9. Tree Algorithm: used on Hierarchiecal data

        Ex:
        Tree Traversal
            - In Order
            - Pre Order
            - Post Order
        - BST Search
        - AVL Tree Operations

        Real world usecases:
        - File Systems
        - Organization Hierarchy
        - Database Indexing

10. String Algorithm: Used to process text

        Ex:
        - KMP (Knuth-Morris-Pratt)
        - Rabin-Karp
        - Boyer-Moore

        Real world usecases:
        - Search Engines
        - Text Editors
        - DNA Sequence Matching

11. Hashing Algorithms: Converts data into key-value pairs for fast lookups.

        Ex:
        - Hash Table
        - Hash Map
        - Dictionary

        Real world usecases:
        - Caching
        - Database indexing
        - Password Storage


