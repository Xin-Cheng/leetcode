# 4. Median of Two Sorted Arrays
# There are two sorted arrays nums1 and nums2 of size m and n respectively.

# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

# Example 1:
# nums1 = [1, 3]
# nums2 = [2]

# The median is 2.0
# Example 2:
# nums1 = [1, 2]
# nums2 = [3, 4]

# The median is (2 + 3)/2 = 2.5
from __future__ import division

class MyArray:
    def __init__(self, arr1, arr2):
        self.first = arr1
        self.second = arr2
    def findMedian(self):
        totalLength = len(self.first) + len(self.second)
        leftCount = (totalLength - 1) // 2
        firstIndex = 0
        secondIndex = 0
        first = 0
        second = 0
        while leftCount > 0 :
            if self.first[firstIndex] < self.second[secondIndex]:
                firstIndex += 1
            else:
                secondIndex += 1
            leftCount -= 1
        maxValue = max(self.first[len(self.first) - 1], self.second[len(self.second) - 1])
        median = min(self.first[firstIndex], self.second[secondIndex])
        largeMedian = max(self.first[firstIndex], self.second[secondIndex])
        if firstIndex == len(self.first) - 1:
            first = maxValue
        else: 
            first == self.first[firstIndex + 1]
        if secondIndex == len(self.second) - 1:
            second = maxValue
        else:
            second = self.second[secondIndex + 1]
        if totalLength % 2 == 1:
            return median
        else:
            nextMedian = min(first, second, largeMedian)
            return (median + nextMedian)/2

def main():
    nums1 = [1, 2]
    nums2 = [3, 4]
    myArray = MyArray(nums1, nums2)
    print(myArray.findMedian())
    cdd = 1

if __name__ == "__main__":
    main()