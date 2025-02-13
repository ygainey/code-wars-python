# input is an unsorted list of 3 positive integers
def pythagorean_triple(integers):
    # return True if it is possible to form a Pythagorean triple with the 3 integers
    # return False if it is not possible
    integers.sort()
    x = integers[0]
    y = integers[1]
    z = integers[2]
    
    if x**2 + y**2 == z**2:
        return True
    else:
        return False