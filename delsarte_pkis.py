import csv
import argparse
from pathlib import Path
from sympy import *

parser = argparse.ArgumentParser()
parser.add_argument("--n", type=int, default=2)
parser.add_argument("--file_name", type=str, default="delsarte")

args = parser.parse_args()

n = args.n
file_name = args.file_name

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


def calculate_single_value(n, k, i, j, b=q**2.0):
    return simplify(
        (-1)**(k-j) *
        (b**calculate_normal_binomial(k-j, 2)) *
        calculate_product_function(b, n-j, n-k) *
        calculate_product_function(b, n-i, j) *
        (q**((2.0*n*(2.0*n -1))/(2.0*n)))**j
        
    )

def calculate_sum(n, k, i, b=q**2.0):
    j = 0
    result = 0
    while j <= k:
        result += calculate_single_value(n,k,i,j)
        j+=1
    
    return result
    

def delsarte_pkis(n):
    k = 0
    results = [ [ None for i in range(n+1) ] for j in range(n+1) ]

    while k <= n:
        i = 0
        while i <= n:
            results[i][k] = calculate_sum(n,k,i)
            i+=1
        k+=1

    return results


result_table = delsarte_pkis(n)


Path('./output').mkdir(parents=True, exist_ok=True)
f = open(f'output/{file_name}.csv', 'w+')
writer = csv.writer(f)

for i in result_table:
    writer.writerow(i)

print(f"Result has been generated and stored in output/{file_name}.csv")