"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters
and removing all non-alphanumeric characters.

it reads the same forwards and backwards.

"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = ""
        for char in s:
            ascii_val = ord(char)
            if not (ascii_val in range(48, 58) or ascii_val in range(65, 91) or ascii_val in range(97, 123)):
                continue

            if ascii_val in range(65, 91):
                result += chr(ascii_val + 32)
                continue

            result += chr(ascii_val)

        if len(result) == 1:
            return True

        return result == result[::-1]



s = Solution()
print(s.isPalindrome("A man, a plan, a canal: Panama"))

