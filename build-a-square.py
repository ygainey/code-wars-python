def generate_shape(n):
    x = ""
    for i in range(n):
        x += (n * '+' + '\n')
    
    return x.strip()