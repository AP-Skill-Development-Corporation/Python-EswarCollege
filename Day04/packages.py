def evenOdd(number):
    if number%2 == 0:
        print('Even Number')
    else:
        print('Odd Number')

def num_factor(n):
    for i in range(1, n+1):
        if n%i == 0:
            print(i)