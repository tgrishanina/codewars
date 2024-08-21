def rgb(r, g, b):
    r = max(0, min(255, r))
    g = max(0, min(255, g))
    b = max(0, min(255, b))
        
    x = r % 16
    i = r // 16
    y = g % 16
    j = g // 16
    z = b % 16
    k = b // 16
    return (hex(i)[2:] + hex(x)[2:]  + hex(j)[2:]  + hex(y)[2:]  + hex(k)[2:]  + hex(z)[2:]).upper() 


# shorter and cleverer

def rgb(r, g, b): 
    return ''.join(['%02X' % max(0, min(x, 255)) for x in [r, g, b]])