# 3. Longest Substring Without Repeating Characters
# Given a string, find the length of the longest substring without repeating characters.

# Examples:

# Given "abcabcbb", the answer is "abc", which the length is 3.

# Given "bbbbb", the answer is "b", with the length of 1.

# Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

class MyString:
    def __init__(self, s):
        self.content = s
    def distSubstring(self):
        result = []
        temp = []
        for c in self.content:
            if c in temp:
                if len(temp) > len(result):
                    result = temp
                idx = temp.index(c)
                temp = temp[idx+1:len(result)]
            temp.append(c)
        return "".join(result)

def main():
    myString = MyString("pwwkew")
    print(myString.distSubstring())

if __name__ == "__main__":
    main()