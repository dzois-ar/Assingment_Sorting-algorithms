from random import randint


#the fuction which creates three lists of random numbers
def random_t_shirts(size, color, fabric):
    for i in range( 40):
        size.append(randint(1, 7))
        color.append(randint(1, 7))
        fabric.append(randint(1, 7))
    return  size, color, fabric

#Bubble Sort in ascending position
def bubbleSort_asce(data):
    
    n = len(data)
    for i in range(n-1):
        # loop  Sort elements 
        for j in range(0, n-i-1):
            if data[j] > data[j+1]: 
                # Swap data in list
                data[j], data[j+1] = data[j+1],  data[j]    

               





# The function create  forty T-Shrit
def create_t_shirts(size, color, fabric):
    # create the list with size element
    for i in range(len(size)):
        if size[i] == 1:
            size[i] = "XS"
        
        if size[i] == 2:
            size[i] = "S"
            

        if size[i] == 3:
            size[i] = "M"
            
        if size[i] == 4:
            size[i] = "L"
            
        if size[i] == 5:
            size[i] = "XL"
            
        if size[i] == 6:
            size[i] = "XXL"
             
        if size[i] == 7:
            size[i] = "XXXL"

    # create the list with color element
    for i in range(len(color)):
        if color[i] == 1:
            color[i] = "RED"
        
        if color[i] == 2:
            color[i] = "ORANGE"
            

        if color[i] == 3:
            color[i] = "YELLOW"
            
        if color[i] == 4:
            color[i] = "GREEN"
            
        if color[i] == 5:
            color[i] = "BLUE"
            
        if color[i] == 6:
            color[i] = "INDIGO"
             
        if color[i] == 7:
            color[i] = "VIOLET" 

    # create the list with fabric element
    for i in range(len(fabric)):
        if fabric[i] == 1:
            fabric[i] = "WOOL"
        
        if fabric[i] == 2:
            fabric[i] = "COTTON"
            

        if fabric[i] == 3:
            fabric[i] = "POLYESTER"
            
        if fabric[i] == 4:
            fabric[i] = "RAYON"
            
        if fabric[i] == 5:
            fabric[i] = "LINEN"
            
        if fabric[i] == 6:
            fabric[i] = "CASHMERE"
             
        if fabric[i] == 7:
            fabric[i] = "SILK"                      
    
    #print the list of forty t-shirt
    for j in range(40):  
        a = j +1
        print(f"{a}.The T-Shrit has Size:{size[j]}, Color: {color[j]}, fabric:{fabric[j]}")
        
        

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
    print("Sort t-shirts by Size in ascending position with Bubble Sort:")
    bubbleSort_asce(size)
    print("-" *100)
    print("-" *100)
    
    

    #call create_t_shirts() function with its three Arguments
    create_t_shirts(size, color, fabric)

    print("-" *100)
    print("-" *100)
    print("Sort t-shirts by Size in descending position with Bubble Sort: ")
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


