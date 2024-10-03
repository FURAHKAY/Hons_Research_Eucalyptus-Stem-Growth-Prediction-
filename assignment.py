class double_linked_list:
   
    def __init__(self, data_value, pointer_to_previous=None, pointer_to_next=None):
        self.data = data_value
        self.previous = pointer_to_previous
        self.next = pointer_to_next

# Driver code
if __name__ == "__main__":
    # Create nodes for the doubly linked list
    head = double_linked_list(0)
    current = head
    
    # Create the rest of the doubly linked list
    for i in range(1, 10):
        new_node = double_linked_list(i)
        current.next = new_node
        new_node.previous = current
        current = current.next
    
    # Traverse the list and print the values
    current = head
    while current:
        print(current.data)
        current = current.next
