def groceryStore(cost,location) :
    sum=0
    a_dict={'Rice':105,'Potato':20,'Chicken':250,'Beef':510,'Oil':85}
    order=[str(x) for x in input().split()]

    for i in order:
        if i in a_dict:
            sum += a_dict[i]
    total=sum
    if location=='Dhanmondi':
        total=total+70
    return total

print(groceryStore(sum,location='Dhanmondi'))