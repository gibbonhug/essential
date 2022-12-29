def to_string(num: int) -> str:
    """Given an integer, return this integer represented as a string

    :param num: The number to convert
    :type num: int

    :rtype: str
    :return: num param as a string
    """
    digits = "0123456789"
    # base 10 number

    if num < 10:
        return digits[num]
    
    return to_string(num // 10) + digits[num % 10]