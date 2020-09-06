def calculateTax(age,salary,desingnation):
    if age<18:
        return 0
    elif desingnation=='president':
        return 0
    elif salary<10000:
        return 0
    elif 10000<= salary<=20000:
        a=salary*0.05
        return a
    elif salary>20000:
        b=salary*0.1
        return b
age=int(input('Enter age: '))
salary=int(input('Enter salary: '))
desingnation=str(input('Enter desingnation: '))
print(calculateTax(age,salary,desingnation))


