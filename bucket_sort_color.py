from random import randint
from bubble_sort_size import random_t_shirts, create_t_shirts


# The main function that implements BucketSort
def bucketsort_asce(data):
    maxVal = max(data)
    #create a new list 
    bucket = [None] * (maxVal + 1)
    for i in range (len(bucket)):
        bucket[i] = 0

    for i in range(len(data)):
        bucket[data[i]] += 1
    outPos = 0 

    for i in range(len(bucket)):
        for j in range(bucket[i]):
            data[outPos] = i
            outPos += 1
    





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
    print("Sort t-shirts by Color in ascending position with Bucket Sort:")
    bucketsort_asce(color)
    
    print("-" *100)
    print("-" *100)
    

    #call create_t_shirts() function with its three Arguments
    create_t_shirts(size, color, fabric)

    print("-" *100)
    print("-" *100)
    print("Sort t-shirts by Color in descending position with Bucket Sort: ")
    
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