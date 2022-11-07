# Selection Sort (low to high)

def selection_sort(arr: list[int]) -> None:
    """Performs selection sort in-place on parameter list of integers.
    
    Time complexity: O(n^2) [worst/avg]; O(n^2) [best]
    Space complexity: O(1)

    :param arr: The list of ints to sort
    :type arr: list[int]

    :rtype: None
    :return: None
    """

    # only (n-1) traversals are neccesary; on last traversal, last index will automatically
    # hold the largest integer in the array
    # each traversal increases the size of the sorted portion [0, i] by 1
    for i in range(0, len(arr) - 1):
        # find the index of the smallest element in the unsorted portion of the array
        smallest_element_index: int = i
        
        for j in range (i + 1, len(arr)):
            if (arr[j] < arr[smallest_element_index]):
                smallest_element_index = j
        
        # swap: place the smallest unsorted element into i, increasing the size of the sorted portion by 1
        temp: int = arr[smallest_element_index]
        arr[smallest_element_index] = arr[i]
        arr[i] = temp