# Insertion Sort (low to high)

def insertion_sort(arr: list[int]) -> None:
    """Performs insertion sort in-place on parameter list of integers.
    
    Time complexity: O(n^2) [worst/avg]; O(n) [best; list already sorted]
    Space complexity: O(1)

    :param arr: The list of ints to sort
    :type arr: list[int]

    :rtype: None
    :return: None
    """

    current_elem: int
    dest_index: int

    # indices below current 'i' are already sorted (lo->hi). Each traversal will
    # insert the current_elem from 'i' into its correct spot in the sorted portion, expanding the
    # sorted size of the sorted portion by 1
    # (element at 0 at first traversal can be considered already sorted, and sorted portion can
    # be considered to be of size 1)
    for i in range(1, len(arr)):
        current_elem = arr[i] 
        dest_index = i

        while ((dest_index > 0) and (arr[dest_index - 1]) > current_elem):
            # shuffle elements greater than current_elem we are sorting up a spot
            arr[dest_index] = arr[dest_index - 1]
            dest_index -= 1
        
        # place this element in correct place in sorted portion
        arr[dest_index] = current_elem