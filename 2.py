# 2. Add Two Numbers
# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

# Definition for singly-linked list.
import math

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class LinkedList:
    def __init__(self, array):
        self.data = array
        self.head = None
    def buildList(self):
        ishead = True
        prev = None
        for i in self.data:
            node = ListNode(i)
            if ishead:
                self.head = node
                prev = node
                ishead = False
            else:
                prev.next = node
                prev = node
        return self
    def __add__(self, other):
        nl = self.head
        nr = other.head
        carry = 0
        result = []
        while nl is not None or nr is not None:
            if nl is None:
                vl = 0
            else:
                vl = nl.val
                nl = nl.next
            if nr is None:
                vr = 0
            else:
                vr = nr.val
                nr = nr.next
            remainder = (vl + vr + carry) % 10
            carry = (vl + vr + carry)//10
            result.append(remainder)
        if carry == 1:
            result.append(1)
        resultList = LinkedList(result)
        resultList.buildList()
        return resultList

    def printList(self):
        node = self.head
        while node is not None:
            print(str(node.val)),
            if node.next is not None:
                print("->"),
            node = node.next
        print('')

def main():
    l1 = LinkedList([2, 9, 6])
    l1.buildList()
    l1.printList()
    print(" + ")
    l2 = LinkedList([3, 4, 9])
    l2.buildList()
    l2.printList()
    print(" = ")
    result = l1 + l2
    result.printList()

if __name__== "__main__":
    main()
            
        