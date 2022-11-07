def largest_even_sum(arr: List[int]) -> int:
    """Given an integer array arr, return the greatest possible even sum which can be summed from elements of arr.

    Time complexity: O(nlogn) [sorting array]
    Space complexity: O(1) [disregard sorting array]

    :param arr: The list of nums
    :type arr: List[int]

    :rtype: int
    :return: Largest possible even sum which can be formed from elements of arr
    """
    running_total: int = 0

    # 'stack' of odd nums; no need to make an actual stack since we are sorting the array,
    # so it is easy to know when adding 2 odds will increase the running_total sum
    prev_odd: int = 0 
    this_odd: int = 0
    num_odd: int = 0

    arr.sort()

    for num in reversed(arr):
        # an even number which will increase running total
        if (num % 2 == 0) and (running_total + num > running_total):
            running_total += num
        # odd
        elif (num % 2 == 1):
            prev_odd = this_odd
            this_odd = num
            num_odd += 1

        if num_odd == 2 and this_odd + prev_odd > 0:
            running_total += this_odd
            running_total += prev_odd
            # empty 'stack'
            this_odd = 0
            prev_odd = 0
            num_odd = 0
        
        # no use going down into negative numbers
        if (num < 0) and (prev_odd <= 0):
            break
    
    return running_total