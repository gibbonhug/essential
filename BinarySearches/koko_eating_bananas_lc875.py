# Koko Eating Bananas
# Leetcode 875
# https://leetcode.com/problems/koko-eating-bananas/

def koko_eating_bananas_lc875(piles: list[int], h: int) -> int:
    """Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

    Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

    Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.

Time Complexity: O(n*log(max(piles)))
Space Complexity: O(1)

:param piles: The list of piles Koko wants to eat as slowly as possible
:type piles: list[int]
:param h: The number of hours Koko has to eat all the piles
:type h: int

:rtype: int
:return: The slowest eating speed k by which Koko can eat all the piles in h hours
"""
    # Minimize k, such that hours taken <= h

    # Bounds for speed (k)
    lo = 1
    hi = max(piles)

    # Start min valid k as max(piles) (== hi), since eating this many bananas an hour will be fastest valid time
    # While loop will binary search to find slowest valid value for this variable
    min_valid_k = hi 

    while lo <= hi:
        k = lo + ((hi - lo) // 2)

        this_time_taken = getHoursToEatAllPilesGivenK(piles, k)

        if this_time_taken > h:
            # This time is too slow: Increase lower bound speed
            lo = k + 1
        else:
            # This time valid (able to eat all bananas): Set min_valid_k to this time and decrease upper bound speed
            min_valid_k = k
            hi = k - 1

    return min_valid_k


    # Helper Inner Functions

    def getHoursToEatAllPilesGivenK(piles: list[int], k: int) -> int:
        hours = 0

        for pile in piles:
            hours += getHoursToEatPileGivenK(pile, k)

        return hours

    def getHoursToEatPileGivenK(pile: int, k: int) -> int:
        return ceil(pile / k)