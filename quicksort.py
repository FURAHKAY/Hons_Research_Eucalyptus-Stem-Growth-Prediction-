# Select Pivot: Choose a pivot element from the array.

# Partitioning: Rearrange the array so that elements smaller than the pivot 
#are on its left, and elements greater than the pivot are on its right.

# Recursively Sort: Apply the same process to the sub-arrays on the left 
#and right of the pivot until the entire array is sorted.

# In simple terms, Quicksort picks a point (pivot), rearranges the 
#elements so that everything smaller than the pivot is on one side, and 
#everything larger is on the other side. Then it repeats the process for each 
#side until everything is in order.



def Quicksort(my_list):
    # Base case: If the list has 1 or fewer elements, it is already sorted
    if len(my_list) <= 1:
        return my_list
    else:
        # Choose the first element as the pivot
        pivot = my_list[0]
        i = 0
        # Partitioning step: Arrange elements smaller than the pivot to the left of it and larger ones to the right
        for j in range(0, len(my_list) - 1):
            # If the current element is less than the pivot, swap it with the element at position i + 1
            if my_list[j + 1] < pivot:
                my_list[j + 1], my_list[i + 1] = my_list[i + 1], my_list[j + 1]
                i += 1
        # Swap the pivot element with the element at position i
        my_list[0], my_list[i] = my_list[i], my_list[0]
        # Recursively sort the elements to the left and right of the pivot
        first_part = Quicksort(my_list[:i])  # Quicksort the left partition
        second_part = Quicksort(my_list[i + 1:])  # Quicksort the right partition
        # Append the pivot element to the end of the sorted left partition
        first_part.append(my_list[i])
        # Concatenate the sorted left partition, pivot element, and sorted right partition
        return first_part + second_part
