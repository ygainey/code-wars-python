def flick_switch(lst):
    x = True
    acc = []
    for i in lst:
        if i == 'flick':
            x = not x
        
        acc.append(x)

    return acc