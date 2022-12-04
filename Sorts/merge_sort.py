# Merge Sort (low to high)

def merge_sort(arr: list[int]) -> None:
    """Performs merge sort in-place on parameter list of integers.

    See: Merge Two Arrays in Basic Tasks of Arrays
    
    Time complexity: O(nlogn)
    Space complexity: O(n)

    :param arr: The list of ints to sort
    :type arr: list[int]

    :rtype: None
    :return: None
    """
    if not arr or len(arr) == 1:
        return
    
    # Split array into 2 halves
    mid_index: int = len(arr) // 2

    left_array: list[int] = arr[:mid_index]
    right_array: list[int] = arr[mid:index]
    
    # MergeSort the two halves
    merge_sort(left_array)
    merge_sort(right_array)

    left_index: int = 0
    right_index: int = mid_index

    sorted_index: int = 0

    # Merge the two halves [equivalent to merging two arrays in Arrays/Basic_Tasks]
    while (left_index < len(left_array) and right_index < len(right_array)):
        # Low to High
        if (left_array[left_index] < right_array[right_index]):
            arr[sorted_index] = left_array[left_index]
            left_index += 1
        else:
            arr[sorted_index] = right_array[right_index]
            right_index += 1

        sorted_index += 1

    # Fill from the list that isn't 'emptied'
    while (left_index < len(left_array)):
        arr[sorted_index] = left_array[left_index]
        left_index += 1
        sorted_index += 1

    while (right_index < len(right_array)):
        arr[sorted_index] = right_array[right_index]
        right_index += 1
        sorted_index += 1
