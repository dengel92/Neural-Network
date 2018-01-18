import itertools as combi
import numpy as num

HIS = ['+', '-']
NAT = ['+', '-']
LEU = ['+', '-']
TRP = ['+', '-']

p = list(combi.product(NAT, HIS, LEU, TRP))
count = 0
for n in combi.combinations(p, 4):
   count += 1
   print(num.matrix(n))
print(count)