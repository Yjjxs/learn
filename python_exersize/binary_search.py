#递归处理（还有点问题）
from bubblesort1 import bubbleSort

def binerySearch(arr,a,r,x):
    #元素多于一个
    if r:
        mid = int(1+(r-1)/2)
    
        #元素正好再中间
        if arr[mid] == x:
            return mid

        #小于中间位置数字
        elif arr[mid] > x:
            return binerySearch(arr,a,mid-1,x)
        
        else:
            return binerySearch(arr,a,mid+1,x)
    
    #不存在
    else:
        return -1

arr = [3,1,55,43,28,67,79,346,361,234,43,33,456,3435]

bubbleSort(arr)
for i in range(len(arr)):
    print("%d"%arr[i])

x = int(input("请输入要找的数字："))
#x=4

res = binerySearch(arr,0,len(arr)-1,x)

if res != -1:
    print ("元素在数组中的索引为 %d" % res )
else:
    print("元素不在数组中")


