
def add_element(lst: list, element, index: int = None) -> list:
    if index is None:
        lst.append(element)
    else:
        if 0 <= index <= len(lst):  
            lst.insert(index, element)
        else:
            raise IndexError(f"Index {index} out of bounds")
    return lst

def delete_by_value(lst: list, value) -> list:
    try:
        lst.remove(value)
    except ValueError:
        pass  
    return lst

def delete_by_index(lst: list, index: int) -> list:
    
    if 0 <= index < len(lst):
        lst.pop(index)
    else:
        raise IndexError(f"Index {index} out of bounds")
    return lst

def update_element(lst: list, index: int, new_value) -> list:
    if 0 <= index < len(lst):
        lst[index] = new_value
    else:
        raise IndexError(f"Index {index} out of bounds")
    return lst


def selection_sort(lst: list, reverse: bool = False) -> list:
    for i in range(len(lst)):
        extrema_idx = i  
        for j in range(i + 1, len(lst)):
            if (not reverse and lst[j] < lst[extrema_idx]) or (reverse and lst[j] > lst[extrema_idx]):
                extrema_idx = j
        lst[i], lst[extrema_idx] = lst[extrema_idx], lst[i]
    return lst

def bubble_sort(lst: list, reverse: bool = False) -> list:
    n = len(lst)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if (not reverse and lst[j] > lst[j + 1]) or (reverse and lst[j] < lst[j + 1]):
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                swapped = True
        if not swapped:
            break 
    return lst

# Searching Algorithm
def linear_search(lst: list, target) -> bool:
    return target in lst  

# Example Usage
if __name__ == "__main__":
    my_list = [3, 1, 4, 1, 5]
    
    add_element(my_list, 9)          
    add_element(my_list, 2, index=2) 
    delete_by_value(my_list, 1)      