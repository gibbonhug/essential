# Merge Sort (low to high)
# Time complexity: 
# Space complexity:

def merge_sort(arr: list[int], start_index: int = 0, end_index: int = None) -> None:
    """Performs merge sort in-place on parameter list of integers.
    Uses the middle element as the pivot.
    
    :param arr: The list of ints to sort
    :type arr: list[int]

    :rtype: None
    :return: None
    """
    # set default parameter
    if (end_index is None):
        end_index = len(arr) - 1

    # merge sort
    if (start_index >= end_index):
        return

    mid_index: int = start_index + ((end_index - start_index) // 2) # avoid overflow

    merge_sort(arr, start_index, mid_index)
    merge_sort(arr, mid_index + 1, end_index)

    arr = _merge(arr, start_index, end_index)
    

def _merge(arr: list[int], left_start: int, right_end: int) -> list[int]:
    """Merges two portions of a list together, lo->hi, given the starting index of the left portion and the end index of the right portion.
    
    :param arr: The list of ints to merge two halves of
    :type arr: list[int]
    :param left_start: The index on the left portion of arr to begin merging from
    :type left_start: int
    :param arr: The index on the right portion of arr to stop merging at (inclusive range)
    :type right_end: int


    :rtype: list[int]
    :return: A copy of the original list, with the elements from [left_start, right_end] merged together.
    """

    merged_index: int = left_start
    merged_list: list[int] = arr[:] # copy by value not reference

    mid_index: int = left_start + ((right_end - left_start) // 2) # avoid overflow
    left_place: int = left_start # how far into the left portion we have merged
    right_place: int = mid_index + 1 # how far into the right portion we have merged

    while ((left_place <= mid_index) and (right_place <= right_end)):
        if (arr[left_place] < arr[right_place]):
            merged_list[merged_index] = arr[left_place]
            left_place += 1
        else: 
            merged_list[merged_index] = arr[right_place]
            right_place += 1
        
        merged_index += 1
    
    while (left_place <= mid_index):
        merged_list[merged_index] = arr[left_place]
        left_place += 1
        merged_index += 1

    while (right_place <= right_end):
        merged_list[merged_index] = arr[right_place]
        right_place += 1
        merged_index += 1

    return merged_list

my_list = [100, 5, 6, 20, 1]
merge_sort(my_list)
print(my_list)