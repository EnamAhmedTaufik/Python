
def showPalindromicTriangle(number):
    for row in range(1,num+1):
        for space in range(0,num-row):
            print(' ',end=' ')
        for i in range(1,row+1):
            print(i ,end=' ')
        for a in range(row-1,0,-1):
            print(a, end=' ')
        print()
num=int(input('Enter the limit: '))
showPalindromicTriangle(num)