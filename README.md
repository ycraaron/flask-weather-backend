
#### Complete the following function definition. The function takes 2 arguments:

```sh
`x`, a list of numeric intervals, expressed as 2-tuples
`y`, a single number interval, expresses as a 2-tuple
The function returns a new list with `y` merged into `x`, collapsing any overlapping intervals.
```

#### Example 1:

```sh
>>> x = [(1, 3), (8, 11), (19, 25)]
>>> y = (5, 7)
>>> new_intervals = merge_interval(x, y)
>>> print(new_intervals)
[(1, 3), (5, 7), (8, 11), (19, 25)]
```

#### Implementation

- pseudocode(tail recursion implementation)

```sh
    def func merge(list_interval, interval):
        new_list_interval = []
        1) append interval to list_interval if interval exists
        2) foreach interval in list_interval:
              foreach remaining_interval in list_interval exclude interval:
                  if intersection(interval, remaining_interval):
                      add merge(interval, remaining_interval) to new_list_interval
                  else:
                      pass
           if merge_finish:
               return new_list_interval
           else:
               merge(new_list_interval)
```
