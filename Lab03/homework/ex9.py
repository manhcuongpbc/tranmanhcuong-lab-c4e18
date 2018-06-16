def get_even_list(l):
    even_list = []
    for i in l:
        if i % 2 == 0:
            even_list.append(i)
    return(even_list)
even_list = get_even_list([-1,2,1,3,4,6])
print(even_list)