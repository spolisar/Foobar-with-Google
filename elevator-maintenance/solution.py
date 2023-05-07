import functools
# This task seems to basically be writing a custom 
#   comparator function that is used to sort the list
def version_compare(x, y):
    x_split = x.split('.')
    y_split = y.split('.')
    # if two or more versions contain more numbers than the others, 
    #   sort ascending based on number of numbers
    i = 0
    while i < len(x_split) and i < len(y_split):
        x_int = int(x_split[i])
        y_int = int(y_split[i])
        
        if x_int > y_int:
            return 1
        elif x_int < y_int:
            return -1
        i += 1
    
    if len(x_split) < len(y_split):
        return -1
    elif len(x_split) > len(y_split):
        return 1
    else:
        return 0

def solution(versions):
    # this could be done in a single line with looseversion
    #   but that goes against the spirit of the task
    # I'm using cmp_to_key so that this solution also works in
    #   python 3 since cmp is deprecated
    return sorted(versions, key=functools.cmp_to_key(version_compare))
    
