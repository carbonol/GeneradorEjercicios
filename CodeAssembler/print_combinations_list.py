def add_elemts_to_list(lst, elemts_list):
    if type(elemts_list) != list:
        raise TypeError('El parámetro elemts_list en la función add_elemts_to_list no es de tipo list')
    if type(lst) != list:
        raise TypeError('El parámetro lst en la función add_elemts_to_list no es de tipo list')

    num_elemts_list = len(elemts_list)    
    if (len(lst) == 0):
        for i in range(0, num_elemts_list, 1):
            inner_list = []
            inner_list.append(elemts_list[i])
            lst.append(inner_list)
        return lst
    else:
        new_list = []
        num_indexes_list = len(lst)
        for i in range(0, num_indexes_list, 1):
            num_indexes_sublist = len(lst[i])

            sublist_element = []
            for j in range(0, num_indexes_sublist, 1):                
                sublist_element.append(lst[i][j])

                
            for k in range(0, num_elemts_list, 1):
                inner_sublist_element = sublist_element.copy()
                inner_sublist_element.append(elemts_list[k])
                new_list.append(inner_sublist_element)

        lst = new_list
        return lst

def get_subroutine_possible_variants_list(subroutine_index, variant_count_per_subroutine_list): # OK
    if type(subroutine_index) != int:
        raise TypeError('El parámetro subroutine_index en la función get_subroutine_possible_variants_list no es de tipo int')
    if type(variant_count_per_subroutine_list) != list:
        raise TypeError('El parámetro variant_count_per_subroutine_list en la función get_subroutine_possible_variants_list no es de tipo list')

    num_variants = variant_count_per_subroutine_list[subroutine_index]
    lst = []
    for i in range(1, num_variants + 1, 1):
        lst.append(i)
    return lst

def get_possible_variants_list(num_subroutines, variant_count_per_subroutine_list):
    if type(num_subroutines) != int:
        raise TypeError('El parámetro num_subroutines en la función get_possible_variants_list no es de tipo int')
    if type(variant_count_per_subroutine_list) != list:
        raise TypeError('El parámetro variant_count_per_subroutine_list en la función get_possible_variants_list no es de tipo list')

    lst = []
    for i in range(0, num_subroutines, 1):
        subroutine_possible_variants_list = get_subroutine_possible_variants_list(i, variant_count_per_subroutine_list)
        lst = add_elemts_to_list(lst, subroutine_possible_variants_list)
    return lst

def gen_variant_combinations_list(variant_count_per_subroutine_list): # OK
    if type(variant_count_per_subroutine_list) != list:
        raise TypeError('El parámetro variant_count_per_subroutine_list en la función gen_variant_combinations_list no es de tipo list')

    num_subroutines = len(variant_count_per_subroutine_list)
    return get_possible_variants_list(num_subroutines, variant_count_per_subroutine_list)

# # Main Program / Programa Principal # OK
# variant_count_per_subroutine_list = [2, 2, 3, 2]
# # print(gen_variant_combinations_list(variant_count_per_subroutine_list))
# lst = gen_variant_combinations_list(variant_count_per_subroutine_list)
# num = 1
# for i in lst:
#     print(num,':',i)
#     num = num + 1