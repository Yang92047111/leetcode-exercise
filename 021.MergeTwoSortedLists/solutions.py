# Definition for singly-linked list.
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: list[ListNode], list2: list[ListNode]) -> list[ListNode]:
        head = ListNode()
        curr = head

        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            
            curr = curr.next

        curr.next = list1 or list2
        return head.next
    
if __name__ == '__main__':
    # ListNode{val: 1, next: ListNode{val: 2, next: ListNode{val: 4, next: None}}}
    def list_to_linked_list(nums):
        if not nums:
            return None
        
        head = ListNode(nums[0])
        current = head

        for num in nums[1:]:
            current.next = ListNode(num)
            current = current.next
            
        return head
    
    def are_equal_linked_lists(head1, head2):
        current1 = head1
        current2 = head2
        
        while current1 and current2:
            if current1.val != current2.val:
                return False
            
            current1 = current1.next
            current2 = current2.next
        
        if current1 or current2:
            return False
        
        return True
    
    sol = Solution()

    test_case = {}
    result = {}
    
    test_case['case1'] = [[1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4]]
    test_case['case2'] = [[], [], []]
    test_case['case3'] = [[], [0], [0]]

    for key, val in test_case.items():
        ans = sol.mergeTwoLists(list_to_linked_list(val[0]), list_to_linked_list(val[1]))
        valid = list_to_linked_list(val[2])
        res = are_equal_linked_lists(ans, valid)
        if res:
            result[key] = key + ' pass'
        else:
            result[key] = key + ' false'

    print (result)