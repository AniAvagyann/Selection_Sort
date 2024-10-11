
def selection_sort(array, index=0):
    n = len(array)
    
    if index >= n - 1:
        return
   
    min_index = index
   
    for i in range(index + 1, n):
        
        if array[i] < array[min_index]:
           
            min_index = i
   
    array[index], array[min_index] = array[min_index], array[index]

    selection_sort(array, index + 1)

array = [17, 5, 89, 100, 1, 49, 77, 27, 3, 15]
selection_sort(array)
print("Sorted Array:", array)