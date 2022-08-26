def swappper(my_items):
    my_items_str =[]
    my_items_int =[]
    for i in range(0,len(my_items)):
        if type(my_items[i])==str:
            my_items_str.append(my_items[i])
            my_items_str.sort()
        elif type(my_items[i])==int:
            my_items_int.append(my_items[i])
            my_items_int.sort()
        my_new = my_items_int + my_items_str
        
    return print(my_new)


swappper([11,'queen',2,'ling'])