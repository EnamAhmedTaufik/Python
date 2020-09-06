# to do
def division(starting,ending,first_divisor,second_divisor):
    sum=0
    for i in range(starting,ending):
        if i%first_divisor==0 and i%second_divisor==0:
            continue
        elif i%first_divisor==0:
            sum=sum+i
        elif i % second_divisor == 0:
            sum = sum + i
    return sum
starting=int(input())
ending=int(input())
first_divisor=int(input())
second_divisor=int(input())

print(division(starting,ending,first_divisor,second_divisor))