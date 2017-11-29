#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Complete the following function definition. The function takes 2 arguments:
# - `x`, a list of numeric intervals, expressed as 2-tuples
# - `y`, a single number interval, expresses as a 2-tuple
#
# The function returns a new list with `y` merged into `x`, collapsing any
# overlapping intervals.
#
# You may use all of the CPython 3 standard library.
#
# Example 1:
# >>> x = [(1, 3), (8, 11), (19, 25)]
# >>> y = (5, 7)
# >>> new_intervals = merge_interval(x, y)
# >>> print(new_intervals)
# [(1, 3), (5, 7), (8, 11), (19, 25)]
#
# Example 2:
# >>> x = [(1, 3), (8, 11), (19, 25)]
# >>> y = (3, 5)
# >>> new_intervals = merge_interval(x, y)
# >>> print(new_intervals)
# [(1, 5), (8, 11), (19, 25)]
#
# Example 3:
# >>> x = [(1, 3), (8, 11), (19, 25)]
# >>> y = (9, 21)
# >>> new_intervals = merge_interval(x, y)
# >>> print(new_intervals)
# [(1, 3), (8, 25)]
#
# Example 4:
# >>> x = [(4, 7), (10, 11), (14, 16)]
# >>> y = (9, 15)
# >>> new_intervals = merge_interval(x, y)
# >>> print(new_intervals)
# [(4, 7), (9, 16)]


"""
    def func merge:
        for interval in ls:
            for remaining_interval in ls:
                if intersection():
                    merge()
                else:
                    pass
        if merge_finish:
            return
        else:
            merge
"""


def has_intersection(interval1, interval2):
    start1, end1 = interval1
    start2, end2 = interval2
    if start2 > end1:
        return False
    if start1 > end2:
        return False
    return True


def merge_interval_pair(interval1, interval2):
    start1, end1 = interval1
    start2, end2 = interval2
    new_start = min(start1, start2)
    new_end = max(end1, end2)
    return [new_start, new_end]


def sort_merged_interval(ls_new_interval):
    ls_num = []
    ls_tup = []
    for interval in ls_new_interval:
        for num in interval:
            ls_num.append(num)
    num_pair = int(len(ls_num) / 2)
    ls_num.sort()
    for i in range(0, num_pair):
        new_tup = tuple([ls_num[2*i], ls_num[2*i+1]])
        ls_tup.append(new_tup)
    return ls_tup


from time import sleep


def merge_interval(ls_interval, tup_new_interval=None):
    """

    :param ls_interval: a list of tuples
    :param tup_new_interval: a tuple
    :return: list of tuple after merging y to x
    """

    ls_interval = [list(tup) for tup in ls_interval]
    if tup_new_interval is not None:
        ls_interval.append(list(tup_new_interval))
    ls_new_interval = []
    # print('interval to be merged', ls_interval)
    merge_occur_during_whole_process = False
    last_interval_is_merged = False
    for i in range(0, len(ls_interval)):
        interval = ls_interval[i]
        current_interval_is_merged = False
        # print('current interval', interval)
        # sleep(1)
        if i + 1 < len(ls_interval):
            for j in range(i + 1, len(ls_interval)):
                interval_2 = ls_interval[j]
                if has_intersection(interval, interval_2):
                    # print('has intersection', interval, interval_2)
                    current_interval_is_merged = True
                    if not merge_occur_during_whole_process:
                        merge_occur_during_whole_process = True
                    if j == len(ls_interval) - 1 and not last_interval_is_merged:
                        last_interval_is_merged = True
                    ls_new_interval.append(merge_interval_pair(interval, interval_2))
                    # print('new ls interval', ls_new_interval)
                else:
                    # print('do not has intersection', interval, interval_2)
                    pass
            if current_interval_is_merged:
                pass
            else:
                # print('intersection not found for current interval')
                ls_new_interval.append(interval)
        else:
            if last_interval_is_merged:
                pass
                # print('last interval has already been merged, do not add to new interval list')
                # print(ls_interval[-1])
            else:
                # print('this is the last element in the list')
                # print(ls_interval[-1])
                ls_new_interval.append(ls_interval[-1])

    if merge_occur_during_whole_process:
        return merge_interval(ls_new_interval)
    else:
        return sort_merged_interval(ls_new_interval)
    # if merge_tag == 1:
    #     merge_interval(ls_new_interval)
    # else:
    #     print(ls_new_interval)


if __name__ == '__main__':
    x = [(1, 3), (8, 11), (19, 25)]
    y = (5, 7)
    new_intervals = merge_interval(x, y)
    print('x: {}'.format(x))
    print('y: {}'.format(y))
    print('result: {}'.format(new_intervals))
    print(new_intervals)
    assert new_intervals == [(1, 3), (5, 7), (8, 11), (19, 25)]

    x = [(1, 3), (8, 11), (19, 25)]
    y = (3, 5)
    new_intervals = merge_interval(x, y)
    print('x: {}'.format(x))
    print('y: {}'.format(y))
    print('result: {}'.format(new_intervals))
    assert new_intervals == [(1, 5), (8, 11), (19, 25)]

    x = [(1, 3), (8, 11), (19, 25)]
    y = (9, 21)
    new_intervals = merge_interval(x, y)
    print('x: {}'.format(x))
    print('y: {}'.format(y))
    print('result: {}'.format(new_intervals))
    assert new_intervals == [(1, 3), (8, 25)]

    x = [(4, 7), (10, 11), (14, 16)]
    y = (9, 15)
    new_intervals = merge_interval(x, y)
    print('x: {}'.format(x))
    print('y: {}'.format(y))
    print('result: {}'.format(new_intervals))
    assert new_intervals == [(4, 7), (9, 16)]
