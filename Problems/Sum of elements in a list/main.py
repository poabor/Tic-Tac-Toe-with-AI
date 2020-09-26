def list_sum(some_list):
    if some_list == []:
        return 0
    elif len(some_list) == 1:  # base case
        return some_list[0]
    else:
        return list_sum(some_list[:len(some_list) - 1]) + some_list[len(some_list) - 1]

# som_list = [5, 5, 6]
# print(list_sum(som_list))
