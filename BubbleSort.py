''' 
def bubblesort(elements):
    size=len(elements) # using len we will get the size of list
    
    for i in range(size-1):
        if elements[i] > elements[i+1]:
            temp=elements[i]
            elements[i]=elements[i+1]
            elements[i+1]=temp


if __name__ == '__main__':
    elements=[5,22,1,3,66,77,8,9,10,] # the output of this is [5, 1, 3, 22, 66, 8, 9, 10, 77]
    bubblesort(elements)
    print(elements)
    '''
    
def bubblesort(elements):
    size=len(elements) # using len we will get the size of list
    
    for i in range(size-1):
        swapped=False
        for j in range(size-1-i): # 
             if elements[j] > elements[j+1]:
                temp=elements[j]
                elements[j]=elements[j+1]
                elements[j+1]=temp
                swapped=True
        if not swapped: # bcz of this  the loop will break early if sorted thats why the time complexity is O(n)   O(n) (when the list is already sorted, because the algorithm will only pass through the list once and exit early)
            break

if __name__ == '__main__':
   # elements=[88,100,5,22,1,3,66,77,8,9,10,] # the output of this is [5, 1, 3, 22, 66, 8, 9, 10, 77]
    
    elements=["shyam","sanjana","bawri"] # bubble sort for String
    bubblesort(elements)
    print(elements)
    