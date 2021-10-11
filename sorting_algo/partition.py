def partition( l, low, high):
    
    i = low -1
    pivot = l[high]
    
    for j in range( low, high):
        
        if l[j] < pivot:
            i += 1
            l[i], l[j] = l[j], l[i]   
    l[i+1], l[high] = l[high], l[i+1]
    return i+1

def quick_sort(left, right, l):
    
    if left < right:
        pivot = partition(l,left, right)
        quick_sort( left, pivot-1, l)
        quick_sort( pivot+1, right, l)

simple_list = [5,1,3,8,4,7,2,9,0,6]
print(simple_list)
quick_sort(0, len(simple_list)-1,simple_list)
print(simple_list)