def is_anagram(first_string, second_string):
    first_string_list = list(first_string.lower())
    second_string_list = list(second_string.lower())

    quick_sort(first_string_list,0,len(first_string_list)-1)
    quick_sort(second_string_list,0,len(second_string_list)-1)


    if len(first_string) != len(second_string):
        return False
    if first_string_list == second_string_list:
        return True
    else:
        return False
    
def quick_sort(numbers, start, end):
    if start < end:
        p = partition(numbers, start, end) 
        quick_sort(numbers, start, p - 1)
        quick_sort(numbers, p + 1, end)


def partition(numbers, start, end):
    pivot = numbers[end]
    delimiter = start - 1

    for index in range(start, end):
        if numbers[index] <= pivot:
          delimiter = delimiter + 1
          numbers[index], numbers[delimiter] = numbers[delimiter], numbers[index]

    numbers[delimiter + 1], numbers[end] = numbers[end], numbers[delimiter + 1]

    return delimiter + 1

# Utilizado a funcao quick_sort do Course da Trybe
