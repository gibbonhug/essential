# Bubble Sort (low to high) [unoptimized]
# Time complexity: O(n^2) [worst/avg]; O(n) [best: arr already sorted]
# Space complexity: 

def bubble_sort(arr: list[int]) -> None:
    """Performs bubble sort in-place on parameter list of integers.
    
    :param arr: The list of ints to sort
    :type arr: list[int]

    :rtype: None
    :return: None
    """

    bubbling_num: int

    for i in range(0, len(arr) - 1):
        for j in range(0, i):
            if (arr[j] > arr[j+1]):
                # swap arr[j] and arr[j+1], remembering larger num
                bubbling_num = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = bubbling_num