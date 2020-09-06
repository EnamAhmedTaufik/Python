usr_input=str(input('Enter:'))
remove=int(input('Enter index num:'))

list1=[]
def removeindex(sentence,position):
    for char in usr_input:
        list1.append(char)
    for item in range(0,len(list1)):
        list1.pop(position)
        position=position*2
    for value in list1:
        print(value,end='')
removeindex(usr_input,remove)