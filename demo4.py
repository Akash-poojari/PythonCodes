def maxInArray():
    arr = ['82','31','40','78','90','32','120']
 
# Using for loop
    maximum_val= arr[0]
    for i in range(1, len(arr)): 
        if (arr[i] > maximum_val):
            maximum_val = arr[i]

    print(maximum_val)
    print(arr.index(maximum_val))  
maxInArray()