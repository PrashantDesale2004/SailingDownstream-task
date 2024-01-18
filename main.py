
def checklist(my_list):
    if len(my_list) % 10 != 0:
        print("Error: length of list is not a multiple of 10")

    for i in range(0,len(my_list)):        
        if(i%2==0 or i%3==0):
            my_list.remove(i)
    
    return my_list

