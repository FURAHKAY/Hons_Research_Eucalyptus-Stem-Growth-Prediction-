import time
import random

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def quicksort(arr, cutoff):
    # Check if the length of the array is less than or equal to the cutoff
    if len(arr) <= cutoff:
        # If the array is smaller than or equal to the cutoff, use insertion sort
        insertion_sort(arr)
        return arr  # Return the sorted array
    else:
        if len(arr) > 1:
            # If the array is larger than the cutoff, proceed with quicksort
            pivot = arr[random.randint(0, len(arr) - 1)]
            left = [x for x in arr if x < pivot]
            middle = [x for x in arr if x == pivot]
            right = [x for x in arr if x > pivot]
            return quicksort(left, cutoff) + middle + quicksort(right, cutoff)
        else:
            return arr

# Test the implementation
if __name__ == "__main__":
    # Generate a random list
    random.seed(42)
    test_list = [random.randint(0, 1000) for _ in range(1000)]
    # # Test the implementation
    cutoffs = [10, 50, 100, 200]

    for cutoff in cutoffs:
        start_time = time.time()
        sorted_list = quicksort(test_list.copy(), cutoff)
        end_time = time.time()
        print(f"Cutoff: {cutoff}, Time: {end_time - start_time} seconds")