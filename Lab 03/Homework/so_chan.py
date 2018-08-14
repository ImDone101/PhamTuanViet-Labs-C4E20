def get_even_list(l):
    soeven = []
    for i in range (len(l)):
        if l[i] % 2 == 0:
            soeven.append(l[i])
    return soeven

# even_list = get_even_list([2, 3, 4, 5, -10, 9, 8])
# print(even_list)
even_list = get_even_list([1, 2, 5, -10, 9, 6])

if set(even_list) == set([2, -10, 6]):
    print("Your function is correct")
else:
    print("Ooops, bugs detected")
