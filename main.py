import csv
from pathlib import Path
from sympy import *

#inputs are n, i, and k

b, x, k, q = symbols('b x k q')
init_printing(use_unicode=True)

def calculate_product_function(b, x, k):
    i = 0
    result = 1
    while i <= k - 1:
        result = simplify(result * ((b**x - b**i) / (b**k - b**i)))
        i+=1
    
    return result


def calculate_normal_binomial(n, k):
    return simplify(factorial(n)/(factorial(k) * factorial(n - k)))


def calculate_single_value(n, k, i, j, b=q**2):
    return simplify(
        -1**(k-j) *
        b**(calculate_normal_binomial(k-j, 2)) *
        calculate_product_function(b, n-j, n-k) *
        calculate_product_function(b, n-i, n-j) *
        q**((2*n*(2*n -1))/(2*n)
        )
    )

def calculate_sum(n, k, i, b=q**2):
    j = 0
    result = 0
    while j <= k:
        result += calculate_single_value(n,k,i,j)
        j+=1
    
    return result
    

def main(n):
    k = 0
    results = [[None] * (n+1)] * (n+1)

    while k <= n:
        i = 0
        while i <= n:
            results[k][i] = calculate_sum(n,k,i)
            i+=1
        k+=1

    return results
