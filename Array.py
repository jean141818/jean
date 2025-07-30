def snail(array):
    snail_elements = []
    
    while array:
        # Append the first row in the array to the snail_elements list
        snail_elements.extend(array.pop(0))
        print(snail_elements)
        if array and array[0]:
            # Append the last element of each remaining row to the snail_elements list
            for row in array:
                snail_elements.append(row.pop())
        print(snail_elements)   
        if array:
            # Append the last row in reverse order to the snail_elements list
            snail_elements.extend(array.pop()[::-1])
        print(snail_elements)
        print(array)
        if array and array[0]:
            # Append the first element of each remaining row in reverse order to the snail_elements list
            for row in array[::-1]:
                snail_elements.append(row.pop(0))
        print(snail_elements)
    return snail_elements

array = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(snail(array))