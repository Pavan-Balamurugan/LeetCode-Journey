def swap_pairs(head):
    if not head or not head.next:
        return head
    
    new_head = head.next
    prev = None
    
    while head and head.next:
        first = head
        second = head.next
        
        # Swap
        first.next = second.next
        second.next = first
        
        if prev:
            prev.next = second
        
        prev = first
        head = first.next
    
    return new_head

# Output:
# Original list:        
# 1 2 3 4
# Swapped list:
# 2 1 4 3

# Time Complexity: O(n) where n is the number of nodes in the linked list.
# Space Complexity: O(1) since we are swapping nodes in place without using extra space

