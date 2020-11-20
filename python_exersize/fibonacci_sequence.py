num = int(input('Please enter the number of items:'))
n1=0
n2=1
count=2

if (num <= 0):
    print('Please enter an integer greater than 0.')  
elif (num == 1):
    print(n1)
else:
    print(n1,",",n2,end = ' , ')
while (count < num):
    n = n1 + n2
    print(n,end = ' , ')
    n1 = n2
    n2 = n
    count += 1
