def consecutive_zero_sum(nums: list[int]) -> int:
    """Given an integer array nums, determine the length of the longest sequence of consecutive ints that sum to zero. If no sequences sum to 0 in nums, return -1

    Examples: 
    [-1, 0, 1, 0, 1] -> 4: the sequence from i=0 to i=3 sums to 0 and is the longest sequence which sums to 0.
    [0, 0, 0] -> 3: The sequence from i=0 to i=2 is the longest sequence which sums to 0.
    [1] -> -1: No sequence in this array sums to 0

    Time complexity: O(n) [iterate multiple times thru entire arrays of length n]
    Space complexity: O(n) [new hashmap and array]

    :param nums: The list of nums
    :type nums: list[int]

    :rtype: int
    :return: Size of the longest consecutive sequence in nums which sums to 0
    """
    # empty list can't sum to 0
    if not nums:
        return -1

    # two types of consecutive 0 sums: those which start from beginning of list and those which do not.

    # first build cuum sum array while finding longest cons zero sum which starts from beginning of list.
    # building the cuum sum array is equivalent to cumulative_sum_array in Arrays.
    cuum_sum_list: list[int] = [nums[0]]
    longest_zero_sum_from_beginning: int = 1 if cuum_sum_list[0] == 0 else -1

    for i in range(1, len(nums)):
        cuum_sum_here = nums[i] + cuum_sum_list[i-1]
        cuum_sum_list.insert(i, cuum_sum_here)

        if cuum_sum_here == 0:
            longest_zero_sum_from_beginning = i+1 # 0 indexed array, length will be index +1

    # next find consecutive 0 sums which do not start from index 0.
    # (these can be found by summing between equal numbers in cuum_sum_list: ie from [1, 3, 1] summing from these indices
    # gives a consecutive zero sum of length 3)
    # finding opposite in this way is nearly identical to two sum hashmap version leetcode also in Arrays.
    seen_sum_map: {int: int} = {}
    longest_zero_sum_from_mid: int = -1

    for i in range(0, len(cuum_sum_list)):
        this_cuum_sum = cuum_sum_list[i]

        if this_cuum_sum in seen_sum_map:
            this_length = i - seen_sum_map.get(this_cuum_sum)
            # only adding cuum sum into the map once (below else statement) will eliminate issues of ex. multiple cuum_sums surrounded by same number
            longest_zero_sum_from_mid = max(this_length, longest_zero_sum_from_mid) 

        else:
            seen_sum_map[this_cuum_sum] = i
    
    # now return the larger of the two sum lengths:
    return max(longest_zero_sum_from_beginning, longest_zero_sum_from_mid)