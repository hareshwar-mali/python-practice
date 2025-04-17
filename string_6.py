# Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.
# Example 1:
# Input: str1 = "ABCABC", str2 = "ABC"
# Output: "ABC"
# Example 2:
# Input: str1 = "ABABAB", str2 = "ABAB"
# Output: "AB"
# Example 3:
# Input: str1 = "LEET", str2 = "CODE"
# Output: ""

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def gcd_of_strings(str1, str2):
    if str1 + str2 != str2 + str1:
        return ""

    # Find GCD of lengths without using math module
    gcd_len = gcd(len(str1), len(str2))
    return str1[:gcd_len]
