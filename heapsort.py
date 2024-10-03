# Build Max Heap: Rearrange the elements in the array so that they form a max heap.

# Swap and Heapify: Swap the maximum element (at the root) with the last element and 
#restore the heap property.

# Repeat: Continue swapping and heapifying until the entire array is sorted.

# In simpler terms, Heapsort is like organizing a stack of cards with the largest 
#card on top. You repeatedly take the largest card from the top and put it at the end 
#until all cards are sorted from smallest to largest.


class Heapsort:

    def __init__(self):
        pass

    # Builds a max heap from the given list.
    def Make_maxheap(self, my_list, list_size):
        # Start from the last non-leaf node and heapify all nodes in reverse order.
        for node_index in range(list_size - 1 // 2, -1, -1):
            self.Heapify(my_list, list_size, node_index)

    # Adjusts the heap rooted at node_index to maintain the heap property.
    def Heapify(self, my_list, list_size, node_index):
        largest = node_index  # Initialize largest as root
        left_child = 2 * node_index + 1  # Calculate the left child index
        right_child = 2 * node_index + 2  # Calculate the right child index
        # Check if left child exists and if it's greater than the current largest
        if left_child < list_size and my_list[node_index] < my_list[left_child]:
            largest = left_child
        # Check if right child exists and if it's greater than the current largest
        if right_child < list_size and my_list[largest] < my_list[right_child]:
            largest = right_child
        # If the largest element is not the root, swap it with the root and heapify the affected subtree.
        if largest != node_index:
            my_list[node_index], my_list[largest] = my_list[largest], my_list[node_index]  # Swap elements
            self.Heapify(my_list, list_size, largest)

    # Unwinds the heap to extract elements in sorted order.
    def Heap_unwind(self, my_list, list_size):
        # One by one extract elements
        for node_index in range(list_size - 1, 0, -1):
            my_list[node_index], my_list[0] = my_list[0], my_list[node_index]  # Swap the root with the last element
            self.Heapify(my_list, node_index, 0)  # Heapify the reduced heap

    # The main function to perform heapsort.
    def Heapsort(self, my_list):
        list_size = len(my_list)
        # Build a max heap.
        self.Make_maxheap(my_list, list_size)  # Create a max heap
        self.Heap_unwind(my_list, list_size)  # Unwind the heap to extract elements in sorted order
