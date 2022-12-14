# Don't think sliding window would optimize problem further but not certain

def consecutive_zero_sum(nums: list[int]) -> int:
    """Given an integer array nums, determine the length of the longest sequence of consecutive ints that sum to zero. If no sequences sum to 0 in nums, return -1

    Examples: 
    [-1, 0, 1, 0, 1] -> 4: the sequence from i=0 to i=3 sums to 0 and is the longest sequence which sums to 0.
    [0, 0, 0] -> 3: The sequence from i=0 to i=2 is the longest sequence which sums to 0.
    [1] -> -1: No sequence in this array sums to 0

    Time complexity: O(n) [iterate thru entire array]
    Space complexity: O(n) [new hashmap]

    :param nums: The list of nums
    :type nums: list[int]

    :rtype: int
    :return: Size of the longest consecutive sequence in nums which sums to 0
    """
    # empty list can't sum to 0
    if not nums:
        return -1

    # two types of consecutive 0 sums: those which start from beginning of list and those which do not.

    cuum_sum: int = nums[0]
    longest_zero_sum_from_beg: int = 1 if cuum_sum == 0 else -1

    seen_sum_map: {int: int} = {}
    longest_zero_sum_from_mid: int = -1

    for i in range(1, len(nums)):
        cuum_sum += nums[i]

        if cuum_sum == 0:
            longest_zero_sum_from_beg = i+1 # 0 indexed array, length will be index +1

        # find consecutive 0 sums which do not start from index 0.
        # (summing between equal numbers in cuum_sum_list: ie from [1, 3, 1] summing from these indices
        # gives a consecutive zero sum of length 3)
        # finding the left repeating number in this way is nearly identical to contains_duplicate also in Arrays/Basic_Tasks.
        else:
            if cuum_sum in seen_sum_map:
                this_length: int = i - seen_sum_map.get(cuum_sum)
                longest_zero_sum_from_mid = max(this_length, longest_zero_sum_from_mid)
            # only adding cuum sum into the map once will eliminate issues of ex. multiple cuum_sums surrounded by same number
            else:
                seen_sum_map[cuum_sum] = i

    # now return the larger of the two sum lengths:
    return max(longest_zero_sum_from_beg, longest_zero_sum_from_mid)    
