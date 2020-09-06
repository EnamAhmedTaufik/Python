def fibonacci(num):
    first=0
    second=1
    while first<=num:
        print(first, end=' ')
        temp = first
        first = second
        second = temp + second
num=int(input('Enter the limit: '))
fibonacci(num)