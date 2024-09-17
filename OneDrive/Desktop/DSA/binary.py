def binary_search(a,item):
    l =0
    r =len(a)-1
    mid =l+r/2
    if l>r:
        return "element did not found"
    elif a[mid]==item:
        print(mid)
    elif a[mid]>item:
        r =mid-1
    elif a[mid]<item:
        l =mid+1





















        
     

