def minimumSwap(arr):
    count=0
    i=0
    while i< len(arr):
        index=arr[i]-1

        if arr[i] != arr[index]:
            arr[i],arr[index]=arr[index],arr[i]
            count+=1
        else:
            i+=1
    return count
arr = [1,4,3,2,5,8,9,6]
print(minimumSwap(arr))
