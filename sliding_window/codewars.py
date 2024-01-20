""" 
Implement the function unique_in_order which takes as argument a sequence and 
returns a list of items without any elements with the same value next to each other and preserving the original order of elements.

For example:

unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
unique_in_order([1, 2, 2, 3, 3])   == [1, 2, 3]
unique_in_order((1, 2, 2, 3, 3))   == [1, 2, 3]
"""



def unique_in_order(sequence):
    if not sequence:
        return []
    # Initialize the result list with the first element
    result = [sequence[0]]
    # Loop through the sequence starting from the second element
    for item in sequence[1:]:
        # If the current item is different from the last item in the result list, append it
        if item != result[-1]:
            result.append(item)

    return result


from itertools import groupby

def unique_in_order(iterable):
    return [k for (k, _) in groupby(iterable)]

print(unique_in_order("AAAABBBCCDAABBB"))