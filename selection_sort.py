def smallest_element(array_input):
    smallest = array_input[0]
    smallest_index = 0
    for i in range(len(array_input)):
        if array_input[i] < smallest:
            smallest = array_input[i]
            smallest_index = i
    return smallest_index

def selection_sort(array_input):
    new_array = []
    for i in range(len(array_input)):
        smallest = smallest_element(array_input)
        new_array.append(array_input.pop(smallest))
    return new_array

#print(smallest_element([5, 0, 4, 9, 7, 10, 1, 3]))
print(selection_sort([5, 0, 4, 9, 7, 10, 1, 3]))