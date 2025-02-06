class Solution:
    def pairSum(self, head):
        
        # Step 1: Find the middle of the list
        slow = head
        fast = head
        prev = None
        
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        # Step 2: Break the link to separate the first and second halves
        prev.next = None
        
        # Step 3: Reverse the second half
        curr = slow
        prev = None
        while curr:
            next_node = curr.next  # Save next node
            curr.next = prev  # Reverse pointer
            prev = curr  # Move prev forward
            curr = next_node  # Move curr forward

        # Step 4: Iterate through both halves and calculate the twin sum
        first_half = head
        second_half = prev  # Reversed second half
        max_val = 0
        
        while second_half:
            twin_sum = first_half.val + second_half.val
            max_val = max(max_val, twin_sum)
            first_half = first_half.next
            second_half = second_half.next
        
        return max_val
            
                    
            
            
            
                