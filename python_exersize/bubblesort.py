#from goto import with_goto

def bubbleSort(arr):
    n = len(arr)

    for i in range(n):

        for j in range(0,n-i-1):

            if arr[j] > arr[j+1]:

                #python支持直接交换
                arr[j], arr[j+1] = arr[j+1], arr[j]

#arr = [64, 34, 25, 12, 22, 11, 90]

arr = []   #arr = list()
#@with_goto     #必须有,goto,跳转
#label.begin    #标识跳转并开始执行的地方
n = input('Please enter the list number:') #[64, 34, 25, 12, 22, 11, 90]

#if n.isidigit:
try:
    m = int(n)
#    label.beg1
    for x in range(m):    

        num = input('Please enter the number:')
        #if num.isdigit:
        try:
            c = int(num)
            #arr[x] = int(input('Please enter the number:'))
            #向列表中加元素
            arr.append(c)    
            #arr[x] = int(input('Please enter the number:'))
#        except ValueError as e:
        except ValueError:
            print("你输入了非法字符")
#            goto.beg1
#            return None, e
#except ValueError as r:
except ValueError:
    print("你输入了非法字符")
#    goto.begin   #在有跳转标识的地方开始执行
#    return None,r


#        else:
#            print("Please enter a number.")
            


#Python isdigit() 方法检测字符串是否只由数字组成
#else:
#    print("Please Enter a number.")   

print ("Before sort:")
for i in range(len(arr)):
    print ("%d" %arr[i]),

bubbleSort(arr)
print ("After sort:")
for i in range(len(arr)):
    print ("%d" %arr[i]),





'''
def bubbleSort(arr):
    n = len(arr)
 
    # 遍历所有数组元素
    for i in range(n):
 
        # Last i elements are already in place
        for j in range(0, n-i-1):
 
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
 
arr = input('Please enter the list value:') #[64, 34, 25, 12, 22, 11, 90]
 
bubbleSort(arr)
 
print ("排序后的数组:")
for i in range(len(arr)):
    print ("%d" %arr[i]),
'''
