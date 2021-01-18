def binarysr(ls,key):
    low = 0
    high= len(ls)-1
    found = False
    while low<=high  and not found :
        mid= (low+ high)//2
        if key == ls[mid]:
            found = True
            break
        elif key> ls[mid]:
            low= mid+1
        else:
            high = mid-1
    if found == True :
        print("key found ")
    else:
        print("key not found")                    
    

lst=[1,4,294,2,58,993,2985,5664,34,23,66,99,6,234,555,6]
lst.sort()
print(lst)
key = int(input("Enter key element : "))
binarysr(lst,key)
