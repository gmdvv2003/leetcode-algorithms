# Link: https://leetcode.com/problems/merge-k-sorted-lists/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        listsValues = []

        for curItem in lists:
            while curItem:
                listsValues.append(curItem.val)
                if curItem.next == None:
                    break

                curItem = curItem.next

        listsValues.sort()
        
        if len(listsValues) == 0:
            return None

        mergedKList = ListNode(listsValues[0])
        mergedKListRoot = mergedKList

        for index in range(1, len(listsValues)):
            mergedKList.next = ListNode(listsValues[index])
            mergedKList = mergedKList.next

        return mergedKListRoot