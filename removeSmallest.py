def remove_smallest(numbers):
    
    if len(numbers) >= 1:
        x = min(numbers)
        y = numbers.copy()
        y.remove(x)

        return y
    else:
        return []
