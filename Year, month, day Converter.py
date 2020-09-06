usr_input = int(input('Enter the number of Days: '))

def numberofdays(day):

    years=usr_input//365
    print(years,'years,',end='')
    mon=usr_input%365
    month=mon//30
    print(month,'months,',end='')
    days=mon%30
    print(days,'days',end='')
numberofdays(usr_input)