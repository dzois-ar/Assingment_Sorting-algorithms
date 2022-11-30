from random import randint
from bubble_sort_size import random_t_shirts, create_t_shirts


 
# This Function handles sorting part of quick sort

def partition(start, end, array):
     
    # Initializing pivot's index to start
    pivot_index = start
    pivot = array[pivot_index]
     
    # This loop runs till start pointer crosses
    # end pointer, and when it does we swap the
   
    while start < end:
         
        # Increment the start pointer till it finds an
        # element greater than  pivot
        while start < len(array) and array[start] <= pivot:
            start += 1
             
        
        while array[end] > pivot:
            end -= 1
         
        # If start and end have not crossed each other,
        # swap the numbers on start and end
        if(start < end):
            array[start], array[end] = array[end], array[start]
     
    # Swap pivot element with element on end pointer.
   
    array[end], array[pivot_index] = array[pivot_index], array[end]
    
    # Returning end pointer to divide the array into 2
    return end
     
# The main function that implements QuickSort
def quick_sort(start, end, array):
     
    if (start < end):
         
        # p is partitioning index, array[p]
       
        p = partition(start, end, array)
         
        # Sort elements before partition
        # and after partition
        quick_sort(start, p - 1, array)
        quick_sort(p + 1, end, array)
         

    





# main function
if __name__=="__main__":  
    
    size = []
    color = []
    fabric = []
    # call random_t_shirts() function with its three Arguments
    random_t_shirts(size, color, fabric)
    print("-" *100)
    print("-" *100)
    
    print("Sort t-shirts by Size in ascending position with Quick Sort:")
    #call quick_sort() function with its three Arguments
    quick_sort(0, len(size) - 1, size)
    
    print("-" *100)
    print("-" *100)
    

    #call create_t_shirts() function with its three Arguments
    create_t_shirts(size, color, fabric)

    print("-" *100)
    print("-" *100)
    print("Sort t-shirts by Size in descending position with Quick Sort: ")

    #Sort in descending position
    size.reverse()
    color.reverse()
    fabric.reverse()
    print("-" *100)
    print("-" *100)


    #call create_t_shirts() function with its three Arguments
    create_t_shirts(size, color, fabric)


    print("-" *100)
    print("-" *100)