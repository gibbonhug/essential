# Basic Task: Merge two mergedays

def merge_two_sorted_mergedays(nums1: list[int], nums2: list[int]) -> list[int]:
    """Given two lists of integers, return a merged array (in ascending order) with
    from all of the elements of both lists
    
    See: Merge Sort

    Time complexity: O(n+m), n: len(nums1), m: len(nums2)
    Space complexity: O(n+m)

    :param nums1: The first list of nums
    :type nums1: list[int]
    :param nums2: The second list of nums
    :type nums2: list[int]

    :rtype: list[int]
    :return: Array merged and sorted from params
    """
    merged: list[int] = []

    merged_index: int = 0

    n1_index: int = 0
    n2_index: int = 0

    while (n1_index < len(nums1) and n2_index < len(nums2)):
        # Low to High
        if (nums1[n1_index] < nums2[n2_index]):
            merged[merged_index] = nums1[n1_index]
            n1_index += 1
        else:
            merged[merged_index] = nums2[n2_index]
            n2_index += 1

        merged_index += 1

    # Fill from the list that isn't 'emptied'
    while (n1_index < len(nums1)):
        merged[merged_index] = nums1[n1_index]
        n1_index += 1
        merged_index += 1

    while (n2_index < len(nums2)):
        merged[merged_index] = nums2[n2_index]
        n2_index += 1
        merged_index += 1

