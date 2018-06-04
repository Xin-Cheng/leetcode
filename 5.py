# 5. Longest Palindromic Substring
# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

# Example 1:

# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# Example 2:

# Input: "cbbd"
# Output: "bb"
class MyString:
    def __init__(self, s):
        self.content = s
    def findPalindrome(self):
        index = left = right = 0
        longest = ""
        while index < len(self.content):
            current = ""
            if index > 0 and index < len(self.content) - 1:
                if self.content[index] == self.content[index + 1]:
                    left = index
                else:
                    current = self.content[index]
                    left = index - 1
                right = index + 1
                while left >= 0 and right <= len(self.content) - 1 and self.content[left] == self.content[right]:
                    current = self.content[left] + current + self.content[right]
                    left -= 1
                    right += 1
            else:
                current += self.content[index]
            if len(current) > len(longest):
                longest = current
            index += 1
        return longest

def main():
    myString = MyString("cbbd")
    print(myString.findPalindrome())

if __name__ == "__main__":
    main()
