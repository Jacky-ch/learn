for i in range(1,10):
    for j in range(1,i+1):
        print( '%d X %d = %d' % (j,i,i*j),end = ' ' )
    print('  ')

a=1
b=0
while b-9:
    b += 1
    for i in range(b,b+1):
        for j in range(a,10):
            print('{}X{}={}'.format(i,j,i*j),end=' ')
        print('  ')