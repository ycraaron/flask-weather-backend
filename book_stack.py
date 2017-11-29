import random


# use sorted list to improve the performance
def tallest_tower(book_dimension_list):
    dic_layer_length = {}
    dic_layer_width = {}
    for key in list(set([book[0] for book in book_dimension_list])):
        if key not in dic_layer_length.keys():
            dic_layer_length[key] = []

    for key in list(set([book[1] for book in book_dimension_list])):
        if key not in dic_layer_width.keys():
            dic_layer_width[key] = []

    dic_layer_length, dic_layer_width = build_sorted_layer_hash(dic_layer_length, dic_layer_width, book_dimension_list)

    ls_layer_length = sorted(dic_layer_length.keys(), reverse=True)
    ls_layer_width = sorted(dic_layer_width.keys(), reverse=True)

    # print('------------------------------------------------------------------')
    #
    # print('length->width hash: ', dic_layer_length)
    # print('width->length hash: ', dic_layer_width)
    #
    # print('------------------------------------------------------------------')
    #
    # print('sorted possible layer length: ', ls_layer_length)
    # print('sorted possible layer width: ', ls_layer_width)
    #
    # print('------------------------------------------------------------------')

    stack1 = build_all_stack_by_layer(ls_layer_length, ls_layer_width, dic_layer_length)
    stack2 = build_all_stack_by_layer(ls_layer_width, ls_layer_length, dic_layer_width)

    if len(stack1) > len(stack2):
        return stack1
    elif len(stack1) == len(stack2):
        for i in range(len(stack2)):
            stack2[i][0], stack2[i][1] = stack2[i][1], stack2[i][0]
        print('2 stacks found:')
        print(stack1)
        print(stack2)
        return stack1
    else:
        for i in range(len(stack2)):
            stack2[i][0], stack2[i][1] = stack2[i][1], stack2[i][0]
        return stack2


def build_sorted_layer_hash(dic_layer_length, dic_layer_width, book_list):
    for book in book_list:
        dic_layer_length[book[0]].append(book[1])
        dic_layer_width[book[1]].append(book[0])
    for key in dic_layer_length:
        dic_layer_length[key].sort(reverse=True)
    for key in dic_layer_width:
        dic_layer_width[key].sort(reverse=True)
    return dic_layer_length, dic_layer_width


def build_all_stack_by_layer(ls_layer_edge_1, ls_layer_edge_2, dic_possible_layer_edge_2):
    ls_all_book_stacks = []

    # for optimization
    absolute_max_layer = []

    current_max_layer = 0
    for i in range(len(ls_layer_edge_1)):
        theoretical_max_layer = len(ls_layer_edge_1) + 1 - i
        book_stack = build_stack_from_layer(ls_layer_edge_1[i:], ls_layer_edge_2, dic_possible_layer_edge_2)
        if len(book_stack) == theoretical_max_layer:
            absolute_max_layer = book_stack
            break
        elif len(book_stack) > current_max_layer:
            current_max_layer = len(book_stack)
            ls_all_book_stacks.clear()
            ls_all_book_stacks.append(book_stack)
        elif len(book_stack) == current_max_layer:
            ls_all_book_stacks.append(book_stack)

    # use absolute max layer can reduce the search times
    if absolute_max_layer:
        return absolute_max_layer
    else:
        if len(ls_all_book_stacks) > 1:
            print('multiple found', ls_all_book_stacks)
            random.shuffle(ls_all_book_stacks)
            return ls_all_book_stacks[0]
        else:
            return ls_all_book_stacks[0]


def build_stack_from_layer(ls_layer_edge_1, ls_layer_edge_2, dic_possible_layer_edge_2):
    """
    :param ls_layer_edge_1: sorted possible layer length/width
    :param ls_layer_edge_2: sorted possible layer width/length
    :param dic_possible_layer_edge_2: hash for storing the length/width corresponding to edges in ls_layer_edge_1
    :return:
    """
    book_stack = []
    # print('---------------------')
    # print('start to build book stack from layer edge1:', ls_layer_edge_1[0])
    # print('all possible layer edge1:', ls_layer_edge_1)
    for edge_1 in ls_layer_edge_1:
        # it is a sorted list
        ls_possible_edge_2 = dic_possible_layer_edge_2[edge_1]
        # print('possible edge2 for this layer edge 1', ls_possible_edge_2)
        # loop through the possible edge 2 list
        for i in range(len(ls_possible_edge_2)):
            possible_edge_2 = ls_possible_edge_2[i]
            # if a stack layer is built
            # print('current layer edge_2 list', ls_layer_edge_2)
            if possible_edge_2 in ls_layer_edge_2:
                edge_2_is_found = True
                # print('stack layer found', [edge_1, possible_edge_2], 'for', book_stack)
                book_stack.append([edge_1, possible_edge_2])
                # remove the edges which are larger than edge 2 in ls_layer_edge_2
                ls_layer_edge_2 = update_sorted_hash_edge(ls_layer_edge_2, possible_edge_2)
                # edge_2 was found for edge_1
                # should stop searching edge_2 for edge1
                if edge_2_is_found:
                    # print('edge2 for edge1 is found, stop searching for edge1', edge_1)
                    break
            # if edge_2 is not in edge_2_layer list, skip this possible edge 2 and do nothing
            else:
                # print(possible_edge_2, ' is not valid for', book_stack)
                pass
        # print('finish build stack for:', edge_1)
        # print(book_stack)
        # print('---------------------')
    return book_stack


def update_sorted_hash_edge(ls_sorted_hash_edge, removed_edge_length):
    split_index = 0
    for i in range(len(ls_sorted_hash_edge)):
        length = ls_sorted_hash_edge[i]
        if length == removed_edge_length:
            split_index = i
    ls_layer_width = ls_sorted_hash_edge[split_index + 1:]

    return ls_layer_width

if __name__ == '__main__':

    ls_book = [[14, 9], [11, 9], [11, 12], [3, 4], [15, 10]]
    stack = tallest_tower(ls_book)
    print('************************************')
    print('result: {}'.format(stack))
    print('************************************')

    ls_book = [[14, 9], [11, 9], [11, 12], [3, 4], [15, 10], [17, 11]]
    stack = tallest_tower(ls_book)
    print('************************************')
    print('result: {}'.format(stack))
    print('************************************')

    ls_book = [[14, 9], [11, 9], [11, 12], [3, 4], [15, 10], [17, 10], [1, 2], [15, 111], [1111, 2]]
    stack = tallest_tower(ls_book)
    print('************************************')
    print('result: {}'.format(stack))
    print('************************************')
