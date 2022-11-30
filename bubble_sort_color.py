from random import randint
from bubble_sort_size import random_t_shirts, create_t_shirts



def bubbleSort_asce(data):
    
    n = len(data)
    for i in range(n-1):
        # loop  Sort elements 
        for j in range(0, n-i-1):
            if data[j] > data[j+1]: 
                # Swap data in list
                data[j], data[j+1] = data[j+1],  data[j]






# main function
if __name__=="__main__":  
    # Driver code
    size = []
    color = []
    fabric = []
    # call random_t_shirts() function with its three Arguments
    random_t_shirts(size, color, fabric)
    print("-" *100)
    print("-" *100)
    print("Sort t-shirts by Color in ascending position with Bubble Sort:")
    bubbleSort_asce(color)
    print("-" *100)
    print("-" *100)
    

    #call create_t_shirts() function with its three Arguments
    create_t_shirts(size, color, fabric)

    print("-" *100)
    print("-" *100)
    print("Sort t-shirts by Color in descending position with Bubble Sort: ")
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
