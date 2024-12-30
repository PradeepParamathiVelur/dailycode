value=int(input(('Enter the Value = ')))
for x in range(value):
    for y in range(value):
        if(x==0 or x==value-1):
            print('* ',end="")
        else:
            if(y==0 or y==value-1):
                print('* ',end="")
            else:
                print('  ',end='')

    print(end='\n')