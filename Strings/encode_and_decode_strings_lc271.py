# Encode and Decode Strings
# Leetcode 271
# https://leetcode.com/problems/encode-and-decode-strings/

# Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.
# 
# Please implement encode and decode 

def encode(strs: list[str]) -> str:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    res_list: list[str] = []
    for s in strs:
        res_list.append(str(len(s)) + '#' + s)

    return ''.join(res_list)

def decode(str) -> list[str]:
    """
    @param: str: A string
    @return: dcodes a single string to a list of strings
    """
    res: list[str] = []
    i: int = 0

    while i < len(str):
        j: int = i # j will be the location of the # symbol delimiter; from i to j will be num length
        # extract length:
        while str[j] != '#':
            j += 1
        length: int = int(str[i:j])

        # extract word:
        res.appstr[j+1 : j+1+length]

        # start of next delimiter/string pair
        i = j + length + 1

    return res