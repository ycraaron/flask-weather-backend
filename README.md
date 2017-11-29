
### Problem

You have a bunch of books that you want to stack into a tower, with one book per "level". To ensure maximum stability of the tower, you want each level of the tower to be larger than the one just above it, in both width and length. You also want to keep the book spines on the same side to make the tower look nicer.
Write a function that, given a list of book dimensions, returns a combination of books for the tallest tower in terms of number books, sorted in descending order of size:

### Function prototype:

```sh
def tallest_tower(book_dimension_list):
    tallest_combination = []
    return tallest_combination
```

### Example:
For this list of the width and length of each book:

```sh
[[14, 9], [11, 9], [11, 12], [3, 4], [15, 10]]

[14, 9] is not larger than [11, 9].
[11, 12] is not larger than [11, 9].

The tallest combinations are:
[[15, 10], [14, 9], [3, 4]]
[[15, 10], [11, 9], [3, 4]]
```
### Implementation:
The basic idea is to:
 - Build hash table for all possible layer length and width. If we use the Example data, the hash table will look like:

   ```sh
     [  15,       10  ]
        ^          ^
        |          |
    first edge  second ege
   ```
   hash table for first edge:
   ```sh
   15 ---> 10
   14 ---> 9
   11 ---> 12, 9
   3  ---> 4
   ```
   hask table for second edge:
   ```sh
   12 ---> 11
   10 ---> 15
   9  ---> 14, 11
   4  ---> 3
   ```
   
  - Loop through 2 hash table to find the possible max tower.
  
  - Some optmization has also been implemeted to improve the performance of the algorithm.
  
### Run the code:
  Open terminal -> enter the folder
  ```sh
  $ python3 book_stack.py
  ```
  
  
