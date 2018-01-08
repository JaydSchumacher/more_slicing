list = [0,1,2,3,4,5,6,7,8,9,10,11,12,13]

def first_4(list):
    return(list[:4])

def first_and_last_4(list):
    return(list[:4] + list[-4:])

def odds(list):
    return(list[1::2])

def reverse_evens(list):
    new_list = list[::2]
    return(new_list[-1::-1])


print(reverse_evens(list))
