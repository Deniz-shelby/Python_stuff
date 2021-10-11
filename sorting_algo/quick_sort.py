def quick_sort(left, right, l):
    
    if left < right:
        pivot = partition(l,left, right)
        quick_sort( left, pivot-1, l)
        quick_sort( pivot+1, right, l)

simple_list = [5,1,3,8,4,7,2,9,0,6]
quick_sort(0, len(simple_list)-1,simple_list)