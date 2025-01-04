# -------------------------cyclic_sort in python

def cycle_sort(arr):
    n=len(arr)
    # length = 5

    for cyclestart in range(0,n-1):
        item=arr[cyclestart]
        pos=cyclestart
        for i in range(cyclestart+1, n):
            if(arr[i]<item):
                pos+=1
        
        if(pos==cyclestart):
            continue

        while(item==arr[pos]):
            pos+=1
        arr[pos],item=item,arr[pos]

        while(pos!=cyclestart):
            pos=cyclestart
            for i in range(cyclestart+1, n):
                if(arr[i]<item):
                    pos+=1

            while(item==arr[pos]):
                pos+=1
            arr[pos],item=item,arr[pos]
    return arr

arr=[3,2,7,5,3,5,2,3,3,3,1,0]
result=cycle_sort(arr)
print(result)