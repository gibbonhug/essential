def largest_even_sum(arr: List[int]) -> List[int]:
    running_total: int = 0

    prev_odd: int = 0
    this_odd: int = 0
    num_odd: int = 0

    arr.sort()

    for num in reversed(arr):
        if (num % 2 == 0) and (running_total + num > running_total):
            running_total += num
        elif (num % 2 == 1):
            prev_odd = this_odd
            this_odd = num
            num_odd += 1

        if num_odd == 2 and this_odd + prev_odd > 0:
            running_total += this_odd
            this_odd = 0
            running_total += prev_odd
            prev_odd = 0
            num_odd = 0
        
        # no use going down into negative numbers
        if (num < 0) and (prev_odd < 0):
            break