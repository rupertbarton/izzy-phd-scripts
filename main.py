from sympy import *

#inputs are n, i, and k

b, x, k = symbols('b x k')
init_printing(use_unicode=True)

def product_function(b, x, k):
    i = 0
    result = 1
    while i <= k - 1:
        result = simplify(result * ((b**x - b**i) / (b**k - b**i)))
        i+=1
    
    return result
