import os

f = open('mapping', 'r')
arr = f.readlines()
f.close()


nameDic = dict()
for idx, ele in enumerate(arr):
    ele = ele.strip()
    
    tmparr = (ele.split('  '))
    vmName = tmparr[0]
    fileName = tmparr[1]
    nameDic[fileName] = vmName

for key in nameDic:
    # print(key)
    if os.path.exists(key):
        os.rename(key, nameDic[key])
    