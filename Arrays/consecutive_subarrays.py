def consecutive_subarrays_by_element_flat(arr: List[int]) -> List[int]:
    """Return a list containing every consecutive subarray of parameter list, ordered by the first element in the subarray.
    Example: arr = [0, 1, 2]; its consecutive subarrays are [0], [0, 1], [0, 1, 2], [1], [1, 2], [2]
    This function would return [[0], [0, 1], [0, 1, 2], [1], [1, 2], [2]]

    :param arr: The list of ints to find consecutive subarrays from
    :type arr: List[int]

    :rtype: List[int]
    :return: A flat list containing all consecutive subarrays, ordered by the first element in the subarray
    """
    list_of_lists = []

    # 'i' will determine the first element of this subarray
    # (first iteration will check subarrays starting at 0th element, then 1st, etc)
    for i in range(0, len(arr)):
        values_from_here: List[int] = []
        # 'j' will determine the length of this subarray
        # (first iteration will give length of 1, then 2, etc)
        for j in range(0, len(arr) - i):
            this_subarray: List[int] = values_from_here[:] # copy by value not reference

            this_subarray.append(arr[j+i])
            list_of_lists.append(this_subarray)

            values_from_here.append(arr[j+i])
    
    return list_of_lists

def consecutive_subarrays_by_element_structured(arr: List[int]) -> List[int]:
    """Return a list containing every consecutive subarray of parameter list, ordered by the first element in the subarray.
    Example: arr = [0, 1, 2]; its consecutive subarrays are [0], [0, 1], [0, 1, 2], [1], [1, 2], [2]
    This function would return [[[0], [0, 1], [0, 1, 2]], [[1], [1, 2]], [[2]]]

    :param arr: The list of ints to find consecutive subarrays from
    :type arr: List[int]

    :rtype: List[int]
    :return: A nonflat list containing sublists of consecutive subarrays that begin with the same element.
    """
    list_of_lists = []

    # 'i' will determine the first element of this subarray
    # (first iteration will check subarrays starting at 0th element, then 1st, etc)
    for i in range(0, len(arr)):
        subarrays_starting_here: List[int] = []
        # 'j' will determine the length of this subarray
        # (first iteration will give length of 1, then 2, etc)
        for j in range(0, len(arr) - i):
            this_subarray: List[int] = []
            # get the last subarray from this starting element to add onto
            if (subarrays_starting_here): # on the first iteration subarrays_starting_here is empty
                this_subarray = subarrays_starting_here[-1]
                
            this_subarray.append(arr[j+i])
            list_of_lists.append(this_subarray)

            subarrays_starting_here.append(this_subarray)

    return list_of_lists