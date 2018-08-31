# Written by *** and Eric Martin for COMP9021


'''
Prompts the user for two strictly positive integers, numerator and denominator.

Determines whether the decimal expansion of numerator / denominator is finite or infinite.

Then computes integral_part, sigma and tau such that numerator / denominator is of the form
integral_part . sigma tau tau tau ...
where integral_part in an integer, sigma and tau are (possibly empty) strings of digits,
and sigma and tau are as short as possible.
'''


import sys
from math import gcd


try:
    numerator, denominator = input('Enter two strictly positive integers: ').split()
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
try:
    numerator, denominator = int(numerator), int(denominator)
    if numerator <= 0 or denominator <= 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

def gcd(m, n):
    while m != n:
        if m > n:
            m = m - n
        else:
            n = n - m
    return m
gcd1 = gcd(numerator, denominator)
p = [-1] * 100000000000
q = [-1] * 100000000000
#p = [-1] * (numerator // gcd1) * (denominator // gcd1)
#q = [-1] * (numerator // gcd1) * (denominator // gcd1)
#p = [-1] * numerator
#q = [-1] * numerator
n = numerator // gcd1
m = denominator // gcd1

t = 0
has_finite_expansion = False
integral_part = 0
sigma = ''
tau = ''

if (numerator < denominator):
    o = n
    while (p[o] == -1):
        p[o] = t
        t += 1
        o = o * 10
        q[t] = o // m
        o = o % m
    if p[o] != 0:
        sigma = str(q[1: p[o]+1])
    tau = str(q[p[o]+1: t+1])
    if q[t] == 0:
        has_finite_expansion = True
        tau = ''
elif (numerator > denominator):
    integral_part = n // m
    new_n = n - integral_part * m
    o = new_n
    while (p[o] == -1):
        p[o] = t
        t += 1
        o = o * 10
        q[t] = o // m
        o = o % m
    if p[o] != 0:
        sigma = str(q[1: p[o]+1])
    tau = str(q[p[o]+1: t+1])
    if q[t] == 0:
        has_finite_expansion = True
        tau = ''
        
else:
    integral_part = 1
    has_finite_expansion = True
     
        
        





# Replace this comment with your code

if has_finite_expansion:
    print(f'\n{numerator} / {denominator} has a finite expansion')
else:
    print(f'\n{numerator} / {denominator} has no finite expansion')
if not tau:
    if not sigma:
        print(f'{numerator} / {denominator} = {integral_part}')
    else:
        print(f'{numerator} / {denominator} = {integral_part}.{sigma}')
else:
    print(f'{numerator} / {denominator} = {integral_part}.{sigma}({tau})*')

