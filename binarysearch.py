#A binary search with python. 
my_list = [num for num in range(0, 101)] # create a list from 0 to 100


# it sould be sorted
#create upper limit
upper = max(my_list)
#create lower limit
lower = min(my_list)
target  = int(input('enter input: '))
count = 0 
while lower < upper: 
    middle = int((upper + lower)/2)
    count  += 1

    if target == middle or target == lower or target == upper:
        print('Found! The number '+ str(target) +' was found after ' + str(count-1) + ' half slices')
        break
    elif target < middle:
         upper = middle
         middle = int((lower + upper)/2)
         
    else:
        lower = middle
        middle = int((lower+upper)/2)
        