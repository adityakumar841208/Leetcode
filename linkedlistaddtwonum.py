# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.first = None
        self.last = None

    def insert(self,val):
        if self.first == None:
            self.first = self.last = ListNode(val)

        else:
            self.last.next = ListNode(val)
            self.last = self.last.next


class Solution:
    def addTwoNumbers(self, li1, li2):
        sum1 = sum2 = 0
        index = 0
        while li1.first != None:
            sum1 += li1.first.val * 10**index
            index += 1
            li1.first = li1.first.next

        index = 0
        while li2.first != None:
            sum1 += li2.first.val * 10**index
            index += 1
            li2.first = li2.first.next

        print(sum1,sum2)

        li3 = LinkedList()
        while int(sum1) / 10 > 0:
            modulo = sum1 % 10
            li3.insert(int(modulo))
            sum1 /= 10

        return li3

list1 = [2,4,3]
list2 = [5,6,4]

li1 = LinkedList()
li2 = LinkedList()

for data in list1:
    li1.insert(data)

for data in list2:
    li2.insert(data)

# while li1.first != None:
#     print(li1.first.val)
#     li1.first = li1.first.next

solution = Solution()
li3 = solution.addTwoNumbers(li1,li2)

while li3.first != None:
    print(li3.first.val)
    li3.first = li3.first.next