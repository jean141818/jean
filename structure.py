def same_structure_as(arr1, arr2):
    if isinstance(arr1, list) and isinstance(arr2, list):
        if len(arr1) != len(arr2):
            return False
        for sub_arr1, sub_arr2 in zip(arr1, arr2):
            if not same_structure_as(sub_arr1, sub_arr2):
                return False
        return True
    else:
        return not isinstance(arr1, list) and not isinstance(arr2, list)


print(same_structure_as([ 1, 1, 1 ], [ 2, 2, 2 ] ))