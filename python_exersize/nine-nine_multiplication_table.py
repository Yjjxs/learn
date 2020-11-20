#range(1,10) 依次取从1到9，range(10),是从0到9，所以要是取10就是到11
for i in range(1,10):
    for j in range(1,i+1):
        #\t 横向跳到下一个制表符  end=' ',末尾加个空字符串而不是换行符（python3）
        print('{}*{}={}\t'.format(j,i,i*j),end = ' ')
    print()
