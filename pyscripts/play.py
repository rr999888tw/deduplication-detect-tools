import re

ent = "timeNeeded=2019666  filename=dat/data-16mb-19.dat  filename2=dat/data-16mb-62.dat  interval=9  cache=1"

for ele in ent.strip().split("  "):
    if '=' in ele:
        tmp = ele.split('=')
        print(tmp)

# print(m.group(0))
# import numpy as np

# def gen_exponential_rand(B):
#     return np.random.exponential(B)

# def gen_normal_rand(mean, dev):
#     return (np.random.normal(mean, dev))
    
# def gen_poisson_rand(seed):
#     return (np.random.poisson(seed))

# while (True):
#     print ( gen_poisson_rand(10))