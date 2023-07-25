def sum_lists(arr, n):
    result = []
    for slist in arr:
        slist_sum = sum(slist)
        if slist_sum >= n:
            result.append(slist)
    return result


arr_1 = [[1, 0, 0], [1, 2, 0], [0, 1, 1], [2, 3, 4], [1, 1, 1], [0, 0, 0]]
n1 = 3

res = sum_lists(arr_1, n1)
print(res)
