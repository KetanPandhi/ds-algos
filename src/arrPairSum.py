# better use hash or set here


def arr_sum(arr: list, sum_val: int) -> int:
    """ find number of pairs """
    arr.sort()
    pair_lower_member = []
    for i in arr:
        arr.remove(i)
        if binary_search(arr, sum_val - i):
            if i not in pair_lower_member:
                pair_lower_member.append(i)

    return len(pair_lower_member)


def binary_search(arr: list, search: int) -> bool:
    """ binary search """
    arr_length = len(arr)
    if arr_length > 0:
        halfway = int(arr_length / 2)
        if arr[halfway] == search:
            return True
        elif halfway == 0:
            return False
        elif arr[halfway] > search:
            return binary_search(arr[:halfway], search)
        else:
            return binary_search(arr[halfway:], search)


print(binary_search([1, 2, 3, 4, 5, 7, 7, 8, 8], 1))
