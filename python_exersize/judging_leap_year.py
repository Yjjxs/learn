#要将输入的数字转化为整型，不然运行时会报错：if (year % 4) == 0: TypeError: not all arguments converted during string formatting
year = int(input('请输入年份：'))
if (year % 4) == 0:
    if (year % 100) == 0:
        if (year % 400) == 0:
            print(f'{year} is leap year')
        else:
            print(f'{year} is not leap year') 
    else:
         print(f'{year} is leap year')
else:
    print(f'{year} is not leap year')


